#!/usr/bin/env python3
"""Builds the Blast data files.

Reads the ingredient table from scripts/foods_data.py and the recipe rows from
the scripts/recipes_*.py modules, then writes Blast/Resources/foods.json and
Blast/Resources/recipes.json. Nothing in Resources/ is edited by hand.

    python3 scripts/build_data.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from foods_data import FOODS, ANIMAL, DAIRY, NUTS, CAFFEINE, GLUTEN, NOT_ANIMAL, NOT_DAIRY

CATEGORY_ORDER = [
    "fruit", "frozen", "greens", "vegetable", "liquid", "dairy",
    "protein", "nutSeed", "grain", "flavor", "sweetener", "alcohol", "other",
]

CUP_ML = 236.588

def flags(fid, cat):
    return {
        "isAnimal": (cat == "dairy" and fid not in NOT_ANIMAL) or fid in ANIMAL,
        "isDairy": (cat == "dairy" and fid not in NOT_DAIRY) or fid in DAIRY,
        "hasNuts": fid in NUTS,
        "hasCaffeine": fid in CAFFEINE,
        "isAlcohol": cat == "alcohol",
        "hasGluten": fid in GLUTEN,
    }


def default_unit(food):
    (fid, name, cat, kcal, p, c, fib, sug, fat,
     gpc, gpp, piece, liquid, aliases) = food
    if cat == "protein" and piece == "scoop":
        return "piece"
    if cat in ("nutSeed", "sweetener", "flavor", "other") and gpc:
        return "tbsp"
    if liquid:
        return "cup"
    if piece and cat in ("fruit", "vegetable"):
        return "piece"
    if gpc:
        return "cup"
    return "gram"


def build_food(food):
    (fid, name, cat, kcal, p, c, fib, sug, fat,
     gpc, gpp, piece, liquid, aliases) = food
    ml_per_gram = (CUP_ML / gpc) if gpc else 1.0
    # Leaves fill the cup loosely and pack down to almost nothing once the
    # blades start, so their loose-cup volume badly overstates vessel load.
    if cat == "greens":
        ml_per_gram = min(ml_per_gram, 3.0)
    return {
        "id": fid,
        "name": name,
        "category": cat,
        "per100g": {
            "kcal": kcal, "protein": p, "carbs": c,
            "fiber": fib, "sugar": sug, "fat": fat,
        },
        "gramsPerCup": gpc,
        "gramsPerPiece": gpp,
        "pieceName": piece,
        "isLiquid": liquid,
        "mlPerGram": round(ml_per_gram, 4),
        "defaultUnit": default_unit(food),
        "aliases": aliases,
        "flags": flags(fid, cat),
    }


RECIPE_GROUPS = [
    ("smoothie", "SMOOTHIES"),
    ("green", "GREENS"),
    ("protein", "PROTEIN"),
    ("coffee", "COFFEE"),
    ("breakfast", "BREAKFAST"),
    ("dessert", "DESSERT"),
    ("cocktail", "COCKTAIL"),
    ("mocktail", "MOCKTAIL"),
    ("kids", "KIDS"),
    ("wellness", "WELLNESS"),
    ("savory", "SAVORY"),
]


def program_for(category, ingredients):
    """Ninja's own rule: CRUSH is for frozen drinks, BLEND for everything else."""
    if category in ("cocktail", "mocktail"):
        return "crush"
    ice = next((amt for fid, amt, unit in ingredients if fid == "ice" and unit == "cup"), 0)
    return "crush" if ice >= 0.75 else "blend"


def grams_of(food, amount, unit):
    gpc = food["gramsPerCup"]
    gpp = food["gramsPerPiece"]
    fallback_cup = gpc if gpc else 236.588 / food["mlPerGram"]
    if unit == "gram":
        return amount
    if unit == "milliliter":
        return amount / food["mlPerGram"]
    if unit == "cup":
        return amount * fallback_cup
    if unit == "tbsp":
        return amount * fallback_cup / 16
    if unit == "tsp":
        return amount * fallback_cup / 48
    if unit == "piece":
        return amount * (gpp if gpp else 100)
    raise ValueError(unit)


# Portions are written at a natural ratio, then scaled to the vessel. Only the
# bulk of the drink shrinks — a scoop of protein or a teaspoon of cinnamon
# stays put, because halving those changes the recipe rather than the serving.
BULK = {"liquid", "fruit", "frozen", "dairy", "greens", "vegetable", "alcohol"}
TARGET_ML = {1: 380.0, 2: 440.0}


def round_amount(amount, unit):
    if unit == "cup":
        return max(round(amount * 4) / 4, 0.25)
    if unit in ("tbsp", "tsp"):
        return max(round(amount * 2) / 2, 0.5)
    if unit == "piece":
        return max(round(amount * 4) / 4, 0.25)
    return max(round(amount / 5) * 5, 5)


def volume_of(foods_by_id, ingredients):
    total = 0.0
    for fid, amount, unit in ingredients:
        food = foods_by_id[fid]
        total += grams_of(food, amount, unit) * food["mlPerGram"]
    return total


def fit_to_vessel(foods_by_id, ingredients, servings):
    target = TARGET_ML.get(servings, 450.0)
    for _ in range(6):
        volume = volume_of(foods_by_id, ingredients)
        if volume <= target:
            return ingredients
        bulk_volume = sum(
            grams_of(foods_by_id[f], a, u) * foods_by_id[f]["mlPerGram"]
            for f, a, u in ingredients if foods_by_id[f]["category"] in BULK
        )
        fixed_volume = volume - bulk_volume
        room = target - fixed_volume
        if bulk_volume <= 0 or room <= 0:
            return ingredients
        factor = room / bulk_volume
        scaled = []
        for fid, amount, unit in ingredients:
            if foods_by_id[fid]["category"] in BULK:
                scaled.append((fid, round_amount(amount * factor, unit), unit))
            else:
                scaled.append((fid, amount, unit))
        if scaled == ingredients:
            return ingredients
        ingredients = scaled
    return ingredients


