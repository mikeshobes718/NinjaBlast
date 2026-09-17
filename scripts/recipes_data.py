"""Blast recipe library.

Each entry: (id, name, category, program, servings, prep_minutes, ingredients, tip)
ingredients: list of (food_id, amount, unit)

Directions are not stored per recipe. Like the printed Ninja inserts, every
blend follows the same sequence, so the app generates the steps from the
selected device and the program. Only the box-insert recipes quote fixed
wording, and those live in Swift alongside their scans.
"""

# ---------------------------------------------------------------- smoothies
SMOOTHIES = [
    ("triple-berry-blast", "Triple Berry Blast", 1, 3, [
        ("oat_milk", 0.75, "cup"), ("berries_mixed_frozen", 0.75, "cup"),
        ("banana", 0.5, "piece"), ("honey", 1, "tsp")], None),
    ("strawberry-banana", "Strawberry Banana Classic", 1, 3, [
        ("milk_2", 0.75, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("banana", 0.5, "piece"), ("vanilla_extract", 0.5, "tsp")], None),
    ("mango-lassi", "Mango Lassi", 1, 4, [
        ("yogurt_plain", 0.5, "cup"), ("mango_frozen", 0.75, "cup"),
        ("milk_whole", 0.5, "cup"), ("honey", 1, "tsp")], "Skip the honey if the mango is very ripe."),
    ("peach-melba", "Peach Melba", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("peach_frozen", 0.75, "cup"),
        ("raspberry", 0.25, "cup"), ("maple_syrup", 1, "tsp")], None),
    ("pina-colada-smoothie", "Pineapple Coconut Cooler", 1, 3, [
        ("coconut_water", 0.75, "cup"), ("pineapple_frozen", 1, "cup"),
        ("lime_juice", 1, "tbsp")], None),
    ("blueberry-muffin", "Blueberry Muffin Smoothie", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("oats", 2, "tbsp"), ("cinnamon", 0.25, "tsp"), ("maple_syrup", 2, "tsp")], None),
    ("cherry-almond", "Cherry Almond", 1, 3, [
        ("almond_milk", 0.75, "cup"), ("cherry_frozen", 0.75, "cup"),
        ("almond_butter", 1, "tbsp"), ("vanilla_extract", 0.5, "tsp")], None),
    ("watermelon-cooler", "Watermelon Mint Cooler", 1, 3, [
        ("watermelon", 1.5, "cup"), ("lime_juice", 1, "tbsp"),
        ("mint", 3, "gram"), ("ice", 0.5, "cup")], None),
    ("tropical-sunrise", "Tropical Sunrise", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("mango_frozen", 0.5, "cup"),
        ("pineapple_frozen", 0.5, "cup")], None),
    ("raspberry-lemonade-smoothie", "Raspberry Lemonade Smoothie", 1, 3, [
        ("water", 0.5, "cup"), ("lemonade_frozen", 0.25, "cup"),
        ("raspberry", 0.75, "cup"), ("ice", 0.5, "cup")], None),
    ("strawberry-cheesecake", "Strawberry Cheesecake Smoothie", 1, 4, [
        ("milk_whole", 0.5, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("cream_cheese", 2, "tbsp"), ("graham_cracker", 1, "piece"),
        ("honey", 1, "tsp")], None),
    ("blackberry-sage", "Blackberry Vanilla", 1, 3, [
        ("almond_milk_vanilla", 0.75, "cup"), ("blackberry", 0.75, "cup"),
        ("greek_yogurt_nonfat", 0.25, "cup")], None),
    ("papaya-lime", "Papaya Lime", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("papaya", 1, "cup"),
        ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("dragonfruit-cooler", "Dragon Fruit Cooler", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("dragonfruit", 0.75, "cup"),
        ("pineapple_frozen", 0.5, "cup"), ("lime_juice", 2, "tsp")], None),
    ("pear-ginger", "Pear Ginger Fizz", 1, 4, [
        ("kombucha", 0.5, "cup"), ("pear", 1, "piece"),
        ("ginger", 3, "gram"), ("ice", 0.5, "cup")], None),
    ("grape-escape", "Purple Grape Escape", 1, 3, [
        ("apple_juice", 0.5, "cup"), ("grapes", 1, "cup"),
        ("blueberry_frozen", 0.5, "cup")], None),
    ("kiwi-crush", "Kiwi Crush", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("kiwi", 2, "piece"),
        ("banana_frozen", 0.5, "cup"), ("lime_juice", 2, "tsp")], None),
    ("acai-bowl-drink", "Acai Berry Blend", 1, 4, [
        ("almond_milk", 0.5, "cup"), ("acai_puree", 1, "piece"),
        ("banana_frozen", 0.5, "cup"), ("blueberry_frozen", 0.5, "cup")], "Use less milk and eat it with a spoon for a bowl."),
    ("orange-creamsicle", "Orange Creamsicle", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("yogurt_vanilla", 0.5, "cup"),
        ("ice", 0.75, "cup"), ("vanilla_extract", 0.5, "tsp")], None),
    ("fig-honey", "Fig and Honey", 1, 4, [
        ("milk_whole", 0.75, "cup"), ("fig", 3, "piece"),
        ("greek_yogurt_whole", 0.25, "cup"), ("honey", 2, "tsp")], None),
    ("apricot-orange", "Apricot Orange", 1, 4, [
        ("orange_juice", 0.75, "cup"), ("apricot_dried", 6, "piece"),
        ("greek_yogurt_nonfat", 0.25, "cup"), ("ice", 0.5, "cup")], "Soak the apricots in warm water for five minutes if they are very dry."),
    ("pomegranate-berry", "Pomegranate Berry", 1, 3, [
        ("pomegranate_juice", 0.75, "cup"), ("berries_mixed_frozen", 0.75, "cup"),
        ("lemon_juice", 2, "tsp")], None),
    ("cantaloupe-cream", "Cantaloupe Cream", 1, 3, [
        ("milk_2", 0.5, "cup"), ("cantaloupe", 1.25, "cup"),
        ("ice", 0.5, "cup"), ("honey", 1, "tsp")], None),
    ("honeydew-cucumber", "Honeydew Cucumber", 1, 4, [
        ("water", 0.5, "cup"), ("honeydew", 1.25, "cup"),
        ("cucumber", 0.5, "cup"), ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("guava-paradise", "Guava Paradise", 1, 4, [
        ("pineapple_juice", 0.75, "cup"), ("guava", 1, "piece"),
        ("banana_frozen", 0.5, "cup")], None),
    ("passionfruit-pineapple", "Passion Fruit Pineapple", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("passionfruit", 2, "piece"),
        ("pineapple_frozen", 0.75, "cup")], None),
    ("plum-perfect", "Prune and Pear", 1, 4, [
        ("apple_juice", 0.75, "cup"), ("prune", 4, "piece"),
        ("pear", 0.5, "piece"), ("ice", 0.5, "cup")], None),
    ("very-cherry-vanilla", "Very Cherry Vanilla", 1, 3, [
        ("almond_milk_vanilla", 0.75, "cup"), ("cherry_frozen", 1, "cup"),
        ("vanilla_extract", 0.5, "tsp")], None),
    ("banana-date-shake", "Banana Date Shake", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("banana_frozen", 0.75, "cup"),
        ("date", 2, "piece"), ("cinnamon", 0.25, "tsp")], None),
    ("mixed-melon", "Mixed Melon", 1, 4, [
        ("coconut_water", 0.5, "cup"), ("watermelon", 0.75, "cup"),
        ("honeydew", 0.75, "cup"), ("ice", 0.5, "cup")], None),
    ("strawberry-basil", "Strawberry Basil", 1, 4, [
        ("water", 0.5, "cup"), ("strawberry_frozen", 1, "cup"),
        ("basil", 3, "gram"), ("honey", 2, "tsp"), ("lemon_juice", 2, "tsp")], None),
    ("blueberry-lemon", "Blueberry Lemon", 1, 3, [
        ("oat_milk", 0.75, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"), ("maple_syrup", 2, "tsp")], None),
    ("raspberry-peach", "Raspberry Peach", 1, 3, [
        ("almond_milk", 0.75, "cup"), ("peach_frozen", 0.5, "cup"),
        ("raspberry", 0.5, "cup")], None),
    ("apple-pie-smoothie", "Apple Pie Smoothie", 1, 4, [
        ("milk_2", 0.75, "cup"), ("applesauce", 0.5, "cup"),
        ("oats", 2, "tbsp"), ("cinnamon", 0.5, "tsp"), ("maple_syrup", 2, "tsp"),
        ("ice", 0.5, "cup")], None),
    ("pina-mango", "Pina Mango", 1, 3, [
        ("coconut_milk_bev", 0.75, "cup"), ("pineapple_frozen", 0.5, "cup"),
        ("mango_frozen", 0.5, "cup")], None),
    ("grapefruit-sunrise", "Grapefruit Sunrise", 1, 4, [
        ("orange_juice", 0.5, "cup"), ("grapefruit", 0.5, "piece"),
        ("strawberry_frozen", 0.5, "cup"), ("honey", 2, "tsp")], None),
    ("coconut-cream-pie", "Coconut Cream Pie", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"), ("banana_frozen", 0.75, "cup"),
        ("coconut_shredded", 2, "tbsp"), ("graham_cracker", 1, "piece")], None),
    ("mixed-berry-yogurt", "Mixed Berry Yogurt Smoothie", 1, 3, [
        ("milk_2", 0.5, "cup"), ("greek_yogurt_nonfat", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("cranberry-orange", "Cranberry Orange", 1, 4, [
        ("orange_juice", 0.75, "cup"), ("cranberry_frozen", 0.5, "cup"),
        ("banana", 0.5, "piece"), ("maple_syrup", 2, "tsp")], None),
    ("tart-cherry-berry", "Tart Cherry Berry", 1, 3, [
        ("cherry_juice", 0.75, "cup"), ("berries_mixed_frozen", 0.75, "cup"),
        ("lemon_juice", 1, "tsp")], None),
    ("peaches-and-cream", "Peaches and Cream", 1, 3, [
        ("milk_whole", 0.5, "cup"), ("peach_frozen", 1, "cup"),
        ("yogurt_vanilla", 0.25, "cup")], None),
    ("strawberry-kiwi", "Strawberry Kiwi", 1, 4, [
        ("apple_juice", 0.5, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("kiwi", 1, "piece"), ("ice", 0.25, "cup")], None),
    ("mango-chili", "Mango Chili Cooler", 1, 4, [
        ("water", 0.5, "cup"), ("mango_frozen", 1, "cup"),
        ("lime_juice", 1, "tbsp"), ("jalapeno", 0.25, "piece"), ("honey", 1, "tsp")], "Start with a sliver of jalapeño, taste, then add more."),
    ("berry-beet-blend", "Berry Beet Blend", 1, 4, [
        ("apple_juice", 0.75, "cup"), ("beet", 0.33, "cup"),
        ("berries_mixed_frozen", 0.75, "cup")], None),
    ("pineapple-basil", "Pineapple Basil", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("pineapple_frozen", 0.75, "cup"),
        ("basil", 3, "gram"), ("lime_juice", 2, "tsp")], None),
    ("blood-orange-berry", "Orange Berry Swirl", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("strawberry_frozen", 0.5, "cup"),
        ("raspberry", 0.25, "cup")], None),
    ("banana-bread-smoothie", "Banana Bread Smoothie", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("banana_frozen", 0.75, "cup"),
        ("walnuts", 1, "tbsp"), ("oats", 2, "tbsp"), ("cinnamon", 0.25, "tsp")], None),
    ("blueberry-cobbler", "Blueberry Cobbler", 1, 4, [
        ("milk_2", 0.75, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("granola", 2, "tbsp"), ("maple_syrup", 2, "tsp")], None),
    ("raspberry-rose", "Raspberry Cream", 1, 3, [
        ("milk_whole", 0.5, "cup"), ("raspberry", 1, "cup"),
        ("greek_yogurt_whole", 0.25, "cup"), ("honey", 2, "tsp")], None),
    ("mango-turmeric", "Mango Turmeric", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"), ("mango_frozen", 0.75, "cup"),
        ("turmeric", 0.25, "tsp"), ("black_pepper", 0.05, "tsp"),
        ("honey", 1, "tsp")], "The pinch of black pepper is what makes turmeric absorbable."),
    ("strawberry-rhubarb", "Strawberry Orange Crush", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("strawberry_frozen", 1, "cup"),
        ("honey", 1, "tsp")], None),
    ("tropical-greens-lite", "Tropical Cooler", 1, 3, [
        ("pineapple_juice", 0.75, "cup"), ("mango_frozen", 0.75, "cup"),
        ("lime_juice", 2, "tsp")], None),
    ("cherry-cola-smoothie", "Cherry Vanilla Cream", 1, 4, [
        ("milk_2", 0.5, "cup"), ("cherry_frozen", 0.75, "cup"),
        ("yogurt_vanilla", 0.25, "cup"), ("vanilla_extract", 0.5, "tsp")], None),
    ("apple-berry", "Apple Berry", 1, 3, [
        ("apple_juice", 0.75, "cup"), ("apple", 0.5, "piece"),
        ("berries_mixed_frozen", 0.5, "cup")], None),
    ("pomegranate-cherry", "Pomegranate Cherry", 1, 3, [
        ("pomegranate_juice", 0.75, "cup"), ("cherry_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tsp")], None),
]

# ------------------------------------------------------------------- greens
GREENS = [
    ("classic-green", "Classic Green", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("spinach", 1, "cup"),
        ("banana_frozen", 0.5, "cup"), ("mango_frozen", 0.5, "cup")], None),
    ("kale-pineapple", "Kale Pineapple", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("kale", 0.75, "cup"),
        ("pineapple_frozen", 0.75, "cup"), ("lemon_juice", 2, "tsp")], None),
    ("green-machine", "Green Machine", 1, 5, [
        ("water", 0.75, "cup"), ("spinach", 1, "cup"), ("celery", 1, "piece"),
        ("apple_green", 0.5, "piece"), ("lemon_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("avocado-greens", "Avocado Green Cream", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("spinach", 1, "cup"),
        ("avocado", 0.5, "piece"), ("banana_frozen", 0.5, "cup"),
        ("honey", 1, "tsp")], None),
    ("cucumber-mint-green", "Cucumber Mint Green", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("cucumber", 0.75, "cup"),
        ("spinach", 1, "cup"), ("mint", 3, "gram"), ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup")], None),
    ("green-protein", "Green Protein", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("spinach", 1, "cup"),
        ("whey_vanilla", 1, "piece"), ("banana_frozen", 0.5, "cup")], None),
    ("matcha-greens", "Matcha Greens", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("matcha", 1, "tsp"),
        ("spinach", 0.75, "cup"), ("banana_frozen", 0.5, "cup"),
        ("honey", 1, "tsp")], None),
    ("kale-apple-ginger", "Kale Apple Ginger", 1, 5, [
        ("water", 0.75, "cup"), ("kale", 0.75, "cup"), ("apple_green", 1, "piece"),
        ("ginger", 4, "gram"), ("lemon_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("spinach-peanut-butter", "Green Peanut Butter Cup", 1, 4, [
        ("milk_2", 0.75, "cup"), ("spinach", 1, "cup"),
        ("peanut_butter", 1, "tbsp"), ("banana_frozen", 0.5, "cup"),
        ("cacao_powder", 1, "tsp")], "The cocoa hides the color if greens are a hard sell."),
    ("arugula-pear", "Arugula Pear", 1, 4, [
        ("apple_juice", 0.75, "cup"), ("arugula", 0.75, "cup"),
        ("pear", 1, "piece"), ("lemon_juice", 2, "tsp")], None),
    ("swiss-chard-berry", "Chard Berry", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("chard", 1, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("green-detox", "Green Reset", 1, 5, [
        ("green_tea", 0.75, "cup"), ("spinach", 1, "cup"), ("cucumber", 0.5, "cup"),
        ("apple_green", 0.5, "piece"), ("lemon_juice", 1, "tbsp"),
        ("ginger", 3, "gram"), ("ice", 0.5, "cup")], None),
    ("tropical-green", "Tropical Green", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("kale", 0.5, "cup"),
        ("mango_frozen", 0.5, "cup"), ("pineapple_frozen", 0.5, "cup")], None),
    ("green-goddess", "Green Goddess", 1, 5, [
        ("coconut_water", 0.75, "cup"), ("spinach", 1, "cup"),
        ("avocado", 0.25, "piece"), ("kiwi", 1, "piece"),
        ("lime_juice", 1, "tbsp"), ("mint", 2, "gram")], None),
    ("celery-cucumber-tonic", "Celery Cucumber Tonic", 1, 5, [
        ("water", 0.75, "cup"), ("celery", 2, "piece"), ("cucumber", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"), ("apple_green", 0.5, "piece"), ("ice", 0.5, "cup")], None),
    ("spinach-oat-green", "Green Oat Breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("spinach", 1, "cup"), ("oats", 3, "tbsp"),
        ("banana_frozen", 0.5, "cup"), ("maple_syrup", 2, "tsp")], None),
    ("hemp-green", "Hemp Green", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("spinach", 1, "cup"),
        ("hemp_hearts", 2, "tbsp"), ("pineapple_frozen", 0.5, "cup")], None),
    ("kiwi-spinach", "Kiwi Spinach", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("spinach", 1, "cup"),
        ("kiwi", 2, "piece"), ("banana_frozen", 0.5, "cup")], None),
    ("green-tea-pear", "Green Tea Pear", 1, 4, [
        ("green_tea", 0.75, "cup"), ("pear", 1, "piece"),
        ("spinach", 0.75, "cup"), ("honey", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("zucchini-green", "Zucchini Vanilla Green", 1, 4, [
        ("almond_milk_vanilla", 0.75, "cup"), ("zucchini", 0.5, "cup"),
        ("spinach", 0.75, "cup"), ("banana_frozen", 0.5, "cup"),
        ("cinnamon", 0.25, "tsp")], "Frozen zucchini makes it creamy without tasting like vegetables."),
    ("parsley-lemon-green", "Parsley Lemon Green", 1, 5, [
        ("water", 0.75, "cup"), ("parsley", 0.25, "cup"), ("spinach", 0.75, "cup"),
        ("apple_green", 1, "piece"), ("lemon_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("romaine-melon", "Romaine Melon", 1, 4, [
        ("water", 0.5, "cup"), ("romaine", 1, "cup"), ("honeydew", 1, "cup"),
        ("lime_juice", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("green-chia", "Green Chia", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("spinach", 1, "cup"),
        ("chia", 1, "tbsp"), ("mango_frozen", 0.5, "cup"), ("lime_juice", 2, "tsp")], None),
    ("spirulina-green", "Spirulina Power Green", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("spirulina", 1, "tsp"),
        ("spinach", 0.75, "cup"), ("pineapple_frozen", 0.75, "cup")], None),
    ("broccoli-free-green", "Sweet Green Starter", 1, 3, [
        ("apple_juice", 0.75, "cup"), ("spinach", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"), ("mango_frozen", 0.25, "cup")], "A mild first green smoothie — mostly fruit, one cup of spinach."),
]

# ------------------------------------------------------------------ protein
PROTEIN = [
    ("vanilla-whey-classic", "Vanilla Protein Classic", 1, 3, [
        ("milk_2", 1, "cup"), ("whey_vanilla", 1, "piece"),
        ("banana_frozen", 0.5, "cup")], None),
    ("chocolate-peanut-protein", "Chocolate Peanut Protein", 1, 3, [
        ("milk_2", 0.75, "cup"), ("whey_chocolate", 1, "piece"),
        ("peanut_butter", 1, "tbsp"), ("banana_frozen", 0.5, "cup")], None),
    ("post-workout-cherry", "Tart Cherry Recovery", 1, 3, [
        ("cherry_juice", 0.75, "cup"), ("whey_unflavored", 1, "piece"),
        ("cherry_frozen", 0.5, "cup")], "Tart cherry is a classic post-training choice for sore legs."),
    ("cottage-berry-protein", "Cottage Cheese Berry", 1, 4, [
        ("milk_skim", 0.5, "cup"), ("cottage_cheese", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("skyr-blueberry", "Skyr Blueberry", 1, 3, [
        ("milk_skim", 0.5, "cup"), ("skyr", 0.5, "cup"),
        ("blueberry_frozen", 0.75, "cup"), ("maple_syrup", 1, "tsp")], None),
    ("plant-power-chocolate", "Plant Power Chocolate", 1, 3, [
        ("oat_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("banana_frozen", 0.5, "cup"), ("cacao_powder", 1, "tbsp")], None),
    ("egg-white-vanilla", "Egg White Vanilla Shake", 1, 4, [
        ("milk_skim", 0.5, "cup"), ("egg_white", 0.5, "cup"),
        ("whey_vanilla", 1, "piece"), ("banana_frozen", 0.5, "cup")], "Use pasteurized egg whites only."),
    ("greek-mocha-protein", "Greek Mocha Protein", 1, 3, [
        ("coffee", 0.5, "cup"), ("greek_yogurt_nonfat", 0.5, "cup"),
        ("whey_chocolate", 1, "piece"), ("ice", 0.75, "cup")], None),
    ("mass-gainer", "Big Build Shake", 1, 4, [
        ("milk_whole", 1, "cup"), ("whey_chocolate", 1, "piece"),
        ("oats", 0.25, "cup"), ("peanut_butter", 2, "tbsp"),
        ("banana", 1, "piece")], "High calorie by design — this is the one for a bulking phase."),
    ("lean-vanilla", "Lean Vanilla", 1, 3, [
        ("almond_milk", 1, "cup"), ("whey_vanilla", 1, "piece"),
        ("strawberry_frozen", 0.5, "cup"), ("ice", 0.25, "cup")], None),
    ("collagen-berry", "Collagen Berry", 1, 3, [
        ("coconut_water", 0.75, "cup"), ("collagen", 1, "piece"),
        ("berries_mixed_frozen", 0.75, "cup")], None),
    ("casein-night", "Bedtime Casein", 1, 3, [
        ("milk_2", 1, "cup"), ("casein", 1, "piece"),
        ("almond_butter", 1, "tbsp"), ("cinnamon", 0.25, "tsp")], "Casein digests slowly, which is the point before bed."),
    ("tofu-berry-protein", "Silken Tofu Berry", 1, 4, [
        ("soy_milk", 0.75, "cup"), ("silken_tofu", 0.5, "cup"),
        ("strawberry_frozen", 0.75, "cup"), ("maple_syrup", 2, "tsp")], None),
    ("pb-banana-protein", "PB Banana Protein", 1, 3, [
        ("milk_2", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("peanut_powder", 2, "tbsp"), ("banana_frozen", 0.75, "cup")], None),
    ("mocha-collagen", "Mocha Collagen", 1, 3, [
        ("cold_brew", 0.5, "cup"), ("milk_2", 0.5, "cup"),
        ("collagen", 1, "piece"), ("cacao_powder", 1, "tsp"), ("ice", 0.75, "cup")], None),
    ("strawberry-protein-cream", "Strawberry Protein Cream", 1, 3, [
        ("milk_whole", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("strawberry_frozen", 0.75, "cup"), ("greek_yogurt_nonfat", 0.25, "cup")], None),
    ("green-recovery", "Green Recovery", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("whey_unflavored", 1, "piece"),
        ("spinach", 1, "cup"), ("pineapple_frozen", 0.5, "cup")], None),
    ("chocolate-oat-protein", "Chocolate Oat Protein", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("whey_chocolate", 1, "piece"),
        ("oats", 3, "tbsp"), ("banana_frozen", 0.5, "cup")], None),
    ("pumpkin-protein", "Pumpkin Spice Protein", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("pumpkin_puree", 0.5, "cup"), ("cinnamon", 0.5, "tsp"),
        ("maple_syrup", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("blueberry-protein-oat", "Blueberry Protein Oats", 1, 4, [
        ("milk_2", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("blueberry_frozen", 0.5, "cup"), ("oats", 3, "tbsp")], None),
    ("almond-joy-protein", "Almond Joy Protein", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"), ("whey_chocolate", 1, "piece"),
        ("almond_butter", 1, "tbsp"), ("coconut_shredded", 1, "tbsp"),
        ("ice", 0.5, "cup")], None),
    ("kefir-protein", "Kefir Protein", 1, 3, [
        ("kefir", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("berries_mixed_frozen", 0.5, "cup")], None),
    ("mango-protein", "Mango Protein", 1, 3, [
        ("almond_milk", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("mango_frozen", 0.75, "cup")], None),
    ("espresso-protein", "Espresso Protein", 1, 3, [
        ("espresso", 2, "piece"), ("milk_2", 0.75, "cup"),
        ("whey_chocolate", 1, "piece"), ("ice", 0.75, "cup")], None),
    ("salted-caramel-protein", "Salted Caramel Protein", 1, 3, [
        ("milk_2", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("caramel_sauce", 1, "tbsp"), ("salt", 0.1, "tsp"), ("ice", 0.75, "cup")], None),
    ("chocolate-cherry-protein", "Chocolate Cherry Protein", 1, 3, [
        ("milk_2", 0.75, "cup"), ("whey_chocolate", 1, "piece"),
        ("cherry_frozen", 0.75, "cup")], None),
    ("matcha-protein", "Matcha Protein", 1, 3, [
        ("oat_milk", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("matcha", 1, "tsp"), ("banana_frozen", 0.5, "cup")], None),
    ("high-fiber-protein", "High Fiber Protein", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("chia", 1, "tbsp"), ("flax", 1, "tbsp"), ("raspberry", 0.5, "cup")], None),
    ("apple-cinnamon-protein", "Apple Cinnamon Protein", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("applesauce", 0.5, "cup"), ("cinnamon", 0.5, "tsp"), ("ice", 0.5, "cup")], None),
    ("cookies-cream-protein", "Cookies and Cream Protein", 1, 3, [
        ("milk_2", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("choc_cookie", 2, "piece"), ("ice", 0.5, "cup")], None),
    ("tropical-protein", "Tropical Protein", 1, 3, [
        ("coconut_water", 0.75, "cup"), ("whey_vanilla", 1, "piece"),
        ("mango_frozen", 0.5, "cup"), ("pineapple_frozen", 0.5, "cup")], None),
    ("peanut-mocha-protein", "Peanut Mocha Protein", 1, 3, [
        ("cold_brew", 0.5, "cup"), ("milk_2", 0.5, "cup"),
        ("whey_chocolate", 1, "piece"), ("peanut_powder", 2, "tbsp"),
        ("ice", 0.5, "cup")], None),
    ("greek-vanilla-protein", "Greek Vanilla Protein", 1, 3, [
        ("milk_skim", 0.5, "cup"), ("greek_yogurt_nonfat", 0.5, "cup"),
        ("whey_vanilla", 1, "piece"), ("banana_frozen", 0.5, "cup")], None),
    ("beet-protein", "Beet Performance", 1, 4, [
        ("cherry_juice", 0.5, "cup"), ("beet", 0.5, "cup"),
        ("whey_unflavored", 1, "piece"), ("berries_mixed_frozen", 0.5, "cup")], None),
    ("overnight-protein-oats", "Protein Oat Shake", 1, 4, [
        ("milk_2", 1, "cup"), ("whey_vanilla", 1, "piece"),
        ("oats", 0.25, "cup"), ("cinnamon", 0.25, "tsp")], None),
]

# Plant-based protein. Whey dominates the list above, which left almost
# nothing for a vegan who wants 20 g in the cup.
PROTEIN += [
    ("vegan-chocolate-pb", "Vegan Chocolate PB", 1, 3, [
        ("soy_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("peanut_butter", 1, "tbsp"), ("banana_frozen", 0.5, "cup")], None),
    ("vegan-berry-protein", "Vegan Berry Protein", 1, 3, [
        ("oat_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("berries_mixed_frozen", 0.75, "cup")], None),
    ("vegan-green-protein", "Vegan Green Protein", 1, 4, [
        ("soy_milk", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("spinach", 1, "cup"), ("banana_frozen", 0.5, "cup")], None),
    ("tofu-chocolate-protein", "Tofu Chocolate Protein", 1, 4, [
        ("soy_milk", 0.75, "cup"), ("silken_tofu", 0.5, "cup"),
        ("plant_protein", 1, "piece"), ("cacao_powder", 1, "tbsp"),
        ("date", 2, "piece")], None),
    ("vegan-mocha-protein", "Vegan Mocha Protein", 1, 3, [
        ("cold_brew", 0.5, "cup"), ("soy_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"), ("ice", 0.5, "cup")], None),
    ("hemp-protein-shake", "Hemp Seed Protein Shake", 1, 4, [
        ("soy_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("hemp_hearts", 2, "tbsp"), ("blueberry_frozen", 0.5, "cup")], None),
    ("vegan-vanilla-oat-protein", "Vegan Vanilla Oat Protein", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("oats", 3, "tbsp"), ("cinnamon", 0.25, "tsp"), ("maple_syrup", 2, "tsp")], None),
    ("vegan-tropical-protein", "Vegan Tropical Protein", 1, 3, [
        ("coconut_water", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("mango_frozen", 0.75, "cup")], None),
    ("vegan-pb-power", "Vegan Peanut Power", 1, 3, [
        ("soy_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("peanut_powder", 2, "tbsp"), ("banana_frozen", 0.5, "cup")], None),
    ("vegan-cherry-recovery", "Vegan Cherry Recovery", 1, 3, [
        ("cherry_juice", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("cherry_frozen", 0.5, "cup")], None),
    ("vegan-matcha-protein", "Vegan Matcha Protein", 1, 3, [
        ("soy_milk", 1, "cup"), ("plant_protein", 1, "piece"),
        ("matcha", 1, "tsp"), ("banana_frozen", 0.5, "cup")], None),
    ("vegan-fiber-protein", "Vegan Fiber Protein", 1, 4, [
        ("soy_milk", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("chia", 1, "tbsp"), ("raspberry", 0.75, "cup")], None),
    ("vegan-almond-date-protein", "Vegan Almond Date Protein", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("almond_butter", 1, "tbsp"), ("date", 2, "piece")], None),
    ("vegan-pumpkin-protein", "Vegan Pumpkin Protein", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("plant_protein", 1, "piece"),
        ("pumpkin_puree", 0.5, "cup"), ("cinnamon", 0.5, "tsp"),
        ("maple_syrup", 2, "tsp")], None),
    ("tofu-berry-breakfast-protein", "Tofu Berry Protein", 1, 4, [
        ("soy_milk", 0.75, "cup"), ("silken_tofu", 0.5, "cup"),
        ("plant_protein", 1, "piece"), ("strawberry_frozen", 0.5, "cup")], None),
    ("vegan-espresso-protein", "Vegan Espresso Protein", 1, 3, [
        ("espresso", 2, "piece"), ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"), ("ice", 0.5, "cup")], None),
]

# ------------------------------------------------------------------- coffee
COFFEE = [
    ("frozen-latte", "Frozen Vanilla Latte", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("milk_2", 0.5, "cup"),
        ("vanilla_extract", 0.5, "tsp"), ("maple_syrup", 2, "tsp"),
        ("ice", 1, "cup")], None),
    ("mocha-freeze", "Mocha Freeze", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("chocolate_syrup", 2, "tbsp"), ("ice", 1, "cup")], None),
    ("caramel-frappe", "Caramel Frappe", 1, 3, [
        ("coffee", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("caramel_sauce", 2, "tbsp"), ("ice", 1, "cup")], None),
    ("espresso-banana", "Espresso Banana", 1, 3, [
        ("espresso", 2, "piece"), ("almond_milk", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup")], None),
    ("vietnamese-style", "Sweet Condensed Coffee", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("condensed_milk", 2, "tbsp"),
        ("ice", 1, "cup")], None),
    ("coffee-oat-shake", "Coffee Oat Shake", 1, 4, [
        ("cold_brew", 0.5, "cup"), ("oat_milk", 0.75, "cup"),
        ("oats", 3, "tbsp"), ("date", 2, "piece"), ("ice", 0.5, "cup")], None),
    ("affogato-shake", "Affogato Shake", 1, 3, [
        ("espresso", 2, "piece"), ("ice_cream", 0.75, "cup"),
        ("milk_whole", 0.25, "cup")], None),
    ("coconut-cold-brew", "Coconut Cold Brew", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("coconut_milk_bev", 0.5, "cup"),
        ("maple_syrup", 2, "tsp"), ("ice", 1, "cup")], None),
    ("cinnamon-coffee", "Cinnamon Coffee Cream", 1, 3, [
        ("coffee", 0.75, "cup"), ("half_and_half", 3, "tbsp"),
        ("cinnamon", 0.5, "tsp"), ("brown_sugar", 2, "tsp"), ("ice", 1, "cup")], None),
    ("mocha-almond-freeze", "Mocha Almond Freeze", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("almond_milk", 0.5, "cup"),
        ("almond_butter", 1, "tbsp"), ("cacao_powder", 1, "tbsp"),
        ("ice", 0.75, "cup")], None),
    ("dalgona-style", "Whipped Coffee Shake", 1, 3, [
        ("instant_coffee", 2, "tsp"), ("milk_whole", 1, "cup"),
        ("sugar", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("pumpkin-latte-freeze", "Pumpkin Latte Freeze", 1, 4, [
        ("cold_brew", 0.5, "cup"), ("milk_2", 0.5, "cup"),
        ("pumpkin_puree", 0.33, "cup"), ("cinnamon", 0.5, "tsp"),
        ("maple_syrup", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("matcha-latte-freeze", "Iced Matcha Latte", 1, 3, [
        ("matcha", 1, "tsp"), ("oat_milk", 1, "cup"),
        ("honey", 2, "tsp"), ("ice", 1, "cup")], None),
    ("chai-freeze", "Chai Freeze", 1, 3, [
        ("chai_concentrate", 0.75, "cup"), ("milk_2", 0.5, "cup"),
        ("ice", 1, "cup")], None),
    ("dirty-chai", "Dirty Chai Freeze", 1, 3, [
        ("chai_concentrate", 0.5, "cup"), ("espresso", 1, "piece"),
        ("milk_2", 0.5, "cup"), ("ice", 1, "cup")], None),
    ("coffee-date-shake", "Coffee Date Shake", 1, 4, [
        ("cold_brew", 0.75, "cup"), ("almond_milk", 0.5, "cup"),
        ("date", 3, "piece"), ("ice", 0.75, "cup")], None),
    ("hazelnut-mocha", "Hazelnut Mocha", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("milk_2", 0.5, "cup"),
        ("choc_hazelnut", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("coffee-cacao-nib", "Cacao Nib Cold Brew", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("oat_milk", 0.5, "cup"),
        ("cacao_nibs", 1, "tbsp"), ("maple_syrup", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("mint-mocha", "Mint Mocha Freeze", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("milk_2", 0.5, "cup"),
        ("cacao_powder", 1, "tbsp"), ("mint", 2, "gram"),
        ("honey", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("green-tea-freeze", "Green Tea Freeze", 1, 3, [
        ("green_tea", 1, "cup"), ("honey", 2, "tsp"),
        ("lemon_juice", 2, "tsp"), ("ice", 1, "cup")], None),
]

# ---------------------------------------------------------------- breakfast
BREAKFAST = [
    ("oatmeal-in-a-glass", "Oatmeal in a Glass", 1, 4, [
        ("milk_2", 1, "cup"), ("oats", 0.33, "cup"), ("banana", 1, "piece"),
        ("cinnamon", 0.5, "tsp"), ("maple_syrup", 2, "tsp")], None),
    ("peanut-butter-banana-oats", "PB Banana Oats", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("oats", 0.25, "cup"),
        ("peanut_butter", 1, "tbsp"), ("banana_frozen", 0.5, "cup")], None),
    ("berry-yogurt-breakfast", "Berry Yogurt Breakfast", 1, 3, [
        ("milk_2", 0.5, "cup"), ("greek_yogurt_whole", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"), ("granola", 2, "tbsp")], None),
    ("granola-crunch-shake", "Granola Crunch Shake", 1, 3, [
        ("milk_whole", 0.75, "cup"), ("granola", 0.25, "cup"),
        ("banana_frozen", 0.5, "cup"), ("honey", 1, "tsp")], None),
    ("chia-breakfast", "Chia Breakfast Blend", 1, 4, [
        ("almond_milk", 1, "cup"), ("chia", 1.5, "tbsp"),
        ("banana_frozen", 0.5, "cup"), ("maple_syrup", 2, "tsp")], "Let it sit two minutes after blending and the chia thickens it."),
    ("flax-berry-breakfast", "Flax Berry Breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("flax", 1, "tbsp"),
        ("berries_mixed_frozen", 0.75, "cup"), ("greek_yogurt_nonfat", 0.25, "cup")], None),
    ("carrot-cake-breakfast", "Carrot Cake Breakfast", 1, 5, [
        ("oat_milk", 0.75, "cup"), ("carrot", 0.5, "cup"), ("oats", 3, "tbsp"),
        ("cinnamon", 0.5, "tsp"), ("raisin", 2, "tbsp"), ("maple_syrup", 2, "tsp")], None),
    ("sweet-potato-breakfast", "Sweet Potato Pie Shake", 1, 4, [
        ("milk_2", 0.75, "cup"), ("sweet_potato", 0.5, "cup"),
        ("cinnamon", 0.5, "tsp"), ("maple_syrup", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("wheat-germ-banana", "Wheat Germ Banana", 1, 3, [
        ("milk_2", 0.75, "cup"), ("wheat_germ", 2, "tbsp"),
        ("banana_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("apple-oat-breakfast", "Apple Oat Breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("apple", 1, "piece"), ("oats", 3, "tbsp"),
        ("cinnamon", 0.5, "tsp"), ("ice", 0.5, "cup")], None),
    ("cottage-peach-breakfast", "Cottage Peach Breakfast", 1, 3, [
        ("milk_skim", 0.5, "cup"), ("cottage_cheese", 0.5, "cup"),
        ("peach_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("mocha-oat-breakfast", "Mocha Oat Breakfast", 1, 4, [
        ("cold_brew", 0.5, "cup"), ("oat_milk", 0.5, "cup"), ("oats", 3, "tbsp"),
        ("cacao_powder", 1, "tsp"), ("banana_frozen", 0.5, "cup")], None),
    ("kefir-granola", "Kefir Granola Start", 1, 3, [
        ("kefir", 0.75, "cup"), ("granola", 3, "tbsp"),
        ("blueberry_frozen", 0.5, "cup")], None),
    ("almond-date-breakfast", "Almond Date Breakfast", 1, 4, [
        ("almond_milk", 1, "cup"), ("almond_butter", 1, "tbsp"),
        ("date", 3, "piece"), ("ice", 0.5, "cup")], None),
    ("maple-pecan-oats", "Maple Pecan Oats", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("oats", 0.25, "cup"), ("pecans", 1, "tbsp"),
        ("maple_syrup", 1, "tbsp"), ("cinnamon", 0.25, "tsp")], None),
    ("pumpkin-oat-breakfast", "Pumpkin Oat Breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"), ("pumpkin_puree", 0.5, "cup"), ("oats", 3, "tbsp"),
        ("cinnamon", 0.5, "tsp"), ("maple_syrup", 2, "tsp")], None),
    ("strawberry-oat-breakfast", "Strawberry Oat Breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("oats", 3, "tbsp"), ("honey", 2, "tsp")], None),
    ("banana-walnut-breakfast", "Banana Walnut Breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"), ("banana_frozen", 0.75, "cup"),
        ("walnuts", 2, "tbsp"), ("cinnamon", 0.25, "tsp")], None),
    ("blueberry-flax-breakfast", "Blueberry Flax Breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("flax", 1, "tbsp"), ("greek_yogurt_nonfat", 0.25, "cup")], None),
    ("tahini-banana-breakfast", "Tahini Banana Breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("tahini", 1, "tbsp"),
        ("banana_frozen", 0.75, "cup"), ("honey", 2, "tsp")], None),
    ("oat-bran-berry", "Oat Bran Berry", 1, 4, [
        ("milk_2", 0.75, "cup"), ("oat_bran", 3, "tbsp"),
        ("berries_mixed_frozen", 0.75, "cup"), ("maple_syrup", 2, "tsp")], None),
    ("sunflower-breakfast", "Sunflower Seed Breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("sunflower_butter", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"), ("oats", 2, "tbsp")], "Nut-free, so it works for school-safe mornings."),
    ("hemp-oat-breakfast", "Hemp Oat Breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("hemp_hearts", 2, "tbsp"),
        ("oats", 3, "tbsp"), ("blueberry_frozen", 0.5, "cup")], None),
    ("mango-yogurt-breakfast", "Mango Yogurt Breakfast", 1, 3, [
        ("milk_2", 0.5, "cup"), ("greek_yogurt_whole", 0.5, "cup"),
        ("mango_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("cocoa-oat-breakfast", "Cocoa Oat Breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("oats", 0.25, "cup"),
        ("cacao_powder", 1, "tbsp"), ("banana_frozen", 0.5, "cup"),
        ("maple_syrup", 2, "tsp")], None),
]

# ------------------------------------------------------------------ dessert
DESSERT = [
    ("vanilla-milkshake", "Vanilla Milkshake", 1, 3, [
        ("ice_cream", 1, "cup"), ("milk_whole", 0.5, "cup"),
        ("vanilla_extract", 0.5, "tsp")], None),
    ("chocolate-milkshake", "Chocolate Milkshake", 1, 3, [
        ("ice_cream", 1, "cup"), ("milk_whole", 0.5, "cup"),
        ("chocolate_syrup", 2, "tbsp")], None),
    ("strawberry-milkshake", "Strawberry Milkshake", 1, 3, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("strawberry_frozen", 0.5, "cup")], None),
    ("cookies-and-cream-shake", "Cookies and Cream Shake", 1, 3, [
        ("ice_cream", 1, "cup"), ("milk_whole", 0.5, "cup"),
        ("choc_cookie", 3, "piece")], None),
    ("brownie-batter", "Brownie Batter Shake", 1, 3, [
        ("milk_whole", 0.75, "cup"), ("ice_cream", 0.5, "cup"),
        ("cacao_powder", 2, "tbsp"), ("date", 2, "piece")], None),
    ("key-lime-pie", "Key Lime Pie Shake", 1, 4, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.25, "cup"),
        ("lime_juice", 2, "tbsp"), ("graham_cracker", 2, "piece")], None),
    ("banana-split", "Banana Split Shake", 1, 4, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("banana", 1, "piece"), ("chocolate_syrup", 1, "tbsp")], None),
    ("salted-caramel-shake", "Salted Caramel Shake", 1, 3, [
        ("ice_cream", 1, "cup"), ("milk_whole", 0.5, "cup"),
        ("caramel_sauce", 2, "tbsp"), ("salt", 0.1, "tsp")], None),
    ("peanut-butter-cup-shake", "Peanut Butter Cup Shake", 1, 3, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("peanut_butter", 2, "tbsp"), ("cacao_powder", 1, "tbsp")], None),
    ("mint-chip-shake", "Mint Chip Shake", 1, 3, [
        ("ice_cream", 1, "cup"), ("milk_whole", 0.5, "cup"),
        ("mint", 3, "gram"), ("cacao_nibs", 1, "tbsp")], None),
    ("frozen-hot-chocolate", "Frozen Hot Chocolate", 1, 3, [
        ("milk_whole", 0.75, "cup"), ("cacao_powder", 2, "tbsp"),
        ("sugar", 1, "tbsp"), ("ice", 1, "cup")], None),
    ("cheesecake-shake", "Cheesecake Shake", 1, 4, [
        ("milk_whole", 0.5, "cup"), ("cream_cheese", 3, "tbsp"),
        ("graham_cracker", 2, "piece"), ("sugar", 2, "tsp"), ("ice", 1, "cup")], None),
    ("tiramisu-shake", "Tiramisu Shake", 1, 4, [
        ("espresso", 2, "piece"), ("milk_whole", 0.5, "cup"),
        ("cream_cheese", 2, "tbsp"), ("sugar", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("affogato-float", "Coffee Float", 1, 3, [
        ("cold_brew", 0.75, "cup"), ("ice_cream", 0.75, "cup")], None),
    ("apple-crisp-shake", "Apple Crisp Shake", 1, 4, [
        ("applesauce", 0.5, "cup"), ("ice_cream", 0.75, "cup"),
        ("granola", 2, "tbsp"), ("cinnamon", 0.5, "tsp")], None),
    ("pumpkin-pie-shake", "Pumpkin Pie Shake", 1, 4, [
        ("pumpkin_puree", 0.5, "cup"), ("ice_cream", 0.75, "cup"),
        ("milk_whole", 0.25, "cup"), ("cinnamon", 0.5, "tsp"),
        ("nutmeg", 0.1, "tsp")], None),
    ("nutella-shake", "Chocolate Hazelnut Shake", 1, 3, [
        ("milk_whole", 0.75, "cup"), ("choc_hazelnut", 2, "tbsp"),
        ("ice_cream", 0.5, "cup")], None),
    ("s-mores-shake", "S'mores Shake", 1, 4, [
        ("milk_whole", 0.5, "cup"), ("ice_cream", 0.75, "cup"),
        ("chocolate_syrup", 1, "tbsp"), ("graham_cracker", 2, "piece")], None),
    ("coconut-fudge", "Coconut Fudge Shake", 1, 3, [
        ("coconut_milk_canned", 0.33, "cup"), ("milk_whole", 0.5, "cup"),
        ("cacao_powder", 2, "tbsp"), ("maple_syrup", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("frozen-yogurt-berry", "Frozen Yogurt Berry", 1, 3, [
        ("frozen_yogurt", 0.75, "cup"), ("milk_2", 0.5, "cup"),
        ("berries_mixed_frozen", 0.5, "cup")], None),
    ("caramel-apple-shake", "Caramel Apple Shake", 1, 4, [
        ("apple", 1, "piece"), ("ice_cream", 0.75, "cup"),
        ("caramel_sauce", 1, "tbsp"), ("milk_whole", 0.25, "cup")], None),
    ("chocolate-cherry-shake", "Black Forest Shake", 1, 3, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("cherry_frozen", 0.5, "cup"), ("cacao_powder", 1, "tbsp")], None),
    ("maple-walnut-shake", "Maple Walnut Shake", 1, 3, [
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.5, "cup"),
        ("walnuts", 2, "tbsp"), ("maple_syrup", 1, "tbsp")], None),
    ("orange-dreamsicle-shake", "Orange Dreamsicle Shake", 1, 3, [
        ("orange_juice", 0.5, "cup"), ("ice_cream", 0.75, "cup"),
        ("vanilla_extract", 0.5, "tsp"), ("ice", 0.5, "cup")], None),
    ("pistachio-shake", "Pistachio Shake", 1, 4, [
        ("milk_whole", 0.75, "cup"), ("pistachios", 3, "tbsp"),
        ("ice_cream", 0.5, "cup"), ("honey", 1, "tsp")], None),
    ("blueberry-cheesecake-shake", "Blueberry Cheesecake Shake", 1, 4, [
        ("milk_whole", 0.5, "cup"), ("cream_cheese", 2, "tbsp"),
        ("blueberry_frozen", 0.75, "cup"), ("graham_cracker", 1, "piece"),
        ("sugar", 2, "tsp")], None),
    ("espresso-chip-shake", "Espresso Chip Shake", 1, 3, [
        ("espresso", 1, "piece"), ("ice_cream", 1, "cup"),
        ("cacao_nibs", 1, "tbsp"), ("milk_whole", 0.25, "cup")], None),
    ("banana-cream-pie-shake", "Banana Cream Pie Shake", 1, 4, [
        ("milk_whole", 0.5, "cup"), ("banana_frozen", 0.75, "cup"),
        ("ice_cream", 0.5, "cup"), ("graham_cracker", 1, "piece")], None),
    ("choc-avocado-mousse", "Chocolate Avocado Mousse", 2, 5, [
        ("avocado", 1, "piece"), ("cacao_powder", 3, "tbsp"),
        ("maple_syrup", 3, "tbsp"), ("milk_whole", 0.33, "cup"),
        ("vanilla_extract", 0.5, "tsp")], "Thick by design. Chill it and eat it with a spoon."),
    ("date-caramel-shake", "Date Caramel Shake", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("date", 4, "piece"),
        ("ice_cream", 0.5, "cup"), ("salt", 0.1, "tsp")], None),
]

# ----------------------------------------------------------------- cocktail
COCKTAIL = [
    ("frozen-margarita", "Frozen Lime Margarita", 2, 4, [
        ("tequila", 0.25, "cup"), ("triple_sec", 2, "tbsp"),
        ("lime_juice", 3, "tbsp"), ("limeade_frozen", 0.25, "cup"),
        ("ice", 1, "cup")], None),
    ("strawberry-margarita", "Strawberry Margarita", 2, 4, [
        ("tequila", 0.25, "cup"), ("triple_sec", 2, "tbsp"),
        ("strawberry_frozen", 0.75, "cup"), ("lime_juice", 2, "tbsp"),
        ("ice", 0.75, "cup")], None),
    ("frozen-daiquiri", "Frozen Strawberry Daiquiri", 2, 4, [
        ("white_rum", 0.25, "cup"), ("strawberry_frozen", 1, "cup"),
        ("lime_juice", 2, "tbsp"), ("sugar", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("pina-colada", "Pina Colada", 2, 4, [
        ("white_rum", 0.25, "cup"), ("pineapple_frozen", 1, "cup"),
        ("coconut_milk_canned", 0.33, "cup"), ("ice", 0.5, "cup")], None),
    ("frozen-mojito", "Frozen Mojito", 2, 4, [
        ("white_rum", 0.25, "cup"), ("lime_juice", 3, "tbsp"),
        ("mint", 5, "gram"), ("sugar", 1, "tbsp"), ("ice", 1.25, "cup")], None),
    ("mango-daiquiri", "Mango Daiquiri", 2, 4, [
        ("white_rum", 0.25, "cup"), ("mango_frozen", 1, "cup"),
        ("lime_juice", 2, "tbsp"), ("ice", 0.5, "cup")], None),
    ("watermelon-margarita", "Watermelon Margarita", 2, 4, [
        ("tequila", 0.25, "cup"), ("watermelon", 1, "cup"),
        ("lime_juice", 2, "tbsp"), ("triple_sec", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("frozen-espresso-martini", "Frozen Espresso Martini", 2, 4, [
        ("vodka", 3, "tbsp"), ("coffee_liqueur", 3, "tbsp"),
        ("espresso", 2, "piece"), ("ice", 1, "cup")], None),
    ("peach-bellini-freeze", "Frozen Peach Bellini", 2, 3, [
        ("prosecco", 0.5, "cup"), ("peach_frozen", 1, "cup"),
        ("lemon_juice", 1, "tbsp")], "Add the prosecco last and pulse briefly so it keeps some fizz."),
    ("frozen-cosmo", "Frozen Cosmopolitan", 2, 4, [
        ("vodka", 3, "tbsp"), ("triple_sec", 2, "tbsp"),
        ("cranberry_juice", 0.5, "cup"), ("lime_juice", 1, "tbsp"),
        ("ice", 1, "cup")], None),
    ("blueberry-vodka-crush", "Blueberry Vodka Crush", 2, 4, [
        ("vodka", 0.25, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("lemon_juice", 2, "tbsp"), ("honey", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("frozen-paloma", "Frozen Paloma", 2, 4, [
        ("tequila", 0.25, "cup"), ("grapefruit", 1, "piece"),
        ("lime_juice", 2, "tbsp"), ("agave", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("coconut-rum-freeze", "Coconut Rum Freeze", 2, 3, [
        ("white_rum", 0.25, "cup"), ("coconut_milk_canned", 0.33, "cup"),
        ("banana_frozen", 0.5, "cup"), ("ice", 0.75, "cup")], None),
    ("raspberry-prosecco-freeze", "Raspberry Prosecco Freeze", 2, 3, [
        ("prosecco", 0.5, "cup"), ("raspberry", 1, "cup"),
        ("sugar", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("frozen-white-sangria", "Frozen White Sangria", 2, 4, [
        ("white_wine", 0.75, "cup"), ("peach_frozen", 0.5, "cup"),
        ("grapes", 0.5, "cup"), ("orange_juice", 0.25, "cup"), ("ice", 0.5, "cup")], None),
    ("mudslide", "Frozen Mudslide", 2, 4, [
        ("vodka", 2, "tbsp"), ("coffee_liqueur", 3, "tbsp"),
        ("ice_cream", 0.75, "cup"), ("milk_whole", 0.25, "cup")], None),
    ("pineapple-tequila-crush", "Pineapple Tequila Crush", 2, 4, [
        ("tequila", 0.25, "cup"), ("pineapple_frozen", 1, "cup"),
        ("lime_juice", 2, "tbsp"), ("jalapeno", 0.25, "piece"), ("ice", 0.5, "cup")], None),
    ("cherry-rum-freeze", "Cherry Rum Freeze", 2, 4, [
        ("white_rum", 0.25, "cup"), ("cherry_frozen", 1, "cup"),
        ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("mango-chili-margarita", "Mango Chili Margarita", 2, 5, [
        ("tequila", 0.25, "cup"), ("mango_frozen", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"), ("jalapeno", 0.5, "piece"),
        ("agave", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("frozen-irish-coffee", "Frozen Irish Coffee", 2, 4, [
        ("coffee_liqueur", 3, "tbsp"), ("cold_brew", 0.5, "cup"),
        ("heavy_cream", 2, "tbsp"), ("ice", 1, "cup")], None),
]

# ----------------------------------------------------------------- mocktail
MOCKTAIL = [
    ("virgin-pina-colada", "Virgin Pina Colada", 1, 3, [
        ("pineapple_frozen", 1, "cup"), ("coconut_milk_canned", 0.25, "cup"),
        ("pineapple_juice", 0.5, "cup"), ("ice", 0.5, "cup")], None),
    ("virgin-mojito", "Virgin Mojito Freeze", 1, 4, [
        ("water", 0.5, "cup"), ("lime_juice", 3, "tbsp"), ("mint", 5, "gram"),
        ("honey", 1, "tbsp"), ("ice", 1.25, "cup")], None),
    ("virgin-daiquiri", "Virgin Strawberry Daiquiri", 1, 3, [
        ("strawberry_frozen", 1, "cup"), ("lime_juice", 2, "tbsp"),
        ("sugar", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("shirley-temple-freeze", "Cherry Shirley Freeze", 1, 3, [
        ("cherry_juice", 0.75, "cup"), ("cherry_frozen", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"), ("ice", 0.75, "cup")], None),
    ("cucumber-lime-cooler", "Cucumber Lime Cooler", 1, 4, [
        ("water", 0.5, "cup"), ("cucumber", 1, "cup"), ("lime_juice", 2, "tbsp"),
        ("mint", 3, "gram"), ("honey", 2, "tsp"), ("ice", 0.75, "cup")], None),
    ("virgin-paloma", "Virgin Paloma", 1, 4, [
        ("grapefruit", 1, "piece"), ("lime_juice", 1, "tbsp"),
        ("agave", 2, "tsp"), ("kombucha", 0.5, "cup"), ("ice", 0.75, "cup")], None),
    ("frozen-lemonade", "Frozen Lemonade", 1, 3, [
        ("water", 0.5, "cup"), ("lemonade_frozen", 0.33, "cup"),
        ("ice", 1.25, "cup")], None),
    ("frozen-limeade", "Frozen Limeade", 1, 3, [
        ("water", 0.5, "cup"), ("limeade_frozen", 0.33, "cup"),
        ("ice", 1.25, "cup")], None),
    ("arnold-palmer-freeze", "Frozen Arnold Palmer", 1, 3, [
        ("green_tea", 0.75, "cup"), ("lemonade_frozen", 0.25, "cup"),
        ("ice", 1, "cup")], None),
    ("berry-spritz", "Berry Kombucha Spritz", 1, 3, [
        ("kombucha", 0.75, "cup"), ("berries_mixed_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tbsp")], None),
    ("ginger-peach-mock", "Ginger Peach Mocktail", 1, 4, [
        ("kombucha", 0.5, "cup"), ("peach_frozen", 0.75, "cup"),
        ("ginger", 4, "gram"), ("honey", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("watermelon-basil-mock", "Watermelon Basil Mocktail", 1, 4, [
        ("watermelon", 1.5, "cup"), ("basil", 3, "gram"),
        ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("pomegranate-spritz", "Pomegranate Spritz", 1, 3, [
        ("pomegranate_juice", 0.75, "cup"), ("kombucha", 0.25, "cup"),
        ("lime_juice", 1, "tbsp"), ("ice", 1, "cup")], None),
    ("pineapple-mint-mock", "Pineapple Mint Mocktail", 1, 4, [
        ("pineapple_juice", 0.5, "cup"), ("pineapple_frozen", 0.75, "cup"),
        ("mint", 4, "gram"), ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("cranberry-orange-mock", "Cranberry Orange Mocktail", 1, 3, [
        ("cranberry_juice", 0.5, "cup"), ("orange_juice", 0.5, "cup"),
        ("cranberry_frozen", 0.25, "cup"), ("ice", 0.75, "cup")], None),
    ("mango-coconut-mock", "Mango Coconut Mocktail", 1, 3, [
        ("coconut_water", 0.75, "cup"), ("mango_frozen", 1, "cup"),
        ("lime_juice", 1, "tbsp")], None),
    ("spicy-tamarind-style", "Spicy Mango Chamoy Style", 1, 4, [
        ("mango_frozen", 1, "cup"), ("lime_juice", 2, "tbsp"),
        ("jalapeno", 0.25, "piece"), ("honey", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("blue-lagoon-mock", "Blueberry Lagoon", 1, 3, [
        ("lemonade_frozen", 0.25, "cup"), ("blueberry_frozen", 0.75, "cup"),
        ("water", 0.5, "cup"), ("ice", 0.5, "cup")], None),
]

# --------------------------------------------------------------------- kids
KIDS = [
    ("purple-cow", "Purple Cow", 1, 3, [
        ("milk_2", 0.75, "cup"), ("blueberry_frozen", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"), ("honey", 1, "tsp")], None),
    ("pink-drink-kids", "Pink Drink", 1, 3, [
        ("milk_2", 0.5, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("yogurt_vanilla", 0.25, "cup")], None),
    ("monster-smoothie", "Monster Smoothie", 1, 4, [
        ("apple_juice", 0.75, "cup"), ("spinach", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"), ("mango_frozen", 0.25, "cup")], "Call it a monster and the spinach stops being a problem."),
    ("peanut-butter-jelly-shake", "PB and J Shake", 1, 3, [
        ("milk_2", 0.75, "cup"), ("peanut_butter", 1, "tbsp"),
        ("strawberry_frozen", 0.75, "cup"), ("honey", 1, "tsp")], None),
    ("banana-milk", "Simple Banana Milk", 1, 2, [
        ("milk_2", 1, "cup"), ("banana_frozen", 0.75, "cup"),
        ("cinnamon", 0.1, "tsp")], None),
    ("orange-fluff", "Orange Fluff", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("yogurt_vanilla", 0.5, "cup"),
        ("ice", 0.5, "cup")], None),
    ("chocolate-banana-kids", "Chocolate Banana", 1, 3, [
        ("milk_2", 0.75, "cup"), ("banana_frozen", 0.75, "cup"),
        ("chocolate_syrup", 1, "tbsp"), ("honey", 1, "tsp")],
        "Chocolate syrup rather than cacao powder here — cacao carries real caffeine, and this one is for kids."),
    ("apple-cinnamon-kids", "Apple Cinnamon Cup", 1, 3, [
        ("milk_2", 0.75, "cup"), ("applesauce", 0.5, "cup"),
        ("cinnamon", 0.25, "tsp"), ("ice", 0.5, "cup")], None),
    ("berry-yogurt-kids", "Berry Yogurt Cup", 1, 3, [
        ("yogurt_vanilla", 0.5, "cup"), ("milk_2", 0.5, "cup"),
        ("berries_mixed_frozen", 0.5, "cup")], None),
    ("mango-sunshine-kids", "Mango Sunshine", 1, 3, [
        ("orange_juice", 0.75, "cup"), ("mango_frozen", 0.75, "cup")], None),
    ("blueberry-banana-kids", "Blueberry Banana", 1, 3, [
        ("milk_2", 0.75, "cup"), ("blueberry_frozen", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup")], None),
    ("watermelon-slush-kids", "Watermelon Slush", 1, 3, [
        ("watermelon", 1.5, "cup"), ("ice", 0.75, "cup"),
        ("honey", 1, "tsp")], None),
    ("peach-cream-kids", "Peach Cream Cup", 1, 3, [
        ("milk_2", 0.5, "cup"), ("peach_frozen", 0.75, "cup"),
        ("yogurt_vanilla", 0.25, "cup")], None),
    ("cocoa-oat-kids", "Cocoa Oat Cup", 1, 3, [
        ("oat_milk", 0.75, "cup"), ("banana_frozen", 0.5, "cup"),
        ("oats", 2, "tbsp"), ("chocolate_syrup", 2, "tsp"), ("honey", 1, "tsp")], None),
    ("strawberry-oat-kids", "Strawberry Oat Cup", 1, 3, [
        ("oat_milk", 0.75, "cup"), ("strawberry_frozen", 0.75, "cup"),
        ("oats", 2, "tbsp"), ("honey", 1, "tsp")], None),
]

# ----------------------------------------------------------------- wellness
WELLNESS = [
    ("immunity-shot-blend", "Ginger Turmeric Tonic", 1, 4, [
        ("orange_juice", 0.75, "cup"), ("ginger", 6, "gram"),
        ("turmeric", 0.5, "tsp"), ("black_pepper", 0.05, "tsp"),
        ("lemon_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("golden-milk-freeze", "Golden Milk Freeze", 1, 4, [
        ("coconut_milk_bev", 1, "cup"), ("turmeric", 0.5, "tsp"),
        ("cinnamon", 0.25, "tsp"), ("black_pepper", 0.05, "tsp"),
        ("honey", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("gut-health-kefir", "Gut Health Kefir", 1, 3, [
        ("kefir", 0.75, "cup"), ("berries_mixed_frozen", 0.5, "cup"),
        ("chia", 1, "tbsp"), ("honey", 1, "tsp")], None),
    ("fiber-fix", "Fiber Fix", 1, 4, [
        ("water", 0.75, "cup"), ("psyllium", 1, "tsp"), ("chia", 1, "tbsp"),
        ("raspberry", 0.75, "cup"), ("honey", 2, "tsp")], "Drink it soon after blending — psyllium thickens fast."),
    ("beet-nitric", "Beet Endurance", 1, 4, [
        ("beet", 0.75, "cup"), ("apple_juice", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"), ("ginger", 3, "gram"), ("ice", 0.5, "cup")], None),
    ("electrolyte-refresh", "Electrolyte Refresh", 1, 3, [
        ("coconut_water", 1, "cup"), ("watermelon", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"), ("salt", 0.1, "tsp"), ("ice", 0.5, "cup")], None),
    ("matcha-focus", "Matcha Focus", 1, 3, [
        ("almond_milk", 1, "cup"), ("matcha", 1, "tsp"),
        ("collagen", 1, "piece"), ("honey", 1, "tsp"), ("ice", 0.5, "cup")], None),
    ("spirulina-shot", "Spirulina Green Tonic", 1, 4, [
        ("coconut_water", 0.75, "cup"), ("spirulina", 1, "tsp"),
        ("pineapple_frozen", 0.75, "cup"), ("lime_juice", 1, "tbsp")], None),
    ("maca-energy", "Maca Energy", 1, 4, [
        ("oat_milk", 0.75, "cup"), ("maca", 1, "tsp"),
        ("banana_frozen", 0.75, "cup"), ("almond_butter", 1, "tbsp")], None),
    ("tart-cherry-sleep", "Tart Cherry Wind-Down", 1, 3, [
        ("cherry_juice", 0.75, "cup"), ("cherry_frozen", 0.5, "cup"),
        ("chia", 1, "tsp"), ("ice", 0.25, "cup")], None),
    ("anti-inflammatory-berry", "Anti-Inflammatory Berry", 1, 4, [
        ("green_tea", 0.75, "cup"), ("berries_mixed_frozen", 0.75, "cup"),
        ("turmeric", 0.25, "tsp"), ("ginger", 3, "gram"), ("honey", 1, "tsp")], None),
    ("liver-love-green", "Citrus Green Tonic", 1, 4, [
        ("water", 0.75, "cup"), ("spinach", 1, "cup"), ("lemon_juice", 2, "tbsp"),
        ("apple_green", 1, "piece"), ("ginger", 3, "gram"), ("ice", 0.5, "cup")], None),
    ("omega-boost", "Omega Boost", 1, 4, [
        ("almond_milk", 0.75, "cup"), ("flax", 1, "tbsp"), ("chia", 1, "tbsp"),
        ("walnuts", 1, "tbsp"), ("blueberry_frozen", 0.5, "cup")], None),
    ("hydration-cucumber", "Hydration Cooler", 1, 3, [
        ("coconut_water", 1, "cup"), ("cucumber", 0.75, "cup"),
        ("mint", 3, "gram"), ("lime_juice", 1, "tbsp"), ("ice", 0.5, "cup")], None),
    ("iron-boost", "Iron Boost Green", 1, 4, [
        ("orange_juice", 0.75, "cup"), ("spinach", 1, "cup"),
        ("pumpkin_seeds", 1, "tbsp"), ("strawberry_frozen", 0.5, "cup")], "Vitamin C from the orange helps you absorb the iron from the greens."),
    ("bone-broth-free-calcium", "Calcium Green", 1, 4, [
        ("milk_2", 0.75, "cup"), ("kale", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"), ("chia", 1, "tbsp")], None),
    ("probiotic-tropical", "Probiotic Tropical", 1, 3, [
        ("kefir", 0.75, "cup"), ("mango_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tsp")], None),
    ("low-sugar-green", "Low Sugar Green", 1, 4, [
        ("water", 0.75, "cup"), ("spinach", 1, "cup"), ("avocado", 0.5, "piece"),
        ("lemon_juice", 2, "tbsp"), ("stevia", 0.25, "tsp"), ("ice", 0.5, "cup")], None),
    ("cold-fighter", "Cold Fighter", 1, 4, [
        ("orange_juice", 0.75, "cup"), ("kiwi", 1, "piece"),
        ("ginger", 4, "gram"), ("honey", 2, "tsp"), ("ice", 0.5, "cup")], None),
    ("magnesium-cocoa", "Cocoa Magnesium Calm", 1, 3, [
        ("almond_milk", 1, "cup"), ("cacao_powder", 1, "tbsp"),
        ("pumpkin_seeds", 1, "tbsp"), ("date", 2, "piece")], None),
]

# ------------------------------------------------------------------- savory
SAVORY = [
    ("gazpacho", "Chilled Gazpacho", 2, 6, [
        ("tomato", 2, "piece"), ("cucumber", 0.75, "cup"),
        ("bell_pepper", 0.5, "piece"), ("olive_oil", 1, "tbsp"),
        ("cider_vinegar", 1, "tbsp"), ("garlic", 1, "piece"),
        ("salt", 0.5, "tsp")], "Chill it an hour before serving."),
    ("classic-hummus-style", "Tahini Chickpea-Free Dip", 2, 5, [
        ("silken_tofu", 0.75, "cup"), ("tahini", 2, "tbsp"),
        ("lemon_juice", 2, "tbsp"), ("garlic", 1, "piece"),
        ("olive_oil", 1, "tbsp"), ("cumin", 0.5, "tsp"), ("salt", 0.5, "tsp")], None),
    ("green-goddess-dressing", "Green Goddess Dressing", 4, 5, [
        ("greek_yogurt_nonfat", 0.5, "cup"), ("mayonnaise", 2, "tbsp"),
        ("parsley", 0.25, "cup"), ("basil", 8, "gram"),
        ("lemon_juice", 2, "tbsp"), ("garlic", 1, "piece"), ("salt", 0.5, "tsp")], None),
    ("avocado-crema", "Avocado Crema", 2, 4, [
        ("avocado", 1, "piece"), ("sour_cream", 0.25, "cup"),
        ("lime_juice", 2, "tbsp"), ("cilantro", 8, "gram"),
        ("jalapeno", 0.5, "piece"), ("salt", 0.5, "tsp")], None),
    ("caesar-style-dressing", "Creamy Garlic Dressing", 4, 5, [
        ("mayonnaise", 0.25, "cup"), ("greek_yogurt_nonfat", 0.25, "cup"),
        ("lemon_juice", 2, "tbsp"), ("dijon", 1, "tsp"),
        ("garlic", 2, "piece"), ("black_pepper", 0.5, "tsp")], None),
    ("roasted-pepper-dip", "Red Pepper Feta Dip", 2, 5, [
        ("bell_pepper", 1, "piece"), ("feta", 70, "gram"),
        ("olive_oil", 1, "tbsp"), ("lemon_juice", 1, "tbsp"),
        ("garlic", 1, "piece"), ("cumin", 0.25, "tsp")], None),
    ("cilantro-lime-dressing", "Cilantro Lime Dressing", 4, 4, [
        ("olive_oil", 0.25, "cup"), ("lime_juice", 3, "tbsp"),
        ("cilantro", 15, "gram"), ("honey", 1, "tsp"),
        ("garlic", 1, "piece"), ("salt", 0.5, "tsp")], None),
    ("carrot-ginger-dressing", "Carrot Ginger Dressing", 4, 5, [
        ("carrot", 0.75, "cup"), ("olive_oil", 3, "tbsp"),
        ("cider_vinegar", 2, "tbsp"), ("ginger", 6, "gram"),
        ("honey", 1, "tsp"), ("salt", 0.5, "tsp")], None),
    ("tomato-basil-soup-cold", "Cold Tomato Basil Soup", 2, 5, [
        ("tomato", 2, "piece"), ("basil", 8, "gram"),
        ("olive_oil", 1, "tbsp"), ("garlic", 1, "piece"),
        ("salt", 0.5, "tsp"), ("black_pepper", 0.25, "tsp")], None),
    ("cucumber-yogurt-soup", "Cucumber Yogurt Soup", 2, 5, [
        ("cucumber", 1.5, "cup"), ("greek_yogurt_nonfat", 0.5, "cup"),
        ("mint", 5, "gram"), ("garlic", 0.5, "piece"),
        ("olive_oil", 1, "tbsp"), ("salt", 0.5, "tsp")], None),
    ("spicy-peanut-sauce", "Spicy Peanut Sauce", 4, 4, [
        ("peanut_butter", 0.25, "cup"), ("lime_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"), ("water", 3, "tbsp"),
        ("garlic", 1, "piece"), ("jalapeno", 0.5, "piece")], None),
    ("pesto-style", "Blender Basil Pesto", 4, 5, [
        ("basil", 30, "gram"), ("olive_oil", 0.25, "cup"),
        ("walnuts", 3, "tbsp"), ("garlic", 2, "piece"),
        ("lemon_juice", 1, "tbsp"), ("salt", 0.5, "tsp")], "Pulse rather than run it long if you want texture."),
    ("beet-hummus-style", "Beet Tahini Dip", 2, 5, [
        ("beet", 1, "cup"), ("tahini", 2, "tbsp"), ("lemon_juice", 2, "tbsp"),
        ("garlic", 1, "piece"), ("cumin", 0.5, "tsp"), ("salt", 0.5, "tsp")], None),
    ("ranch-style-dressing", "Herb Ranch Dressing", 4, 4, [
        ("greek_yogurt_nonfat", 0.5, "cup"), ("mayonnaise", 2, "tbsp"),
        ("milk_2", 2, "tbsp"), ("parsley", 0.25, "cup"),
        ("garlic", 1, "piece"), ("black_pepper", 0.25, "tsp"), ("salt", 0.25, "tsp")], None),
    ("salsa-verde-style", "Creamy Jalapeño Salsa", 2, 4, [
        ("sour_cream", 0.33, "cup"), ("cilantro", 10, "gram"),
        ("jalapeno", 1, "piece"), ("lime_juice", 2, "tbsp"),
        ("garlic", 1, "piece"), ("salt", 0.5, "tsp")], None),
]
