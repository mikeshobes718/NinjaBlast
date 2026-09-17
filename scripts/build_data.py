#!/usr/bin/env python3
"""Source of truth for the Blast ingredient database.

Emits Blast/Resources/foods.json. Values are per 100 g, from standard
USDA-style reference data. Re-run after editing: python3 scripts/build_data.py
"""
import json
import os

# id, name, category, kcal, protein, carbs, fiber, sugar, fat,
# grams_per_cup, grams_per_piece, piece_name, is_liquid, aliases
FOODS = [
    # ---- fruit ----
    ("banana", "Banana", "fruit", 89, 1.1, 22.8, 2.6, 12.2, 0.3, 150, 118, "medium banana", False, []),
    ("banana_frozen", "Frozen banana slices", "frozen", 89, 1.1, 22.8, 2.6, 12.2, 0.3, 150, None, None, False, []),
    ("strawberry", "Strawberries", "fruit", 32, 0.7, 7.7, 2.0, 4.9, 0.3, 144, 12, "berry", False, []),
    ("strawberry_frozen", "Frozen strawberries", "frozen", 35, 0.7, 8.4, 2.1, 5.2, 0.2, 145, None, None, False, []),
    ("blueberry", "Blueberries", "fruit", 57, 0.7, 14.5, 2.4, 10.0, 0.3, 148, None, None, False, []),
    ("blueberry_frozen", "Frozen blueberries", "frozen", 51, 0.4, 12.2, 2.7, 8.5, 0.6, 155, None, None, False, []),
    ("raspberry", "Raspberries", "fruit", 52, 1.2, 11.9, 6.5, 4.4, 0.7, 123, None, None, False, []),
    ("blackberry", "Blackberries", "fruit", 43, 1.4, 9.6, 5.3, 4.9, 0.5, 144, None, None, False, []),
    ("berries_mixed_frozen", "Mixed frozen berries", "frozen", 50, 1.0, 12.0, 3.5, 7.0, 0.4, 140, None, None, False, []),
    ("cherry", "Sweet cherries", "fruit", 63, 1.1, 16.0, 2.1, 12.8, 0.2, 154, None, None, False, []),
    ("cherry_frozen", "Frozen dark cherries", "frozen", 60, 1.0, 15.0, 2.0, 12.5, 0.3, 140, None, None, False, []),
    ("cranberry_frozen", "Frozen cranberries", "frozen", 46, 0.4, 12.2, 4.6, 4.0, 0.1, 110, None, None, False, []),
    ("mango", "Mango", "fruit", 60, 0.8, 15.0, 1.6, 13.7, 0.4, 165, 200, "medium mango", False, []),
    ("mango_frozen", "Frozen mango chunks", "frozen", 60, 0.8, 15.0, 1.6, 13.7, 0.4, 165, None, None, False, []),
    ("pineapple", "Pineapple", "fruit", 50, 0.5, 13.1, 1.4, 9.9, 0.1, 165, None, None, False, []),
    ("pineapple_frozen", "Frozen pineapple chunks", "frozen", 50, 0.5, 13.1, 1.4, 9.9, 0.1, 165, None, None, False, []),
    ("peach", "Peach", "fruit", 39, 0.9, 9.5, 1.5, 8.4, 0.3, 154, 150, "medium peach", False, []),
    ("peach_frozen", "Frozen peach slices", "frozen", 40, 0.9, 9.6, 1.6, 8.5, 0.2, 155, None, None, False, []),
    ("pear", "Pear", "fruit", 57, 0.4, 15.2, 3.1, 9.8, 0.1, 140, 178, "medium pear", False, []),
    ("apple", "Apple", "fruit", 52, 0.3, 13.8, 2.4, 10.4, 0.2, 125, 182, "medium apple", False, []),
    ("apple_green", "Green apple", "fruit", 52, 0.3, 13.8, 2.4, 10.4, 0.2, 125, 182, "medium apple", False, ["granny smith"]),
    ("applesauce", "Unsweetened applesauce", "fruit", 42, 0.2, 11.3, 1.1, 9.4, 0.1, 244, None, None, False, []),
    ("orange", "Orange", "fruit", 47, 0.9, 11.8, 2.4, 9.4, 0.1, 180, 131, "medium orange", False, []),
    ("clementine", "Clementine", "fruit", 47, 0.9, 12.0, 1.7, 9.2, 0.2, 180, 74, "clementine", False, ["mandarin"]),
    ("grapefruit", "Grapefruit", "fruit", 42, 0.8, 10.7, 1.6, 6.9, 0.1, 230, 246, "whole grapefruit", False, []),
    ("kiwi", "Kiwi", "fruit", 61, 1.1, 14.7, 3.0, 9.0, 0.5, 177, 69, "kiwi", False, []),
    ("watermelon", "Watermelon", "fruit", 30, 0.6, 7.6, 0.4, 6.2, 0.2, 152, None, None, False, []),
    ("cantaloupe", "Cantaloupe", "fruit", 34, 0.8, 8.2, 0.9, 7.9, 0.2, 160, None, None, False, []),
    ("honeydew", "Honeydew melon", "fruit", 36, 0.5, 9.1, 0.8, 8.1, 0.1, 170, None, None, False, []),
    ("grapes", "Grapes", "fruit", 69, 0.7, 18.1, 0.9, 15.5, 0.2, 151, None, None, False, []),
    ("avocado", "Avocado", "fruit", 160, 2.0, 8.5, 6.7, 0.7, 14.7, 150, 150, "medium avocado", False, []),
    ("papaya", "Papaya", "fruit", 43, 0.5, 10.8, 1.7, 7.8, 0.3, 145, None, None, False, []),
    ("guava", "Guava", "fruit", 68, 2.6, 14.3, 5.4, 8.9, 1.0, 165, 55, "guava", False, []),
    ("passionfruit", "Passion fruit", "fruit", 97, 2.2, 23.4, 10.4, 11.2, 0.7, 236, 18, "passion fruit", False, []),
    ("dragonfruit", "Dragon fruit", "fruit", 60, 1.2, 13.0, 3.0, 8.0, 0.4, 227, None, None, False, ["pitaya"]),
    ("pomegranate_arils", "Pomegranate arils", "fruit", 83, 1.7, 18.7, 4.0, 13.7, 1.2, 174, None, None, False, []),
    ("fig", "Fresh fig", "fruit", 74, 0.8, 19.2, 2.9, 16.3, 0.3, 149, 50, "fig", False, []),
    ("date", "Medjool date", "fruit", 277, 1.8, 75.0, 6.7, 66.5, 0.2, 178, 24, "date", False, []),
    ("raisin", "Raisins", "fruit", 299, 3.1, 79.2, 3.7, 59.2, 0.5, 145, None, None, False, []),
    ("apricot_dried", "Dried apricots", "fruit", 241, 3.4, 62.6, 7.3, 53.4, 0.5, 130, 8, "half", False, []),
    ("prune", "Prunes", "fruit", 240, 2.2, 63.9, 7.1, 38.1, 0.4, 174, 9, "prune", False, []),
    ("acai_puree", "Unsweetened acai puree", "frozen", 70, 1.0, 4.0, 2.0, 1.0, 5.0, 200, 100, "frozen pack", False, []),
    ("coconut_shredded", "Unsweetened shredded coconut", "nutSeed", 660, 6.9, 23.7, 16.3, 7.4, 64.5, 80, None, None, False, []),

    # ---- greens & vegetables ----
    ("spinach", "Spinach", "greens", 23, 2.9, 3.6, 2.2, 0.4, 0.4, 30, None, None, False, ["baby spinach"]),
    ("kale", "Kale", "greens", 49, 4.3, 8.8, 3.6, 2.3, 0.9, 40, None, None, False, []),
    ("romaine", "Romaine lettuce", "greens", 17, 1.2, 3.3, 2.1, 1.2, 0.3, 47, None, None, False, []),
    ("chard", "Swiss chard", "greens", 19, 1.8, 3.7, 1.6, 1.1, 0.2, 36, None, None, False, []),
    ("arugula", "Arugula", "greens", 25, 2.6, 3.7, 1.6, 2.1, 0.7, 20, None, None, False, ["rocket"]),
    ("mint", "Fresh mint", "flavor", 70, 3.8, 14.9, 8.0, 0.0, 0.9, 32, None, None, False, []),
    ("basil", "Fresh basil", "flavor", 23, 3.2, 2.6, 1.6, 0.3, 0.6, 24, None, None, False, []),
    ("cilantro", "Cilantro", "flavor", 23, 2.1, 3.7, 2.8, 0.9, 0.5, 16, None, None, False, ["coriander"]),
    ("parsley", "Parsley", "flavor", 36, 3.0, 6.3, 3.3, 0.9, 0.8, 60, None, None, False, []),
    ("celery", "Celery", "vegetable", 16, 0.7, 3.0, 1.6, 1.3, 0.2, 101, 40, "stalk", False, []),
    ("cucumber", "Cucumber", "vegetable", 15, 0.7, 3.6, 0.5, 1.7, 0.1, 119, 300, "cucumber", False, []),
    ("carrot", "Carrot", "vegetable", 41, 0.9, 9.6, 2.8, 4.7, 0.2, 128, 61, "medium carrot", False, []),
    ("beet", "Cooked beets", "vegetable", 44, 1.7, 10.0, 2.0, 6.8, 0.2, 136, None, None, False, []),
    ("pumpkin_puree", "Pumpkin puree", "vegetable", 34, 1.1, 8.1, 2.9, 3.3, 0.3, 245, None, None, False, []),
    ("sweet_potato", "Cooked sweet potato", "vegetable", 90, 2.0, 20.7, 3.3, 6.5, 0.2, 200, None, None, False, []),
    ("zucchini", "Zucchini", "vegetable", 17, 1.2, 3.1, 1.0, 2.5, 0.3, 124, None, None, False, ["courgette"]),
    ("cauliflower_frozen", "Frozen riced cauliflower", "frozen", 25, 1.9, 5.0, 2.0, 1.9, 0.3, 107, None, None, False, []),
    ("tomato", "Tomato", "vegetable", 18, 0.9, 3.9, 1.2, 2.6, 0.2, 180, 123, "medium tomato", False, []),
    ("bell_pepper", "Red bell pepper", "vegetable", 31, 1.0, 6.0, 2.1, 4.2, 0.3, 149, 119, "pepper", False, []),
    ("jalapeno", "Jalapeño", "vegetable", 29, 0.9, 6.5, 2.8, 4.1, 0.4, 90, 14, "pepper", False, []),
    ("ginger", "Fresh ginger", "flavor", 80, 1.8, 17.8, 2.0, 1.7, 0.8, 96, None, None, False, []),
    ("garlic", "Garlic", "flavor", 149, 6.4, 33.1, 2.1, 1.0, 0.5, 136, 3, "clove", False, []),
    ("peas_frozen", "Frozen peas", "frozen", 81, 5.4, 14.5, 5.1, 5.7, 0.4, 134, None, None, False, []),

    # ---- liquids ----
    ("water", "Water", "liquid", 0, 0, 0, 0, 0, 0, 236, None, None, True, []),
    ("ice", "Ice", "frozen", 0, 0, 0, 0, 0, 0, 120, None, None, False, ["ice cubes"]),
    ("milk_whole", "Whole milk", "liquid", 61, 3.2, 4.8, 0, 5.1, 3.3, 244, None, None, True, []),
    ("milk_2", "2% milk", "liquid", 50, 3.3, 4.9, 0, 5.0, 2.0, 244, None, None, True, []),
    ("milk_skim", "Skim milk", "liquid", 34, 3.4, 5.0, 0, 5.0, 0.2, 245, None, None, True, []),
    ("almond_milk", "Unsweetened almond milk", "liquid", 15, 0.6, 0.6, 0.3, 0, 1.2, 240, None, None, True, []),
    ("almond_milk_vanilla", "Vanilla almond milk", "liquid", 38, 0.4, 6.3, 0.3, 6.0, 1.1, 240, None, None, True, []),
    ("oat_milk", "Oat milk", "liquid", 48, 1.3, 7.0, 0.8, 3.5, 1.5, 240, None, None, True, []),
    ("soy_milk", "Unsweetened soy milk", "liquid", 33, 3.3, 1.8, 0.6, 0.9, 1.8, 243, None, None, True, []),
    ("coconut_milk_bev", "Coconut milk beverage", "liquid", 20, 0.2, 1.0, 0, 1.0, 1.8, 240, None, None, True, []),
    ("coconut_milk_canned", "Canned coconut milk", "liquid", 197, 2.0, 2.8, 0, 1.6, 21.3, 240, None, None, True, []),
    ("coconut_cream", "Coconut cream", "liquid", 330, 3.6, 6.7, 2.2, 4.9, 34.7, 240, None, None, True, []),
    ("cashew_milk", "Unsweetened cashew milk", "liquid", 10, 0.4, 1.0, 0, 0, 0.9, 240, None, None, True, []),
    ("rice_milk", "Rice milk", "liquid", 47, 0.3, 9.2, 0.3, 5.3, 1.0, 240, None, None, True, []),
    ("kefir", "Plain kefir", "liquid", 41, 3.8, 4.6, 0, 4.6, 1.0, 243, None, None, True, []),
    ("orange_juice", "Orange juice", "liquid", 45, 0.7, 10.4, 0.2, 8.4, 0.2, 248, None, None, True, []),
    ("apple_juice", "Apple juice", "liquid", 46, 0.1, 11.3, 0.2, 9.6, 0.1, 248, None, None, True, []),
    ("carrot_juice", "Carrot juice", "liquid", 40, 0.9, 9.3, 0.8, 3.9, 0.2, 236, None, None, True, []),
    ("pomegranate_juice", "Pomegranate juice", "liquid", 54, 0.2, 13.1, 0.1, 12.7, 0.3, 249, None, None, True, []),
    ("cranberry_juice", "Cranberry juice", "liquid", 46, 0.4, 12.0, 0.1, 12.0, 0.1, 253, None, None, True, []),
    ("cherry_juice", "Tart cherry juice", "liquid", 50, 0.3, 12.4, 0, 11.0, 0.1, 248, None, None, True, []),
    ("pineapple_juice", "Pineapple juice", "liquid", 53, 0.4, 12.9, 0.2, 9.9, 0.1, 250, None, None, True, []),
    ("lemon_juice", "Lemon juice", "liquid", 22, 0.4, 6.9, 0.3, 2.5, 0.2, 244, None, None, True, []),
    ("lime_juice", "Lime juice", "liquid", 25, 0.4, 8.4, 0.4, 1.7, 0.1, 242, None, None, True, []),
    ("coconut_water", "Coconut water", "liquid", 19, 0.7, 3.7, 1.1, 2.6, 0.2, 240, None, None, True, []),
    ("coffee", "Brewed coffee", "liquid", 1, 0.1, 0, 0, 0, 0, 237, None, None, True, []),
    ("cold_brew", "Cold brew concentrate", "liquid", 8, 0.3, 1.4, 0, 0, 0, 237, None, None, True, []),
    ("espresso", "Espresso", "liquid", 9, 0.1, 1.7, 0, 0, 0.2, 237, 30, "shot", True, []),
    ("green_tea", "Brewed green tea", "liquid", 1, 0, 0, 0, 0, 0, 237, None, None, True, []),
    ("chai_concentrate", "Chai concentrate", "liquid", 60, 1.0, 13.0, 0, 12.0, 0.5, 240, None, None, True, []),
    ("kombucha", "Kombucha", "liquid", 30, 0, 7.0, 0, 6.0, 0, 240, None, None, True, []),
    ("limeade_frozen", "Frozen limeade concentrate", "liquid", 128, 0.1, 34.0, 0.3, 31.0, 0.1, 246, None, None, True, ["lime cocktail mixer"]),
    ("lemonade_frozen", "Frozen lemonade concentrate", "liquid", 128, 0.2, 33.5, 0.3, 31.0, 0.1, 246, None, None, True, []),

    # ---- dairy ----
    ("greek_yogurt_nonfat", "Nonfat Greek yogurt", "dairy", 59, 10.2, 3.6, 0, 3.2, 0.4, 245, None, None, False, []),
    ("greek_yogurt_whole", "Whole-milk Greek yogurt", "dairy", 97, 9.0, 3.9, 0, 3.6, 5.0, 245, None, None, False, []),
    ("yogurt_plain", "Plain whole-milk yogurt", "dairy", 61, 3.5, 4.7, 0, 4.7, 3.3, 245, None, None, False, []),
    ("yogurt_vanilla", "Vanilla whole-milk yogurt", "dairy", 96, 3.5, 15.7, 0, 15.6, 2.6, 245, None, None, False, []),
    ("skyr", "Skyr", "dairy", 63, 11.0, 4.0, 0, 4.0, 0.2, 245, None, None, False, []),
    ("cottage_cheese", "Cottage cheese", "dairy", 98, 11.1, 3.4, 0, 2.7, 4.3, 226, None, None, False, []),
    ("cream_cheese", "Cream cheese", "dairy", 350, 6.2, 5.5, 0, 3.2, 34.4, 232, None, None, False, []),
    ("sour_cream", "Sour cream", "dairy", 198, 2.4, 4.6, 0, 3.5, 19.4, 230, None, None, False, []),
    ("heavy_cream", "Heavy cream", "dairy", 340, 2.8, 2.8, 0, 2.9, 36.0, 238, None, None, True, []),
    ("half_and_half", "Half and half", "dairy", 130, 3.0, 4.3, 0, 4.3, 11.5, 242, None, None, True, []),
    ("condensed_milk", "Sweetened condensed milk", "dairy", 321, 7.9, 54.4, 0, 54.4, 8.7, 306, None, None, True, []),
    ("feta", "Feta cheese", "dairy", 264, 14.2, 4.1, 0, 4.1, 21.3, 150, None, None, False, []),
    ("ice_cream", "Vanilla ice cream", "dairy", 207, 3.5, 23.6, 0.7, 21.2, 11.0, 132, None, None, False, []),
    ("frozen_yogurt", "Frozen yogurt", "dairy", 159, 4.0, 24.2, 0, 24.0, 4.0, 174, None, None, False, []),
    ("whipped_cream", "Whipped cream", "dairy", 257, 3.2, 12.5, 0, 12.5, 22.2, 60, None, None, False, []),

    # ---- protein & supplements ----
    ("whey_vanilla", "Vanilla whey protein", "protein", 400, 80.0, 10.0, 1.0, 4.0, 4.0, None, 30, "scoop", False, []),
    ("whey_chocolate", "Chocolate whey protein", "protein", 390, 75.0, 12.0, 2.0, 5.0, 5.0, None, 32, "scoop", False, []),
    ("whey_unflavored", "Unflavored whey protein", "protein", 400, 82.0, 8.0, 0.5, 2.0, 4.0, None, 30, "scoop", False, []),
    ("plant_protein", "Plant protein powder", "protein", 380, 70.0, 12.0, 6.0, 2.0, 6.0, None, 33, "scoop", False, []),
    ("collagen", "Collagen peptides", "protein", 360, 90.0, 0, 0, 0, 0, None, 20, "scoop", False, []),
    ("casein", "Casein protein", "protein", 370, 75.0, 9.0, 1.0, 3.0, 3.0, None, 33, "scoop", False, []),
    ("egg_white", "Pasteurized egg whites", "protein", 52, 10.9, 0.7, 0, 0.7, 0.2, 243, None, None, True, []),
    ("silken_tofu", "Silken tofu", "protein", 55, 5.7, 1.9, 0.2, 0.6, 2.7, 248, None, None, False, []),
    ("peanut_powder", "Powdered peanut butter", "protein", 400, 50.0, 30.0, 15.0, 10.0, 11.0, 90, None, None, False, ["pb2"]),

    # ---- nuts, seeds, butters ----
    ("peanut_butter", "Peanut butter", "nutSeed", 588, 25.0, 20.0, 6.0, 9.0, 50.0, 258, None, None, False, ["pb"]),
    ("almond_butter", "Almond butter", "nutSeed", 614, 21.0, 18.8, 10.3, 4.4, 55.5, 256, None, None, False, []),
    ("cashew_butter", "Cashew butter", "nutSeed", 587, 17.6, 27.6, 2.0, 5.0, 49.4, 256, None, None, False, []),
    ("sunflower_butter", "Sunflower seed butter", "nutSeed", 617, 17.3, 23.3, 5.6, 10.0, 55.2, 256, None, None, False, []),
    ("tahini", "Tahini", "nutSeed", 595, 17.0, 21.2, 9.3, 0.5, 53.8, 240, None, None, False, []),
    ("choc_hazelnut", "Chocolate hazelnut spread", "sweetener", 539, 6.3, 57.9, 5.4, 52.4, 30.9, 300, None, None, False, ["nutella"]),
    ("almonds", "Almonds", "nutSeed", 579, 21.2, 21.6, 12.5, 4.4, 49.9, 143, None, None, False, []),
    ("walnuts", "Walnuts", "nutSeed", 654, 15.2, 13.7, 6.7, 2.6, 65.2, 117, None, None, False, []),
    ("cashews", "Cashews", "nutSeed", 553, 18.2, 30.2, 3.3, 5.9, 43.8, 137, None, None, False, []),
    ("pecans", "Pecans", "nutSeed", 691, 9.2, 13.9, 9.6, 4.0, 72.0, 109, None, None, False, []),
    ("pistachios", "Pistachios", "nutSeed", 560, 20.2, 27.2, 10.6, 7.7, 45.3, 123, None, None, False, []),
    ("hemp_hearts", "Hemp hearts", "nutSeed", 553, 31.6, 8.7, 4.0, 1.5, 48.8, 160, None, None, False, []),
    ("chia", "Chia seeds", "nutSeed", 486, 16.5, 42.1, 34.4, 0, 30.7, 192, None, None, False, []),
    ("flax", "Ground flaxseed", "nutSeed", 534, 18.3, 28.9, 27.3, 1.6, 42.2, 112, None, None, False, ["linseed"]),
    ("pumpkin_seeds", "Pumpkin seeds", "nutSeed", 559, 30.2, 10.7, 6.0, 1.4, 49.0, 129, None, None, False, ["pepitas"]),
    ("sunflower_seeds", "Sunflower seeds", "nutSeed", 584, 20.8, 20.0, 8.6, 2.6, 51.5, 140, None, None, False, []),

    # ---- grains ----
    ("oats", "Rolled oats", "grain", 389, 16.9, 66.3, 10.6, 0, 6.9, 81, None, None, False, ["quick oats"]),
    ("oat_bran", "Oat bran", "grain", 246, 17.3, 66.2, 15.4, 1.4, 7.0, 94, None, None, False, []),
    ("granola", "Granola", "grain", 471, 10.0, 64.0, 7.0, 25.0, 20.0, 122, None, None, False, []),
    ("wheat_germ", "Wheat germ", "grain", 360, 23.0, 51.8, 13.2, 0, 9.7, 115, None, None, False, []),
    ("psyllium", "Psyllium husk", "grain", 200, 2.0, 80.0, 78.0, 0, 0, 96, None, None, False, []),
    ("graham_cracker", "Graham crackers", "grain", 423, 7.0, 77.0, 2.8, 25.0, 10.0, 85, 14, "sheet", False, []),
    ("choc_cookie", "Chocolate sandwich cookies", "grain", 471, 5.0, 71.0, 3.0, 38.0, 20.0, 120, 11, "cookie", False, ["oreo"]),

    # ---- powders & flavor ----
    ("cacao_powder", "Unsweetened cacao powder", "flavor", 228, 19.6, 57.9, 37.0, 1.8, 13.7, 86, None, None, False, ["cocoa powder"]),
    ("cacao_nibs", "Cacao nibs", "flavor", 650, 14.0, 36.0, 33.0, 1.0, 52.0, 120, None, None, False, []),
    ("matcha", "Matcha powder", "flavor", 324, 29.0, 39.0, 38.0, 0, 5.3, 96, None, None, False, []),
    ("spirulina", "Spirulina powder", "flavor", 290, 57.0, 23.9, 3.6, 3.1, 7.7, 112, None, None, False, []),
    ("maca", "Maca powder", "flavor", 325, 14.5, 71.4, 7.4, 31.0, 1.2, 128, None, None, False, []),
    ("instant_coffee", "Instant coffee", "flavor", 353, 12.2, 41.1, 0, 0, 0.5, 58, None, None, False, []),
    ("cinnamon", "Ground cinnamon", "flavor", 247, 4.0, 80.6, 53.1, 2.2, 1.2, 124, None, None, False, []),
    ("nutmeg", "Ground nutmeg", "flavor", 525, 5.8, 49.3, 20.8, 28.5, 36.3, 110, None, None, False, []),
    ("turmeric", "Ground turmeric", "flavor", 312, 9.7, 67.1, 22.7, 3.2, 3.3, 144, None, None, False, []),
    ("vanilla_extract", "Vanilla extract", "flavor", 288, 0.1, 12.7, 0, 12.7, 0.1, 208, None, None, True, []),
    ("salt", "Kosher salt", "flavor", 0, 0, 0, 0, 0, 0, 288, None, None, False, ["sea salt"]),
    ("espresso_powder", "Espresso powder", "flavor", 353, 12.2, 41.1, 0, 0, 0.5, 58, None, None, False, []),

    # ---- sweeteners & fats ----
    ("honey", "Honey", "sweetener", 304, 0.3, 82.4, 0.2, 82.1, 0, 339, None, None, True, []),
    ("maple_syrup", "Maple syrup", "sweetener", 260, 0, 67.0, 0, 60.5, 0.1, 322, None, None, True, []),
    ("agave", "Agave syrup", "sweetener", 310, 0.1, 76.0, 0.2, 68.0, 0.5, 336, None, None, True, []),
    ("sugar", "Granulated sugar", "sweetener", 387, 0, 100.0, 0, 100.0, 0, 200, None, None, False, []),
    ("brown_sugar", "Brown sugar", "sweetener", 380, 0, 98.0, 0, 97.0, 0, 220, None, None, False, []),
    ("chocolate_syrup", "Chocolate syrup", "sweetener", 279, 2.1, 65.0, 2.6, 49.5, 1.1, 300, None, None, True, []),
    ("caramel_sauce", "Caramel sauce", "sweetener", 310, 1.0, 68.0, 0, 55.0, 4.0, 310, None, None, True, []),
    ("stevia", "Stevia", "sweetener", 0, 0, 0, 0, 0, 0, 200, None, None, False, ["monk fruit"]),
    ("cumin", "Ground cumin", "flavor", 375, 17.8, 44.2, 10.5, 2.3, 22.3, 100, None, None, False, []),
    ("black_pepper", "Ground black pepper", "flavor", 251, 10.4, 63.9, 25.3, 0.6, 3.3, 115, None, None, False, []),
    ("dijon", "Dijon mustard", "flavor", 66, 4.4, 5.8, 3.3, 1.1, 3.3, 249, None, None, False, []),
    ("cider_vinegar", "Apple cider vinegar", "liquid", 21, 0, 0.9, 0, 0.4, 0, 239, None, None, True, []),
    ("olive_oil", "Olive oil", "other", 884, 0, 0, 0, 0, 100.0, 216, None, None, True, []),
    ("coconut_oil", "Coconut oil", "other", 892, 0, 0, 0, 0, 99.0, 218, None, None, False, []),
    ("mct_oil", "MCT oil", "other", 830, 0, 0, 0, 0, 100.0, 216, None, None, True, []),
    ("mayonnaise", "Mayonnaise", "other", 680, 1.0, 0.6, 0, 0.6, 75.0, 224, None, None, False, []),

    # ---- alcohol ----
    ("tequila", "Tequila", "alcohol", 231, 0, 0, 0, 0, 0, 236, 42, "shot", True, []),
    ("vodka", "Vodka", "alcohol", 231, 0, 0, 0, 0, 0, 236, 42, "shot", True, []),
    ("white_rum", "White rum", "alcohol", 231, 0, 0, 0, 0, 0, 236, 42, "shot", True, []),
    ("triple_sec", "Triple sec", "alcohol", 250, 0, 25.0, 0, 25.0, 0, 236, None, None, True, []),
    ("coffee_liqueur", "Coffee liqueur", "alcohol", 336, 0, 46.0, 0, 46.0, 0.3, 236, None, None, True, []),
    ("white_wine", "White wine", "alcohol", 82, 0.1, 2.6, 0, 1.0, 0, 236, None, None, True, []),
    ("prosecco", "Prosecco", "alcohol", 80, 0.1, 2.0, 0, 1.0, 0, 236, None, None, True, []),
]