UNITS = ("gram", "milliliter", "cup", "tbsp", "tsp", "piece")


def collect_rows():
    """Every recipe row from every module, as (id, name, category, servings,
    prep, ingredients, tip).

    recipes_data.py came first and groups its rows by category in named lists.
    Every module added since is a flat RECIPES list that carries the category
    on each row, which is what a new file should use.
    """
    import importlib
    import glob

    rows = []
    import recipes_data
    for category, attr in RECIPE_GROUPS:
        for rid, name, servings, prep, ingredients, tip in getattr(recipes_data, attr):
            rows.append((rid, name, category, servings, prep, ingredients, tip))

    here = os.path.dirname(os.path.abspath(__file__))
    for path in sorted(glob.glob(os.path.join(here, "recipes_*.py"))):
        module_name = os.path.splitext(os.path.basename(path))[0]
        if module_name == "recipes_data":
            continue
        module = importlib.import_module(module_name)
        rows.extend(getattr(module, "RECIPES"))
    return rows


def build_recipes(foods_by_id):
    valid_categories = {c for c, _ in RECIPE_GROUPS}
    out = []
    seen = set()
    seen_names = {}
    for rid, name, category, servings, prep, ingredients, tip in collect_rows():
        assert rid not in seen, f"duplicate recipe id {rid}"
        seen.add(rid)
        key = name.strip().lower()
        assert key not in seen_names, f"duplicate recipe name {name!r} ({rid} and {seen_names[key]})"
        seen_names[key] = rid
        assert category in valid_categories, f"{rid}: unknown category {category}"
        # Drinks are 1 or 2; a dressing or a dip legitimately makes four portions.
        assert 1 <= servings <= 4, f"{rid}: servings out of range"
        assert ingredients, f"{rid}: no ingredients"
        for fid, amount, unit in ingredients:
            assert fid in foods_by_id, f"{rid}: unknown ingredient {fid}"
            assert unit in UNITS, f"{rid}: bad unit {unit}"
            assert amount > 0, f"{rid}: non-positive amount for {fid}"
            if unit == "piece":
                assert foods_by_id[fid]["gramsPerPiece"], \
                    f"{rid}: {fid} has no piece weight, use another unit"
        # Nothing blends without liquid past the MIN line; the machine just spins.
        assert any(foods_by_id[fid]["isLiquid"] or foods_by_id[fid]["category"] in ("liquid", "dairy", "frozen")
                   for fid, _, _ in ingredients), f"{rid}: no liquid or frozen ingredient"
        ingredients = fit_to_vessel(foods_by_id, ingredients, servings)
        out.append({
            "id": rid,
            "name": name,
            "category": category,
            "program": program_for(category, ingredients),
            "servings": servings,
            "prepMinutes": prep,
            "totalMinutes": prep + 1,
            "ingredients": [
                {"foodID": fid, "amount": amount, "unit": unit}
                for fid, amount, unit in ingredients
            ],
            "tip": tip,
        })
    return out


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "Blast", "Resources")
    os.makedirs(out_dir, exist_ok=True)

    ids = [f[0] for f in FOODS]
    assert len(ids) == len(set(ids)), "duplicate food id"
    for f in FOODS:
        assert f[2] in CATEGORY_ORDER, f"unknown category {f[2]} on {f[0]}"

    foods = [build_food(f) for f in FOODS]
    path = os.path.join(out_dir, "foods.json")
    with open(path, "w") as fh:
        json.dump(foods, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {len(foods)} foods -> {path}")

    by_id = {f["id"]: f for f in foods}
    recipes = build_recipes(by_id)
    path = os.path.join(out_dir, "recipes.json")
    with open(path, "w") as fh:
        json.dump(recipes, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {len(recipes)} recipes -> {path}")
    report(recipes, by_id)


def report(recipes, by_id):
    from collections import Counter
    counts = Counter(r["category"] for r in recipes)
    print("  by category:", dict(counts))

    oversized = []
    for r in recipes:
        volume = sum(
            grams_of(by_id[i["foodID"]], i["amount"], i["unit"]) * by_id[i["foodID"]]["mlPerGram"]
            for i in r["ingredients"]
        )
        kcal = sum(
            grams_of(by_id[i["foodID"]], i["amount"], i["unit"]) / 100 * by_id[i["foodID"]]["per100g"]["kcal"]
            for i in r["ingredients"]
        )
        r["_volume"] = volume
        r["_kcal"] = kcal / r["servings"]
        if volume > 470:
            oversized.append((r["id"], round(volume)))
    fits_blast = sum(1 for r in recipes if r["_volume"] <= 400)
    print(f"  fits Blast 16 oz: {fits_blast}/{len(recipes)}")
    print(f"  over Blast MAX 20 oz: {len(oversized)}")
    if oversized:
        print("   ", oversized[:12])
    kcals = sorted(r["_kcal"] for r in recipes)
    print(f"  kcal/serving: min {kcals[0]:.0f}, median {kcals[len(kcals)//2]:.0f}, max {kcals[-1]:.0f}")
    for r in recipes:
        del r["_volume"]
        del r["_kcal"]


if __name__ == "__main__":
    main()
