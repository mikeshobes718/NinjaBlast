"""Savoury blends for the Blast: cold soups, dressings, sauces, dips and salty sippers."""

RECIPES = [
    # ------------------------------------------------------------ cold soups
    ("sv-sevilla-red", "Sevilla Red", "savory", 2, 8, [
        ("tomato", 3, "piece"),
        ("cucumber", 0.5, "piece"),
        ("bell_pepper", 0.5, "piece"),
        ("olive_oil", 2, "tbsp"),
        ("cider_vinegar", 1, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Blend the tomatoes alone first so they release their juice — that liquid is what carries everything else around the blade."),

    ("sv-melon-rojo", "Melon Rojo", "savory", 2, 6, [
        ("watermelon", 1.5, "cup"),
        ("tomato", 1, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("jalapeno", 0.5, "piece"),
        ("salt", 0.5, "tsp"),
    ], "Salt the watermelon and let it sit five minutes before blending; it draws out juice and stops the soup tasting like a fruit cup."),

    ("sv-ajo-blanco", "Ajo Blanco", "savory", 2, 7, [
        ("grapes", 1, "cup"),
        ("almonds", 4, "tbsp"),
        ("water", 0.5, "cup"),
        ("olive_oil", 3, "tbsp"),
        ("cider_vinegar", 1, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Soak the almonds in hot tap water for ten minutes first — the Blast's single blade will not break down dry almonds smoothly."),

    ("sv-pepino-verde", "Pepino Verde", "savory", 1, 6, [
        ("cucumber", 1.5, "piece"),
        ("bell_pepper_green", 0.5, "piece"),
        ("cilantro", 3, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("olive_oil", 2, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Leave the cucumber skin on for colour but scrape the seeds out, or the soup goes watery and bitter within an hour."),

    ("sv-smoked-pepper-gazpacho", "Smoked Pepper Gazpacho", "savory", 2, 5, [
        ("roasted_pepper", 1, "cup"),
        ("tomato_juice", 0.5, "cup"),
        ("almonds", 2, "tbsp"),
        ("cider_vinegar", 1, "tbsp"),
        ("olive_oil", 2, "tbsp"),
        ("smoked_paprika", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Jarred roasted peppers are packed in brine, so taste before you add the full half teaspoon of salt."),

    ("sv-cordoba-salmorejo", "Cordoba Salmorejo", "savory", 2, 6, [
        ("tomato", 3, "piece"),
        ("oats", 0.25, "cup"),
        ("olive_oil", 3, "tbsp"),
        ("cider_vinegar", 2, "tsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Rolled oats stand in for the stale bread and thicken as they sit — blend, wait five minutes, then blend again for the proper velvet."),

    ("sv-chilled-avocado-soup", "Chilled Avocado Soup", "savory", 1, 5, [
        ("avocado", 1, "piece"),
        ("broth_veg", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("cilantro", 2, "tbsp"),
        ("jalapeno", 0.5, "piece"),
        ("salt", 0.5, "tsp"),
    ], "Broth goes in before the avocado, always — put the fat in first and it packs under the blade and spins."),

    ("sv-tarator", "Tarator", "savory", 1, 6, [
        ("cucumber", 1, "piece"),
        ("kefir", 0.75, "cup"),
        ("walnuts", 2, "tbsp"),
        ("dill", 2, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("cider_vinegar", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Pulse in short bursts so the walnuts stay a little gritty; blitzed to paste they turn the soup grey."),

    ("sv-beet-buttermilk-chill", "Beet and Buttermilk Chill", "savory", 1, 5, [
        ("beet", 0.75, "cup"),
        ("buttermilk", 0.75, "cup"),
        ("dill", 2, "tbsp"),
        ("horseradish", 1, "tsp"),
        ("cider_vinegar", 2, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Vacuum-packed cooked beets are the shortcut here — raw beet will not break down in this cup."),

    ("sv-golden-carrot-chill", "Golden Carrot Chill", "savory", 1, 5, [
        ("carrot_juice", 0.75, "cup"),
        ("carrot", 1, "piece"),
        ("coconut_milk_light", 0.25, "cup"),
        ("ginger", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Slice the raw carrot into coins no thicker than a pencil, or you will be chewing your soup."),

    ("sv-pea-and-mint-chill", "Pea and Mint Chill", "savory", 1, 4, [
        ("peas_frozen", 1, "cup"),
        ("broth_veg", 0.75, "cup"),
        ("greek_yogurt_2", 0.25, "cup"),
        ("mint", 2, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Let the peas thaw on the counter ten minutes; frozen-solid they behave like ice and dull the mint."),

    ("sv-chilled-corn-velvet", "Chilled Corn Velvet", "savory", 1, 5, [
        ("corn_frozen", 1, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("cashew_butter", 1, "tbsp"),
        ("nutritional_yeast", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("smoked_paprika", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Nutritional yeast does the work that a parmesan rind would do in a hot soup — savoury depth with no cooking."),

    # ------------------------------------------------------- dressings
    ("sv-emerald-herb-dressing", "Emerald Herb Dressing", "savory", 2, 5, [
        ("avocado", 0.5, "piece"),
        ("parsley", 4, "tbsp"),
        ("greek_yogurt_2", 0.25, "cup"),
        ("lemon_juice", 3, "tbsp"),
        ("capers", 1, "tbsp"),
        ("olive_oil", 2, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Capers stand in for the anchovy — they bring the same salty funk and the dressing stays vegetarian."),

    ("sv-blender-caesar", "Blender Caesar", "savory", 2, 4, [
        ("mayonnaise", 3, "tbsp"),
        ("lemon_juice", 3, "tbsp"),
        ("parmesan", 2, "tbsp"),
        ("capers", 1, "tbsp"),
        ("dijon", 1, "tsp"),
        ("worcestershire", 1, "tsp"),
        ("garlic", 0.5, "tsp"),
    ], "This is a small pour and the blade needs something to catch — tip the cup on its side and pulse rather than running it flat."),

    ("sv-lemon-tahini-drizzle", "Lemon Tahini Drizzle", "savory", 2, 3, [
        ("tahini", 4, "tbsp"),
        ("lemon_juice", 3, "tbsp"),
        ("water", 0.25, "cup"),
        ("garlic", 0.5, "tsp"),
        ("cumin", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Tahini seizes into cement the moment acid hits it — keep blending past that point and the water brings it back glossy."),

    ("sv-miso-ginger-dressing", "Miso Ginger Dressing", "savory", 2, 4, [
        ("miso", 1, "tbsp"),
        ("rice_vinegar", 3, "tbsp"),
        ("ginger", 1, "tbsp"),
        ("avocado_oil", 3, "tbsp"),
        ("sesame_oil", 1, "tsp"),
        ("honey", 1, "tsp"),
    ], "White miso is already salty, so taste before reaching for the salt shaker."),

    ("sv-serrano-cilantro-vinaigrette", "Serrano Cilantro Vinaigrette", "savory", 2, 4, [
        ("cilantro", 5, "tbsp"),
        ("lime_juice", 3, "tbsp"),
        ("olive_oil", 3, "tbsp"),
        ("serrano", 0.5, "piece"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Use the cilantro stems, not just the leaves — they carry more flavour and they break down fine in a blender."),

    ("sv-honey-dijon-shake-up", "Honey Dijon Shake-Up", "savory", 2, 3, [
        ("dijon", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("cider_vinegar", 2, "tbsp"),
        ("olive_oil", 3, "tbsp"),
        ("shallot", 0.5, "piece"),
        ("black_pepper", 0.5, "tsp"),
    ], "Mustard is an emulsifier, so this one holds together for days in the fridge without separating."),

    ("sv-balsamic-shallot-vinaigrette", "Balsamic Shallot Vinaigrette", "savory", 2, 3, [
        ("balsamic", 3, "tbsp"),
        ("olive_oil", 4, "tbsp"),
        ("shallot", 0.5, "piece"),
        ("dijon", 1, "tsp"),
        ("thyme", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], None),

    ("sv-cracked-pepper-kefir-ranch", "Cracked Pepper Kefir Ranch", "savory", 2, 4, [
        ("kefir", 0.25, "cup"),
        ("sour_cream", 3, "tbsp"),
        ("dill", 1, "tbsp"),
        ("scallion", 1, "piece"),
        ("lemon_juice", 1, "tbsp"),
        ("black_pepper", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Kefir brings the tang that buttermilk would and it thickens overnight — make it thinner than you want it."),

    ("sv-peanut-lime-dressing", "Peanut Lime Dressing", "savory", 2, 4, [
        ("peanut_butter", 3, "tbsp"),
        ("lime_juice", 3, "tbsp"),
        ("water", 0.25, "cup"),
        ("fish_sauce", 1, "tsp"),
        ("ginger", 1, "tsp"),
        ("sriracha", 1, "tsp"),
        ("honey", 1, "tsp"),
    ], "Fish sauce is the salt here — a teaspoon disappears into the peanut and leaves only depth behind."),

    ("sv-gochujang-sesame-dressing", "Gochujang Sesame Dressing", "savory", 2, 3, [
        ("gochujang", 1, "tbsp"),
        ("rice_vinegar", 3, "tbsp"),
        ("coconut_aminos", 1, "tbsp"),
        ("sesame_oil", 1, "tsp"),
        ("honey", 1, "tsp"),
        ("sesame_seeds", 1, "tsp"),
    ], "Add the sesame seeds after the blend and stir them in, or you lose the pop of whole seed entirely."),

    ("sv-poppy-seed-shallot-dressing", "Poppy Seed Shallot Dressing", "savory", 2, 3, [
        ("cider_vinegar", 2, "tbsp"),
        ("avocado_oil", 4, "tbsp"),
        ("honey", 1, "tbsp"),
        ("dijon", 1, "tsp"),
        ("shallot", 0.5, "piece"),
        ("poppy_seeds", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], None),

    # -------------------------------------------------- sauces and pastes
    ("sv-cilantro-pepita-pesto", "Cilantro Pepita Pesto", "savory", 2, 5, [
        ("cilantro", 6, "tbsp"),
        ("pumpkin_seeds", 3, "tbsp"),
        ("olive_oil", 4, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Toasted pepitas make this taste cooked without a stove — buy them roasted and salted and pull the added salt back."),

    ("sv-arugula-walnut-pesto", "Arugula Walnut Pesto", "savory", 2, 5, [
        ("arugula", 1, "cup"),
        ("walnuts", 3, "tbsp"),
        ("parmesan", 2, "tbsp"),
        ("olive_oil", 4, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("garlic", 0.5, "tsp"),
    ], "Arugula turns bitter under a long blend, so stop as soon as it is green and grainy rather than chasing smooth."),

    ("sv-mint-pistachio-pesto", "Mint Pistachio Pesto", "savory", 2, 5, [
        ("mint", 4, "tbsp"),
        ("parsley", 4, "tbsp"),
        ("pistachios", 3, "tbsp"),
        ("olive_oil", 4, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Half mint, half parsley — straight mint alone reads like toothpaste on lamb or peas."),

    ("sv-almond-romesco", "Almond Romesco", "savory", 2, 5, [
        ("roasted_pepper", 0.75, "cup"),
        ("almonds", 4, "tbsp"),
        ("olive_oil", 3, "tbsp"),
        ("cider_vinegar", 1, "tbsp"),
        ("smoked_paprika", 1, "tsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "This is thick enough to stall the blade: run it, stop, shake the cup hard, run it again until it moves on its own."),

    ("sv-green-table-salsa", "Green Table Salsa", "savory", 2, 6, [
        ("bell_pepper_green", 1, "piece"),
        ("jalapeno", 1, "piece"),
        ("cilantro", 4, "tbsp"),
        ("lime_juice", 3, "tbsp"),
        ("onion", 0.25, "piece"),
        ("olive_oil", 1, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Pull the ribs and seeds from the jalapeno if you want the flavour without the burn — the heat lives there, not in the flesh."),

    ("sv-fire-roasted-table-salsa", "Fire-Roasted Table Salsa", "savory", 2, 5, [
        ("tomato", 2, "piece"),
        ("serrano", 1, "piece"),
        ("cilantro", 3, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("smoked_paprika", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Pulse, do not blend — a held button turns salsa into pink foam in about four seconds."),

    ("sv-harissa-honey-drizzle", "Harissa Honey Drizzle", "savory", 2, 3, [
        ("harissa", 1, "tbsp"),
        ("tomato_paste", 1, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("olive_oil", 3, "tbsp"),
        ("honey", 1, "tsp"),
        ("cumin", 0.5, "tsp"),
    ], "A teaspoon of honey does not make this sweet, it just rounds off harissa's sharp edge."),

    ("sv-parsley-chimichurri", "Parsley Chimichurri", "savory", 2, 5, [
        ("parsley", 6, "tbsp"),
        ("olive_oil", 4, "tbsp"),
        ("cider_vinegar", 2, "tbsp"),
        ("garlic", 1, "tsp"),
        ("cayenne", 0.25, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Chimichurri wants texture, so give it three one-second pulses and let it rest half an hour instead of blending it smooth."),

    ("sv-red-enchilada-sauce", "Red Enchilada Sauce", "savory", 2, 4, [
        ("tomato_paste", 3, "tbsp"),
        ("broth_chicken", 0.75, "cup"),
        ("chili_powder", 1, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("cider_vinegar", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Blended cold it tastes raw and dusty; the oil and the chili powder only bloom once it hits a hot pan or a hot tray of enchiladas."),

    ("sv-soy-citrus-marinade", "Soy Citrus Marinade", "savory", 2, 3, [
        ("soy_sauce", 3, "tbsp"),
        ("orange_juice", 0.25, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("ginger", 1, "tbsp"),
        ("garlic", 1, "tsp"),
        ("sesame_oil", 1, "tsp"),
    ], "Citrus this acidic starts breaking the surface of fish down fast — thirty minutes is plenty, overnight is too long."),

    ("sv-mojo-garlic-marinade", "Mojo Garlic Marinade", "savory", 2, 4, [
        ("orange_juice", 0.25, "cup"),
        ("lime_juice", 3, "tbsp"),
        ("olive_oil", 3, "tbsp"),
        ("garlic", 1, "tbsp"),
        ("cumin", 1, "tsp"),
        ("coriander_ground", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "A full tablespoon of garlic sounds like a lot until you remember it is going on pork shoulder, not into a salad."),

    # ------------------------------------------------------ dips and spreads
    ("sv-lemon-garlic-hummus", "Lemon Garlic Hummus", "savory", 2, 5, [
        ("chickpeas", 1, "cup"),
        ("tahini", 3, "tbsp"),
        ("lemon_juice", 3, "tbsp"),
        ("water", 0.25, "cup"),
        ("olive_oil", 1, "tbsp"),
        ("garlic", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Whip the tahini, lemon and water into a pale cream before the chickpeas go anywhere near the cup — that order is the whole trick."),

    ("sv-roasted-pepper-hummus", "Roasted Pepper Hummus", "savory", 2, 5, [
        ("chickpeas", 0.75, "cup"),
        ("roasted_pepper", 0.5, "cup"),
        ("tahini", 2, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("smoked_paprika", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Pat the peppers dry first or the brine they are packed in thins this into a sauce."),

    ("sv-green-herb-hummus", "Green Herb Hummus", "savory", 2, 5, [
        ("chickpeas", 0.75, "cup"),
        ("spinach", 0.5, "cup"),
        ("dill", 2, "tbsp"),
        ("tahini", 2, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("water", 0.25, "cup"),
        ("salt", 0.5, "tsp"),
    ], "It will look drab straight after blending and turn properly green about a minute later as the spinach breaks down."),

    ("sv-white-bean-and-olive-spread", "White Bean and Olive Spread", "savory", 2, 5, [
        ("white_beans", 1, "cup"),
        ("olive_green", 6, "piece"),
        ("olive_oil", 3, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("water", 0.25, "cup"),
        ("rosemary", 1, "tsp"),
        ("garlic", 0.5, "tsp"),
    ], "The olives carry all the salt this needs, so taste before you add any — and strip the rosemary needles off the woody stem."),

    ("sv-whipped-feta-and-honey", "Whipped Feta and Honey", "savory", 2, 4, [
        ("feta", 0.75, "cup"),
        ("greek_yogurt_whole", 0.25, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("olive_oil", 2, "tbsp"),
        ("honey", 2, "tsp"),
        ("black_pepper", 0.5, "tsp"),
    ], "Block feta in brine, never the pre-crumbled kind — crumbles are coated in anti-caking starch and whip up chalky."),

    ("sv-blender-tzatziki", "Blender Tzatziki", "savory", 2, 6, [
        ("cucumber", 1, "piece"),
        ("greek_yogurt_whole", 0.5, "cup"),
        ("dill", 2, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Squeeze the grated cucumber in a tea towel first — skip it and you have soup by dinner."),

    ("sv-smoky-zucchini-tahini-dip", "Smoky Zucchini Tahini Dip", "savory", 2, 5, [
        ("zucchini", 1, "cup"),
        ("tahini", 3, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("olive_oil", 1, "tbsp"),
        ("smoked_paprika", 1, "tsp"),
        ("garlic", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Smoked paprika is doing the job the charred skin does in real baba ganoush — go heavier on it than feels right."),

    ("sv-herbed-labneh", "Herbed Labneh", "savory", 2, 4, [
        ("labneh", 0.75, "cup"),
        ("parsley", 3, "tbsp"),
        ("mint", 1, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("olive_oil", 2, "tbsp"),
        ("salt", 0.5, "tsp"),
    ], "Labneh is thick enough to cavitate — add the lemon and oil first so there is something liquid at the blade."),

    ("sv-smoky-black-bean-dip", "Smoky Black Bean Dip", "savory", 2, 4, [
        ("black_beans", 1, "cup"),
        ("salsa", 3, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.25, "cup"),
        ("cumin", 0.5, "tsp"),
        ("smoked_paprika", 1, "tsp"),
        ("salt", 0.5, "tsp"),
    ], "Rinse canned beans until the water runs clear; the starchy packing liquid is what makes bean dips taste tinny."),

    # -------------------------------------------------------- savoury drinks
    ("sv-garden-mary", "Garden Mary", "savory", 1, 4, [
        ("tomato_juice", 1, "cup"),
        ("celery", 0.5, "piece"),
        ("lemon_juice", 1, "tbsp"),
        ("horseradish", 1, "tsp"),
        ("worcestershire", 1, "tsp"),
        ("olive_oil", 1, "tsp"),
        ("black_pepper", 0.5, "tsp"),
    ], "A teaspoon of olive oil sounds odd in a tomato drink until you taste how it rounds the acid and carries the pepper."),

    ("sv-virgin-michelada", "Virgin Michelada", "savory", 1, 3, [
        ("tomato_juice", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("olive_green", 3, "piece"),
        ("worcestershire", 1, "tsp"),
        ("tajin", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Rim the glass with chili-lime seasoning and lime first, and spoon in a little olive brine with the olives — that is the salt."),

    ("sv-celery-salt-cooler", "Celery Salt Cooler", "savory", 1, 4, [
        ("celery_juice", 0.75, "cup"),
        ("apple_green", 0.5, "piece"),
        ("cucumber", 0.5, "piece"),
        ("hemp_hearts", 2, "tsp"),
        ("lemon_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "The green apple is there for acid and body, not sweetness — a red apple makes this taste like a juice bar."),

    ("sv-pepino-con-chile", "Pepino con Chile", "savory", 1, 4, [
        ("cucumber", 1.5, "piece"),
        ("water", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("chia", 1, "tsp"),
        ("tajin", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Stir the chia in after the blend and give it two minutes to swell — dropped in with everything else it welds itself to the blade."),

    ("sv-cold-miso-broth", "Cold Miso Broth", "savory", 1, 3, [
        ("broth_veg", 1, "cup"),
        ("miso", 1, "tbsp"),
        ("scallion", 1, "piece"),
        ("ginger", 1, "tsp"),
        ("rice_vinegar", 1, "tsp"),
        ("tamari", 0.5, "tsp"),
        ("sesame_oil", 0.5, "tsp"),
    ], "Miso clumps against cold broth, so blend it with a splash first and then pour the rest in."),

    ("sv-salted-cumin-lassi", "Salted Cumin Lassi", "savory", 1, 4, [
        ("yogurt_plain", 0.75, "cup"),
        ("water", 0.5, "cup"),
        ("mint", 1, "tbsp"),
        ("cumin", 0.5, "tsp"),
        ("salt", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Toast the cumin in a dry pan for thirty seconds and crush it — ground straight from the jar it tastes like dust here."),

    ("sv-kimchi-tomato-sipper", "Kimchi Tomato Sipper", "savory", 1, 3, [
        ("tomato_juice", 0.75, "cup"),
        ("kimchi", 0.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("gochujang", 0.5, "tsp"),
        ("sesame_oil", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Use the kimchi brine from the bottom of the jar as part of the measure — that is where the sourness lives."),
]