CATEGORY_ORDER = [
    "fruit", "frozen", "greens", "vegetable", "liquid", "dairy",
    "protein", "nutSeed", "grain", "flavor", "sweetener", "alcohol", "other",
]

CUP_ML = 236.588

# Dietary flags. Everything in the "dairy" category is animal + dairy by
# default; these sets cover the cases category alone gets wrong. Recipe tags
# are derived from these, never hand-written, so filters can't drift.
ANIMAL = {
    "honey", "egg_white", "whey_vanilla", "whey_chocolate", "whey_unflavored",
    "collagen", "casein", "kefir", "mayonnaise",
}
DAIRY = {
    "whey_vanilla", "whey_chocolate", "whey_unflavored", "casein", "kefir",
    "milk_whole", "milk_2", "milk_skim",
}
NUTS = {
    "almonds", "almond_butter", "almond_milk", "almond_milk_vanilla",
    "cashews", "cashew_butter", "cashew_milk", "walnuts", "pecans",
    "pistachios", "peanut_butter", "peanuts", "peanut_powder",
    "choc_hazelnut", "coconut_shredded", "coconut_milk_bev",
    "coconut_milk_canned", "coconut_cream", "coconut_water", "coconut_oil",
}
CAFFEINE = {
    "coffee", "cold_brew", "espresso", "espresso_powder", "instant_coffee",
    "green_tea", "matcha", "chai_concentrate", "coffee_liqueur",
}
GLUTEN = {"wheat_germ", "graham_cracker", "choc_cookie", "granola"}


def flags(fid, cat):
    return {
        "isAnimal": cat == "dairy" or fid in ANIMAL,
        "isDairy": cat == "dairy" or fid in DAIRY,
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


def build_recipes(foods_by_id):
    import recipes_data

    out = []
    seen = set()
    for category, attr in RECIPE_GROUPS:
        for rid, name, servings, prep, ingredients, tip in getattr(recipes_data, attr):
            assert rid not in seen, f"duplicate recipe id {rid}"
            seen.add(rid)
            for fid, amount, unit in ingredients:
                assert fid in foods_by_id, f"{rid}: unknown ingredient {fid}"
                assert unit in ("gram", "milliliter", "cup", "tbsp", "tsp", "piece"), \
                    f"{rid}: bad unit {unit}"
                assert amount > 0, f"{rid}: non-positive amount for {fid}"
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
