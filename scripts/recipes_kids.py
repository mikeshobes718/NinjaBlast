"""Kid-friendly blender drinks: bright colors, smooth texture, no caffeine, no alcohol."""

RECIPES = [
    # --- Color first: kids drink with their eyes -------------------------
    ("kd-dragon-breath", "Dragon Breath", "kids", 2, 3, [
        ("dragonfruit_frozen", 1, "cup"),
        ("banana", 0.5, "piece"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("lime_juice", 1, "tsp"),
    ], "Buy the pink-fleshed dragon fruit, not the white — white blends out a dull grey and the color is the entire point."),

    ("kd-mermaid-tail", "Mermaid Tail", "kids", 2, 3, [
        ("pineapple_frozen", 1, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("blue_spirulina", 0.5, "tsp"),
    ], "Half a teaspoon of blue spirulina is already vivid; go past a full one and it turns teal and tastes faintly of the sea."),

    ("kd-color-change-potion", "Color-Changing Potion", "kids", 2, 4, [
        ("blue_matcha", 0.5, "tsp"),
        ("white_grape_juice", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("lemon_juice", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Blend everything except the lemon juice, then let them stir it in at the table — the acid flips butterfly pea from blue to violet while they watch."),

    ("kd-dinosaur-juice", "Dinosaur Juice", "kids", 2, 3, [
        ("spinach_frozen", 0.5, "cup"),
        ("pineapple_frozen", 1, "cup"),
        ("mango", 0.5, "piece"),
        ("apple_juice", 0.75, "cup"),
    ], "Frozen spinach blends away to nothing; fresh leaves leave green flecks that get interrogated."),

    ("kd-fairy-dust", "Fairy Dust", "kids", 2, 4, [
        ("beet", 0.25, "cup"),
        ("strawberry_frozen", 1, "cup"),
        ("yogurt_vanilla", 0.25, "cup"),
        ("oat_milk", 0.75, "cup"),
    ], "A quarter cup of cooked beet gives you the pink; half a cup starts tasting like the garden it came from."),

    ("kd-tiger-stripes", "Tiger Stripes", "kids", 2, 5, [
        ("carrot", 1, "piece"),
        ("mango_frozen", 0.75, "cup"),
        ("orange_juice", 0.75, "cup"),
        ("banana", 0.5, "piece"),
    ], "Cut the carrot into coins no thicker than a penny — the Blast handles raw carrot, but only in small pieces."),

    ("kd-midnight-purple", "Midnight Purple", "kids", 2, 3, [
        ("blackcurrant", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("honey", 1, "tsp"),
    ], None),

    ("kd-lava-flow", "Volcano Float", "kids", 2, 4, [
        ("strawberry_frozen", 1, "cup"),
        ("watermelon", 0.75, "cup"),
        ("apple_juice", 0.5, "cup"),
    ], None),

    ("kd-swamp-water", "Swamp Water", "kids", 2, 4, [
        ("kiwi", 2, "piece"),
        ("spinach", 1, "cup"),
        ("white_grape_juice", 0.75, "cup"),
        ("ice", 0.5, "cup"),
    ], None),

    ("kd-red-racer", "Red Racer", "kids", 2, 3, [
        ("beet_juice", 0.5, "cup"),
        ("strawberry_frozen", 1, "cup"),
        ("orange_juice", 0.25, "cup"),
        ("banana", 0.5, "piece"),
    ], None),

    ("kd-fireworks", "Fireworks", "kids", 2, 4, [
        ("blueberry_frozen", 0.75, "cup"),
        ("strawberry_frozen", 0.5, "cup"),
        ("yogurt_vanilla", 0.25, "cup"),
        ("milk_2", 0.75, "cup"),
    ], "Blend the blueberries with the milk first and pour half out, then blend the strawberries in — you get two colors in one cup without washing anything."),

    # --- Hidden vegetables -----------------------------------------------
    ("kd-secret-agent-shake", "Secret Agent Shake", "kids", 2, 3, [
        ("cauliflower_frozen", 0.5, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("chocolate_syrup", 1, "tbsp"),
        ("milk_2", 0.75, "cup"),
    ], "Use the riced cauliflower straight from the freezer — thawed, it goes watery and the cabbage taste surfaces."),

    ("kd-blast-off-chocolate", "Blast Off Chocolate", "kids", 2, 3, [
        ("zucchini_frozen", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("chocolate_syrup", 1, "tbsp"),
        ("oat_milk", 0.75, "cup"),
        ("oats", 0.25, "cup"),
    ], "Freeze zucchini already diced; a whole frozen one will not fit past the blade and you cannot cut it once it's solid."),

    ("kd-cloud-shake", "Cloud Shake", "kids", 2, 3, [
        ("white_beans", 0.25, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("almond_milk_vanilla", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Rinse the beans until the water runs clear — whatever bean flavor there is lives in the canning liquid."),

    ("kd-rocket-fuel", "Rocket Fuel", "kids", 2, 4, [
        ("sweet_potato", 0.5, "cup"),
        ("orange_juice", 0.75, "cup"),
        ("banana", 0.5, "piece"),
        ("cinnamon", 0.25, "tsp"),
    ], "Roast the sweet potato rather than boiling it, and chill it fully — warm purée makes a sad, thick drink."),

    # --- School mornings ---------------------------------------------------
    ("kd-school-bus-shake", "School Bus Shake", "kids", 2, 4, [
        ("mango_frozen", 0.75, "cup"),
        ("oats", 0.25, "cup"),
        ("milk_2", 0.75, "cup"),
        ("banana", 0.5, "piece"),
    ], "Buzz the oats with the milk for ten seconds before anything else goes in, so nobody finds a raw flake."),

    ("kd-running-late", "Running Late", "kids", 1, 3, [
        ("banana_frozen", 0.75, "cup"),
        ("oats", 0.25, "cup"),
        ("peanut_butter", 1, "tbsp"),
        ("milk_2", 0.75, "cup"),
        ("honey", 1, "tsp"),
    ], "Make it the night before and keep it in the fridge — it thickens, but a splash of milk and five seconds of BLEND brings it back."),

    ("kd-pancakes-in-a-straw", "Pancakes in a Straw", "kids", 2, 4, [
        ("pancake", 0.25, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("maple_syrup", 1, "tsp"),
    ], "This is what yesterday's leftover pancake is for; tear it up small so it soaks rather than spins."),

    ("kd-last-of-the-cornflakes", "Last of the Cornflakes", "kids", 2, 3, [
        ("cornflakes", 0.5, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("strawberry_jam", 1, "tsp"),
    ], "Let the flakes sit in the milk for a minute before blending — they go silky instead of gritty."),

    # --- Sick days and sore throats ---------------------------------------
    ("kd-pajama-day-pear", "Pajama Day Pear", "kids", 2, 5, [
        ("pear", 1, "piece"),
        ("chamomile_tea", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("ice", 0.25, "cup"),
    ], "Brew the chamomile and chill it right down first; lukewarm is the worst temperature for a sore throat."),

    ("kd-blanket-fort-peach", "Blanket Fort Peach", "kids", 2, 3, [
        ("peach_frozen", 1, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("honey", 1, "tsp"),
        ("lemon_juice", 1, "tsp"),
    ], None),

    ("kd-quiet-morning-melon", "Quiet Morning Melon", "kids", 2, 4, [
        ("honeydew", 1, "cup"),
        ("cucumber", 0.25, "piece"),
        ("water", 0.5, "cup"),
        ("ice", 0.5, "cup"),
    ], "Peel the cucumber for this one; the skin is where any bitterness hides and today is not the day."),

    ("kd-melted-popsicle", "Melted Popsicle", "kids", 2, 3, [
        ("watermelon_frozen", 1, "cup"),
        ("watermelon_juice", 0.5, "cup"),
        ("lime_juice", 1, "tsp"),
    ], None),

    ("kd-soft-voice-apple", "Soft Voice Apple", "kids", 2, 4, [
        ("applesauce", 0.5, "cup"),
        ("rooibos_tea", 0.75, "cup"),
        ("honey", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Rooibos is naturally caffeine-free and goes sweet as it cools, so brew it strong and chill it."),

    # --- Make it together --------------------------------------------------
    ("kd-confetti-cup", "Confetti Cup", "kids", 2, 3, [
        ("banana_frozen", 0.75, "cup"),
        ("yogurt_vanilla", 0.25, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("vanilla_extract", 0.5, "tsp"),
        ("sprinkles", 1, "tbsp"),
    ], "Blend it plain and let them stir the sprinkles in themselves — blended, sprinkles turn the whole cup a sad grey."),

    ("kd-pick-your-own", "Pick Your Own", "kids", 2, 3, [
        ("berries_mixed_frozen", 1, "cup"),
        ("milk_2", 0.75, "cup"),
        ("banana", 0.5, "piece"),
        ("honey", 1, "tsp"),
    ], None),

    ("kd-shake-it-up", "Shake It Up", "kids", 2, 4, [
        ("strawberry_frozen", 0.75, "cup"),
        ("pineapple_frozen", 0.5, "cup"),
        ("orange_juice", 0.75, "cup"),
    ], None),

    # --- Holidays ----------------------------------------------------------
    ("kd-candy-cane-swirl", "Candy Cane Swirl", "kids", 2, 4, [
        ("milk_whole", 0.75, "cup"),
        ("ice_cream", 0.5, "cup"),
        ("peppermint_extract", 0.25, "tsp"),
        ("strawberry_jam", 1, "tbsp"),
    ], "Peppermint extract is ferocious — a quarter teaspoon, measured, not a glug from the bottle."),

    ("kd-gingerbread-reindeer", "Gingerbread Reindeer", "kids", 2, 4, [
        ("molasses", 1, "tsp"),
        ("ginger_ground", 0.25, "tsp"),
        ("cinnamon", 0.5, "tsp"),
        ("banana_frozen", 0.75, "cup"),
        ("milk_2", 0.75, "cup"),
        ("oats", 0.25, "cup"),
    ], "Molasses is strong and bitter in quantity; one teaspoon reads as gingerbread, two reads as medicine."),

    ("kd-pumpkin-patch", "Pumpkin Patch", "kids", 2, 3, [
        ("pumpkin_puree", 0.5, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("pumpkin_spice", 0.5, "tsp"),
        ("maple_syrup", 1, "tsp"),
    ], "Check the can says pure pumpkin, not pie filling — the filling is already sweetened and spiced and throws the whole thing off."),

    ("kd-snowman-shake", "Snowman Shake", "kids", 2, 3, [
        ("banana_frozen", 1, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("coconut_shredded", 1, "tbsp"),
        ("vanilla_extract", 0.5, "tsp"),
    ], "Shredded coconut never fully disappears; if bits are a problem in your house, leave it out and add another splash of vanilla."),

    ("kd-love-bug", "Love Bug", "kids", 2, 4, [
        ("strawberry_frozen", 1, "cup"),
        ("white_chocolate", 1, "tbsp"),
        ("milk_whole", 0.75, "cup"),
        ("yogurt_vanilla", 0.25, "cup"),
    ], "Chop the white chocolate small or melt it into the milk first, or you'll get shards on the last sip."),

    ("kd-easter-basket", "Easter Basket", "kids", 2, 3, [
        ("blue_matcha", 0.25, "tsp"),
        ("banana_frozen", 0.75, "cup"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("honey", 1, "tsp"),
    ], None),

    # --- Everyday favorites -------------------------------------------------
    ("kd-fluffernutter-float", "Fluffernutter Float", "kids", 2, 3, [
        ("peanut_butter", 1, "tbsp"),
        ("marshmallow_fluff", 1, "tbsp"),
        ("banana_frozen", 0.75, "cup"),
        ("milk_whole", 0.75, "cup"),
    ], "Spoon the fluff onto the frozen banana rather than the cup wall — it sticks to cold fruit and slides off plastic."),

    ("kd-nut-free-lunchbox", "Nut-Free Lunchbox", "kids", 2, 3, [
        ("sunflower_butter", 1, "tbsp"),
        ("banana_frozen", 0.75, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("honey", 1, "tsp"),
    ], "Sunflower seed butter stands in for peanut butter one-for-one, which matters if the classroom is nut-free."),

    ("kd-apple-orchard-slush", "Apple Orchard Slush", "kids", 2, 3, [
        ("applesauce", 0.5, "cup"),
        ("apple_juice", 0.5, "cup"),
        ("ice", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], None),

    ("kd-grape-snowstorm", "Grape Snowstorm", "kids", 2, 3, [
        ("grape_frozen", 1, "cup"),
        ("white_grape_juice", 0.75, "cup"),
        ("banana", 0.5, "piece"),
    ], "Freeze seedless grapes loose on a tray first, otherwise they clump into one lump that jams the blade."),

    ("kd-cutie-pie-cream", "Cutie Pie Cream", "kids", 2, 5, [
        ("clementine", 2, "piece"),
        ("milk_2", 0.5, "cup"),
        ("ice_cream", 0.25, "cup"),
        ("ice", 0.5, "cup"),
    ], "Pull off every scrap of white pith — that's what turns citrus smoothies bitter as they sit."),

    ("kd-cherry-bomb", "Cherry Bomb", "kids", 2, 3, [
        ("cherry_frozen", 1, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("banana", 0.5, "piece"),
        ("vanilla_extract", 0.5, "tsp"),
    ], "Frozen dark cherries come pitted; fresh ones do not, and one missed pit will chip the blade."),

    ("kd-melon-ball", "Melon Ball", "kids", 2, 5, [
        ("cantaloupe", 1, "cup"),
        ("honeydew", 0.5, "cup"),
        ("lime_juice", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("kd-papaya-pup", "Papaya Pup", "kids", 2, 4, [
        ("papaya", 0.75, "cup"),
        ("orange_juice", 0.75, "cup"),
        ("banana", 0.5, "piece"),
        ("lime_juice", 1, "tsp"),
    ], "Scrape out every black seed — they're peppery and one is enough to ruin a whole cup."),

    ("kd-goodnight-milk", "Goodnight Milk", "kids", 1, 2, [
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("honey", 1, "tsp"),
        ("nutmeg", 0.25, "tsp"),
    ], None),

    ("kd-chocolate-chipmunk", "Chocolate Chipmunk", "kids", 2, 3, [
        ("choc_chips", 1, "tbsp"),
        ("banana_frozen", 0.75, "cup"),
        ("milk_2", 0.75, "cup"),
        ("peanut_butter", 1, "tbsp"),
    ], "Chocolate chips go in last and get two short BLEND pulses — you want freckles, not a uniform brown."),

    ("kd-muscle-monkey", "Muscle Monkey", "kids", 1, 3, [
        ("whey_chocolate", 1, "piece"),
        ("banana_frozen", 0.75, "cup"),
        ("milk_2", 0.75, "cup"),
        ("oats", 0.25, "cup"),
    ], "One scoop is plenty at this size; two makes it chalky and no amount of banana hides it."),

    ("kd-strawberry-sundae-cup", "Strawberry Sundae Cup", "kids", 2, 4, [
        ("strawberry_frozen", 1, "cup"),
        ("frozen_yogurt", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("sprinkles", 1, "tsp"),
    ], None),
]
