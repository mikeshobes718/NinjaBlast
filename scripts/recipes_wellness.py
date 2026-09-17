"""Blast wellness recipes — drinks built around a nutritional property: fibre, low sugar, electrolytes, seeds, greens and the supplement shelf."""

RECIPES = [
    # ------------------------------------------------------------ high fibre
    ("wl-pear-over-oats", "Pear Over Oats", "wellness", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("oats", 0.25, "cup"),
        ("chia", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
    ], "Add the chia last and give it two minutes before you blend, or it clumps on the blade."),

    ("wl-cocoa-and-prune", "Cocoa and Prune", "wellness", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("prune", 4, "piece"),
        ("cacao_powder", 1, "tbsp"),
        ("flax", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Prunes and cocoa are both dark and slightly bitter, so they hide each other — this tastes far more like chocolate than like prunes."),

    ("wl-spoon-thick-berry", "Spoon-Thick Berry", "wellness", 1, 3, [
        ("water", 1, "cup"),
        ("berries_mixed_frozen", 1, "cup"),
        ("psyllium", 1, "tsp"),
        ("lemon_juice", 1, "tbsp"),
    ], "Psyllium keeps thickening in the cup, so drink this within five minutes or you'll be eating it with a spoon."),

    ("wl-fig-and-bran", "Fig and Bran", "wellness", 1, 4, [
        ("soy_milk", 0.75, "cup"),
        ("fig_dried", 3, "piece"),
        ("oat_bran", 0.25, "cup"),
        ("cardamom", 0.25, "tsp"),
    ], "Snip the stems off the dried figs first — they never break down and you'll find them in the last mouthful."),

    ("wl-raspberry-rough-and-cold", "Raspberry Rough and Cold", "wellness", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("raspberry_frozen", 1, "cup"),
        ("flax", 1.5, "tbsp"),
    ], None),

    ("wl-blackberry-seeds-and-all", "Blackberry Seeds and All", "wellness", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("blackberry_frozen", 1, "cup"),
        ("chia", 1.5, "tbsp"),
        ("allulose", 1, "tsp"),
    ], "Allulose instead of honey keeps the sugar down without the cooling aftertaste erythritol leaves."),

    ("wl-four-oclock-filler", "Four O'Clock Filler", "wellness", 1, 2, [
        ("water", 1, "cup"),
        ("fiber_powder", 1, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Soluble fibre powder goes cloudy but shouldn't go lumpy — pour it onto the water before the ice, not after."),

    # -------------------------------------------------------- very low sugar
    ("wl-cold-cucumber-line", "Cold Cucumber Line", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("cucumber", 1, "piece"),
        ("celery", 1, "piece"),
        ("dill", 1, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Leave the cucumber skin on for colour, but peel it if it's a thick-skinned waxed one — that skin turns bitter under the blade."),

    ("wl-fennel-and-ice", "Fennel and Ice", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("fennel", 0.5, "cup"),
        ("cucumber", 0.5, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Use the white bulb only and slice it thin across the grain; the stalks are all string."),

    ("wl-tomato-cold-and-salted", "Tomato, Cold and Salted", "wellness", 1, 4, [
        ("tomato_juice", 0.75, "cup"),
        ("cherry_tomato", 6, "piece"),
        ("basil", 2, "tbsp"),
        ("olive_oil", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "The olive oil isn't optional — without a little fat the tomato tastes thin and metallic."),

    ("wl-avocado-no-sugar", "Avocado, No Sugar", "wellness", 1, 4, [
        ("almond_milk", 1, "cup"),
        ("avocado", 0.5, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("mint", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-cauliflower-cocoa", "Cauliflower Cocoa", "wellness", 1, 3, [
        ("cashew_milk", 0.75, "cup"),
        ("cauliflower_frozen", 0.75, "cup"),
        ("cacao_powder", 1.5, "tbsp"),
        ("almond_butter", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Frozen riced cauliflower is flavourless and gives you milkshake thickness for almost no sugar — but it has to be frozen, not fresh."),

    ("wl-jicama-lime-ice", "Jicama Lime Ice", "wellness", 1, 6, [
        ("water", 0.75, "cup"),
        ("jicama", 0.75, "cup"),
        ("lime_juice", 1.5, "tbsp"),
        ("tajin", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Jicama is fibrous, so cut it into half-inch cubes rather than sticks or the blade just pushes them around."),

    # ------------------------------------------ low calorie, real volume
    ("wl-a-lot-of-cold-watermelon", "A Lot of Cold Watermelon", "wellness", 1, 3, [
        ("watermelon_frozen", 1.5, "cup"),
        ("water", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("mint", 1, "tbsp"),
    ], "Freeze watermelon cubes on a tray, not in a bag, or they weld into one block you can't get into the cup."),

    ("wl-savoury-cucumber-cup", "Savoury Cucumber Cup", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("cucumber", 1, "piece"),
        ("greek_yogurt_nonfat", 0.5, "cup"),
        ("dill", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-a-pint-of-strawberry", "A Pint of Strawberry", "wellness", 1, 3, [
        ("water", 0.75, "cup"),
        ("strawberry_frozen", 1.25, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("stevia", 0.25, "tsp"),
    ], "Stevia goes bitter if you overshoot, so measure it rather than shaking it in."),

    ("wl-cold-pumpkin-cup", "Cold Pumpkin Cup", "wellness", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("pumpkin_puree", 0.5, "cup"),
        ("pumpkin_spice", 0.5, "tsp"),
        ("allulose", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Check the can says pumpkin puree and not pie filling — the filling is already loaded with sugar."),

    # -------------------------------------------- electrolytes and hydration
    ("wl-after-the-heat", "After the Heat", "wellness", 1, 2, [
        ("coconut_water", 1, "cup"),
        ("lime_juice", 1.5, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "A quarter teaspoon of salt in coconut water disappears completely — you read it as the lime tasting rounder."),

    ("wl-watermelon-and-salt", "Watermelon and Salt", "wellness", 1, 4, [
        ("watermelon", 1.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-orange-freeze-hot-day", "Orange Freeze for a Hot Day", "wellness", 1, 4, [
        ("water", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("electrolyte_powder", 1, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("wl-cactus-water-cooler", "Cactus Water Cooler", "wellness", 1, 4, [
        ("cactus_water", 1, "cup"),
        ("cucumber", 0.5, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("wl-long-run-maple", "Long Run Maple", "wellness", 1, 3, [
        ("maple_water", 1, "cup"),
        ("banana", 0.5, "piece"),
        ("salt", 0.25, "tsp"),
        ("lemon_juice", 1, "tbsp"),
    ], None),

    ("wl-salted-pineapple-cooler", "Salted Pineapple Cooler", "wellness", 1, 3, [
        ("coconut_water", 0.75, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("salt", 0.25, "tsp"),
        ("lime_juice", 1, "tbsp"),
    ], "Salt on pineapple is a street-cart trick — it makes the fruit taste sweeter without adding sugar."),

    # ------------------------------------ iron- and folate-rich greens + vit C
    ("wl-spinach-meets-citrus", "Spinach Meets Citrus", "wellness", 1, 3, [
        ("orange_juice", 0.75, "cup"),
        ("spinach", 1.5, "cup"),
        ("strawberry_frozen", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
    ], "Vitamin C genuinely improves how much of the iron in leaves your body takes up, so keep the citrus and the spinach in the same glass rather than the same day."),

    ("wl-beet-greens-and-grapefruit", "Beet Greens and Grapefruit", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("beet_greens", 1, "cup"),
        ("grapefruit", 0.5, "piece"),
        ("honey", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Beet greens are the part people bin — strip them off the stems and they blend softer than kale."),

    ("wl-chard-and-kiwi", "Chard and Kiwi", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("chard", 1, "cup"),
        ("kiwi", 2, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Tear the chard leaf away from the coloured rib; the rib is where the earthy, slightly salty taste lives."),

    ("wl-watercress-and-clementine", "Watercress and Clementine", "wellness", 1, 4, [
        ("water", 0.75, "cup"),
        ("watercress", 1, "cup"),
        ("clementine", 2, "piece"),
        ("hemp_hearts", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Watercress is peppery in a horseradish way — start with half a cup if you've never blended it."),

    ("wl-kale-pepper-lime", "Kale, Pepper and Lime", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("kale", 1, "cup"),
        ("bell_pepper", 0.5, "piece"),
        ("lime_juice", 1.5, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Raw red pepper carries more vitamin C than an orange does, and its sweetness sits under the kale instead of fighting it."),

    # --------------------------------------------------- calcium without dairy
    ("wl-tahini-and-date", "Tahini and Date", "wellness", 1, 3, [
        ("soy_milk", 1, "cup"),
        ("tahini", 1.5, "tbsp"),
        ("date", 2, "piece"),
        ("cinnamon", 0.25, "tsp"),
    ], "Stir the tahini jar right down to the bottom first — the solids at the base are where the flavour is."),

    ("wl-collards-and-almond", "Collards and Almond", "wellness", 1, 5, [
        ("almond_milk", 1, "cup"),
        ("collard", 1, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("almond_butter", 1, "tbsp"),
    ], "Collards are tougher than spinach, so run BLEND twice with a shake in between rather than once for longer."),

    ("wl-orange-chia-cold-cup", "Orange Chia Cold Cup", "wellness", 1, 4, [
        ("soy_milk_vanilla", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("chia", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Buy the fortified soy milk if you're drinking this for the calcium — unfortified plant milks have almost none."),

    ("wl-fig-almond-sesame", "Fig, Almond, Sesame", "wellness", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("fig_dried", 3, "piece"),
        ("sesame_seeds", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Toast the sesame in a dry pan for a minute before it goes in and the whole drink turns nutty instead of raw."),

    ("wl-bok-choy-and-pear", "Bok Choy and Pear", "wellness", 1, 5, [
        ("pea_milk", 0.75, "cup"),
        ("bok_choy", 1, "cup"),
        ("pear", 1, "piece"),
        ("ginger", 1, "tsp"),
    ], "Use the pale stems as well as the leaves — they're crisp and watery and blend almost to nothing."),

    # ---------------------------------------------------------- omega-3 seeds
    ("wl-walnut-and-black-currant", "Walnut and Black Currant", "wellness", 1, 3, [
        ("flax_milk", 0.75, "cup"),
        ("blackcurrant", 0.75, "cup"),
        ("walnuts", 1.5, "tbsp"),
        ("maple_syrup", 1, "tsp"),
    ], "Black currants are properly sour; if yours are frozen and unsweetened you'll want the full teaspoon of maple."),

    ("wl-hemp-and-cacao", "Hemp and Cacao", "wellness", 1, 3, [
        ("hemp_milk", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("hemp_hearts", 2, "tbsp"),
        ("cacao_nibs", 1, "tbsp"),
    ], "Nibs stay crunchy no matter how long you blend — add them at the end if you want the texture, at the start if you don't."),

    ("wl-flax-oil-blueberry", "Flax Oil Blueberry", "wellness", 1, 2, [
        ("almond_milk", 0.75, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("flax_oil", 1, "tsp"),
        ("vanilla_extract", 0.5, "tsp"),
    ], "Keep flaxseed oil in the fridge and never near heat — it goes rancid and fishy faster than any other oil on the shelf."),

    ("wl-sacha-inchi-cold-cup", "Sacha Inchi Cold Cup", "wellness", 1, 3, [
        ("cashew_milk", 0.75, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("sacha_inchi", 1.5, "tbsp"),
        ("lime_zest", 0.5, "tsp"),
    ], None),

    ("wl-pear-in-walnut-oil", "Pear in Walnut Oil", "wellness", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("walnut_oil", 1, "tsp"),
        ("cinnamon", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    # ------------------------------------------------ beet and nitrate builds
    ("wl-twenty-minutes-before", "Twenty Minutes Before", "wellness", 1, 3, [
        ("beet_juice", 0.75, "cup"),
        ("cherry_frozen", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-beet-and-blood-orange", "Beet and Blood Orange", "wellness", 1, 5, [
        ("beet_juice", 0.5, "cup"),
        ("blood_orange", 1, "piece"),
        ("water", 0.25, "cup"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-warm-up-cup", "Warm-Up Cup", "wellness", 1, 2, [
        ("water", 0.75, "cup"),
        ("pomegranate_juice", 0.5, "cup"),
        ("beet_powder", 1, "tsp"),
        ("creatine", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Creatine never fully dissolves — drink it straight away and rinse the cup, or you'll find grit welded to the bottom."),

    ("wl-arugula-and-beet", "Arugula and Beet", "wellness", 1, 5, [
        ("water", 0.75, "cup"),
        ("arugula", 1, "cup"),
        ("beet", 0.5, "cup"),
        ("apple", 0.5, "piece"),
        ("lemon_juice", 1, "tbsp"),
    ], "Use pre-cooked vacuum-packed beets; raw beet never breaks down properly in a single-serve cup."),

    # ---------------------------------- gentle, bland, cold, no appetite
    ("wl-when-nothing-sounds-good", "When Nothing Sounds Good", "wellness", 1, 2, [
        ("rice_milk", 1, "cup"),
        ("banana", 1, "piece"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-cold-apple-and-chamomile", "Cold Apple and Chamomile", "wellness", 1, 3, [
        ("chamomile_tea", 0.75, "cup"),
        ("applesauce", 0.5, "cup"),
        ("honey", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Brew the chamomile double strength and chill it first; hot tea poured over ice just gives you weak tea."),

    ("wl-honeydew-very-cold", "Honeydew, Very Cold", "wellness", 1, 3, [
        ("water", 0.5, "cup"),
        ("honeydew", 1.25, "cup"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-cold-broth-cup", "Cold Broth Cup", "wellness", 1, 4, [
        ("broth_veg", 1, "cup"),
        ("silken_tofu", 0.5, "cup"),
        ("miso", 1, "tsp"),
        ("scallion", 1, "piece"),
    ], "Miso goes harsh if you cook it, so this stays cold on purpose — silken tofu makes it thick enough to feel like food."),

    ("wl-flat-ginger-ale-and-pear", "Flat Ginger Ale and Pear", "wellness", 1, 3, [
        ("ginger_ale", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("ice", 0.5, "cup"),
    ], "Let the ginger ale go flat in an open glass first — carbonation in a sealed blending cup builds pressure you don't want."),

    # ------------------------------------------------------ warming spice
    ("wl-turmeric-with-the-pepper-in", "Turmeric with the Pepper In", "wellness", 1, 4, [
        ("coconut_milk_bev", 1, "cup"),
        ("turmeric_fresh", 1, "tsp"),
        ("black_pepper", 0.25, "tsp"),
        ("honey", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Turmeric on its own is bitter and dusty; the pepper and the coconut fat are what turn it into something you'd finish."),

    ("wl-sharp-ginger-cold-cup", "Sharp Ginger Cold Cup", "wellness", 1, 4, [
        ("water", 0.75, "cup"),
        ("ginger", 1, "tbsp"),
        ("lemon", 0.5, "piece"),
        ("honey", 1, "tsp"),
        ("cayenne", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Scrape ginger skin off with the edge of a teaspoon rather than peeling it — you lose far less of the root."),

    ("wl-cardamom-oat-chai", "Cardamom Oat Chai", "wellness", 1, 3, [
        ("chai_concentrate", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("oats", 2, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Extra cardamom on top of a chai concentrate is what stops it tasting like a syrup — most concentrates are heavy on cinnamon and light on everything else."),

    ("wl-cinnamon-sweet-potato", "Cinnamon Sweet Potato", "wellness", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("sweet_potato", 0.5, "cup"),
        ("date", 2, "piece"),
        ("cinnamon", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Roast the sweet potato rather than boiling it — boiled, it goes watery and the drink tastes of nothing."),

    ("wl-carrot-with-garam-masala", "Carrot with Garam Masala", "wellness", 1, 4, [
        ("carrot_juice", 0.75, "cup"),
        ("carrot", 1, "piece"),
        ("coconut_milk_light", 0.25, "cup"),
        ("garam_masala", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Garam masala is a finishing spice, so half a teaspoon is plenty — any more and it tastes like uncooked curry powder."),

    # ------------------------------------- gentle builds for touchy stomachs
    ("wl-easy-blueberry", "Easy Blueberry", "wellness", 1, 3, [
        ("milk_lactose_free", 0.75, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("peanut_butter", 1, "tbsp"),
        ("maple_syrup", 1, "tsp"),
    ], None),

    ("wl-quiet-strawberry-oat", "Quiet Strawberry Oat", "wellness", 1, 3, [
        ("rice_milk", 0.75, "cup"),
        ("strawberry_frozen", 0.75, "cup"),
        ("oats", 2, "tbsp"),
        ("vanilla_extract", 0.5, "tsp"),
    ], None),

    ("wl-kiwi-ginger-nothing-else", "Kiwi, Ginger, Nothing Else", "wellness", 1, 4, [
        ("water", 0.75, "cup"),
        ("kiwi", 2, "piece"),
        ("ginger", 1, "tsp"),
        ("allulose", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Blend kiwi seeds briefly — hammer them and they release a bitterness that wasn't there a moment ago."),

    # ------------------------------------------- the supplement shelf, sensibly
    ("wl-greens-powder-made-drinkable", "Greens Powder, Made Drinkable", "wellness", 1, 3, [
        ("pineapple_juice", 0.5, "cup"),
        ("water", 0.25, "cup"),
        ("greens_powder", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Greens powder tastes like a lawn in water — pineapple's acid and the banana's sweetness are what make it drinkable."),

    ("wl-blue-green-mango", "Blue-Green Mango", "wellness", 1, 3, [
        ("coconut_water", 0.75, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("spirulina", 0.5, "tsp"),
        ("lime_juice", 1, "tbsp"),
    ], "Half a teaspoon of spirulina colours the whole cup; a full one and you'll taste pond."),

    ("wl-sea-moss-and-mango", "Sea Moss and Mango", "wellness", 1, 3, [
        ("coconut_milk_bev", 0.75, "cup"),
        ("mango_frozen", 0.5, "cup"),
        ("sea_moss", 1, "tbsp"),
        ("honey", 1, "tsp"),
    ], "Sea moss gel is essentially a thickener — leave this standing twenty minutes and it sets into a loose pudding."),

    ("wl-maca-malt", "Maca Malt", "wellness", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("maca", 1, "tsp"),
        ("cacao_powder", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Maca is malty and slightly bitter, closer to Ovaltine than to vanilla — start at a teaspoon and work up."),

    ("wl-ashwagandha-and-date", "Ashwagandha and Date", "wellness", 1, 3, [
        ("almond_milk", 1, "cup"),
        ("ashwagandha", 0.5, "tsp"),
        ("date", 2, "piece"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Ashwagandha tastes bitter and faintly horsey on its own; dates and cardamom are the cheapest way to cover it."),

    ("wl-reishi-cacao", "Reishi Cacao", "wellness", 1, 3, [
        ("cashew_milk", 0.75, "cup"),
        ("reishi", 0.5, "tsp"),
        ("dutch_cocoa", 1, "tbsp"),
        ("date_syrup", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Reishi is properly bitter, so pair it with Dutch-process cocoa rather than natural — the Dutch stuff is mellower and meets it halfway."),

    ("wl-lions-mane-cold-brew", "Lion's Mane Cold Brew", "wellness", 1, 2, [
        ("cold_brew", 0.25, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("lions_mane", 1, "tsp"),
        ("maple_syrup", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("wl-baobab-sour", "Baobab Sour", "wellness", 1, 3, [
        ("water", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("baobab", 1, "tbsp"),
        ("camu_camu", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("wl-collagen-in-the-cold-brew", "Collagen in the Cold Brew", "wellness", 1, 2, [
        ("cold_brew", 0.25, "cup"),
        ("milk_lactose_free", 0.75, "cup"),
        ("collagen", 1, "piece"),
        ("cinnamon", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Collagen peptides are flavourless but they foam — blend on the short side and let the head settle before you drink."),

    ("wl-moringa-and-pear", "Moringa and Pear", "wellness", 1, 4, [
        ("water", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("moringa", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),
]
