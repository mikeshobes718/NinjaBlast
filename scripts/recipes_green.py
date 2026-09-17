"""Green blends for the Blast — leafy, herbal and savoury drinks that earn the colour."""

RECIPES = [

    # ---------------------------------------------- gentle first-green builds
    ("gr-training-wheels", "Training Wheels", "green", 1, 3, [
        ("romaine", 1, "cup"),
        ("pineapple_frozen", 1, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Romaine is the mildest thing in the crisper drawer — it gives you the colour and almost none of the flavour, which is the whole point on day one."),

    ("gr-soft-landing", "Soft Landing", "green", 1, 3, [
        ("butter_lettuce", 1, "cup"),
        ("pear", 1, "piece"),
        ("white_grape_juice", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Use a pear that gives under your thumb; a hard one tastes like nothing and leaves grit on the blade."),

    ("gr-quiet-green", "Quiet Green", "green", 1, 3, [
        ("spinach_frozen", 0.5, "cup"),
        ("mango_frozen", 1, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Frozen spinach blends smoother and tastes noticeably milder than fresh — the freezing softens the leaf so there are no green flecks and no raw edge."),

    ("gr-melon-patch", "Melon Patch", "green", 1, 4, [
        ("mixed_greens", 1, "cup"),
        ("honeydew", 1, "cup"),
        ("cucumber", 0.5, "piece"),
        ("coconut_water", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    # ---------------------------------------------- spinach, fresh
    ("gr-monsoon-green", "Monsoon Green", "green", 1, 4, [
        ("spinach", 1.5, "cup"),
        ("mango", 1, "piece"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "The salt is not seasoning, it is a bitterness switch — leave it out once and you will taste the leaf immediately."),

    ("gr-cardamom-halva", "Cardamom Halva", "green", 1, 4, [
        ("spinach", 1.5, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("tahini", 1, "tbsp"),
        ("date", 2, "piece"),
        ("cardamom", 0.25, "tsp"),
    ], "Tear the dates and drop them in first so they sit against the blade; whole pitted dates tend to ride the top of the cup."),

    ("gr-cassis-leaf", "Cassis Leaf", "green", 1, 3, [
        ("spinach", 1.5, "cup"),
        ("blackcurrant", 0.5, "cup"),
        ("apple_juice", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Black currants are tart enough to carry the spinach on their own — taste before you reach for anything sweet."),

    ("gr-green-velvet", "Green Velvet", "green", 1, 3, [
        ("spinach", 1.5, "cup"),
        ("avocado", 0.5, "piece"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "No sweetener at all here, so the lime is doing the work — two tablespoons sounds like a lot and is exactly right."),

    ("gr-carrot-top", "Carrot Top", "green", 1, 4, [
        ("spinach", 1.5, "cup"),
        ("carrot_juice", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    # ---------------------------------------------- spinach, frozen
    ("gr-green-truffle", "Green Truffle", "green", 1, 3, [
        ("spinach_frozen", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Cacao hides frozen spinach completely — this is the one to hand someone who insists they can taste greens anywhere."),

    ("gr-frost-line", "Frost Line", "green", 1, 3, [
        ("spinach_frozen", 0.5, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("water", 0.75, "cup"),
        ("mint", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
    ], None),

    # ---------------------------------------------- kale
    ("gr-kale-outvoted", "Kale Outvoted", "green", 1, 5, [
        ("kale", 1.5, "cup"),
        ("pineapple_frozen", 1, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Strip the leaves off the ribs before they go in — the ribs are where the bitterness and the stringiness both live."),

    ("gr-stalk-market", "Stalk Market", "green", 1, 5, [
        ("kale", 1, "cup"),
        ("celery", 1, "piece"),
        ("apple_green", 1, "piece"),
        ("parsley", 2, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("water", 0.75, "cup"),
    ], None),

    ("gr-sesame-grove", "Sesame Grove", "green", 1, 4, [
        ("kale", 1.5, "cup"),
        ("almond_milk", 0.75, "cup"),
        ("tahini", 1, "tbsp"),
        ("orange", 1, "piece"),
        ("date", 1, "piece"),
    ], "Tahini fat coats the tongue and blunts kale's edge — it does more for the drink than another spoon of sweetener would."),

    ("gr-miso-verde", "Miso Verde", "green", 1, 5, [
        ("kale", 1, "cup"),
        ("broth_veg", 0.75, "cup"),
        ("avocado", 0.5, "piece"),
        ("miso", 1, "tsp"),
        ("scallion", 1, "piece"),
        ("lime_juice", 1, "tbsp"),
    ], "Savoury and meant to be drunk cold; if the broth is fridge-cold the miso needs a second longer to disperse."),

    # ---------------------------------------------- kale, frozen
    ("gr-kerala-green", "Kerala Green", "green", 1, 3, [
        ("kale_frozen", 0.5, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("coconut_milk_light", 0.75, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("honey", 1, "tsp"),
    ], "Frozen kale is milder and far smoother than fresh — no fibrous bits, so you can use it in a drink this creamy without straining."),

    ("gr-forest-floor", "Forest Floor", "green", 1, 3, [
        ("kale_frozen", 0.5, "cup"),
        ("cherry_frozen", 0.75, "cup"),
        ("almond_milk", 0.75, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Dark cherry and cacao want salt the way caramel does; without it the drink tastes flat and slightly chalky."),

    # ---------------------------------------------- baby kale
    ("gr-orchard-green", "Orchard Green", "green", 1, 4, [
        ("baby_kale", 1.5, "cup"),
        ("peach_frozen", 0.75, "cup"),
        ("skyr", 0.5, "cup"),
        ("milk_lactose_free", 0.5, "cup"),
        ("honey", 1, "tsp"),
    ], "Baby kale is tender enough to skip the stem-stripping you would do with the mature leaf."),

    ("gr-bramble-patch", "Bramble Patch", "green", 1, 3, [
        ("baby_kale", 1.5, "cup"),
        ("blackberry_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("mint", 2, "tbsp"),
    ], None),

    ("gr-pistachio-grove", "Pistachio Grove", "green", 1, 4, [
        ("baby_kale", 1.5, "cup"),
        ("pear", 1, "piece"),
        ("pistachio_milk", 0.75, "cup"),
        ("pistachio_butter", 1, "tbsp"),
        ("whey_vanilla", 1, "piece"),
    ], "Pistachio butter is thick and sticky — spoon it on top of the liquid, not onto the dry blade, or it welds itself to the bottom."),

    # ---------------------------------------------- arugula
    ("gr-peppered-grapefruit", "Peppered Grapefruit", "green", 1, 4, [
        ("arugula", 1, "cup"),
        ("grapefruit", 0.5, "piece"),
        ("water", 0.5, "cup"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("gr-rocket-science", "Rocket Science", "green", 1, 4, [
        ("arugula", 1, "cup"),
        ("spinach", 0.5, "cup"),
        ("apple_green", 1, "piece"),
        ("hemp_hearts", 2, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("water", 0.75, "cup"),
    ], None),

    ("gr-peppery-vine", "Peppery Vine", "green", 1, 5, [
        ("arugula", 1, "cup"),
        ("tomato", 1, "piece"),
        ("water", 0.75, "cup"),
        ("olive_oil", 1, "tbsp"),
        ("balsamic", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Drink this the way you would a cold soup; a ripe room-temperature tomato beats a cold one every time."),

    # ---------------------------------------------- watercress
    ("gr-clear-creek", "Clear Creek", "green", 1, 4, [
        ("watercress", 1, "cup"),
        ("cucumber", 0.5, "piece"),
        ("apple_green", 1, "piece"),
        ("water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Watercress is mustardy and loud — one cup is the ceiling unless you want it to taste like horseradish."),

    ("gr-anisette-cooler", "Anisette Cooler", "green", 1, 5, [
        ("watercress", 1, "cup"),
        ("fennel", 0.5, "cup"),
        ("orange", 1, "piece"),
        ("water", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Slice the fennel thin across the grain; in chunks it stays crunchy no matter how long you run the blade."),

    ("gr-cold-cress", "Cold Cress", "green", 1, 4, [
        ("watercress", 1.5, "cup"),
        ("buttermilk", 0.75, "cup"),
        ("cucumber", 0.5, "piece"),
        ("dill", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("black_pepper", 0.25, "tsp"),
    ], "Buttermilk's acid tames the cress the way a vinaigrette tames a salad — plain milk here is dull."),

    # ---------------------------------------------- romaine
    ("gr-vineyard-cool", "Vineyard Cool", "green", 1, 3, [
        ("romaine", 1.5, "cup"),
        ("grape_frozen", 1, "cup"),
        ("water", 0.5, "cup"),
        ("mint", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
    ], "Frozen grapes are sweet enough that this needs no sweetener and cold enough that it needs no ice."),

    ("gr-summer-bench", "Summer Bench", "green", 1, 3, [
        ("romaine", 1.5, "cup"),
        ("watermelon_frozen", 1, "cup"),
        ("water", 0.5, "cup"),
        ("basil", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Salted watermelon is a street-cart trick and it works just as well blended."),

    # ---------------------------------------------- butter lettuce
    ("gr-evening-garden", "Evening Garden", "green", 1, 4, [
        ("butter_lettuce", 1.5, "cup"),
        ("chamomile_tea", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("honey", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Brew the chamomile strong and chill it first; hot tea poured into the cup will melt the ice before the blade moves."),

    ("gr-rose-garden", "Rose Garden", "green", 1, 3, [
        ("butter_lettuce", 1.5, "cup"),
        ("strawberry_frozen", 0.75, "cup"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("rose_water", 0.5, "tsp"),
        ("honey", 1, "tsp"),
    ], "Rose water goes from floral to soapy in about a quarter teaspoon, so measure it rather than pouring."),

    # ---------------------------------------------- chard
    ("gr-stained-glass", "Stained Glass", "green", 1, 4, [
        ("chard", 1.5, "cup"),
        ("carrot_juice", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Rainbow chard stems will tint the drink pink or orange — use the white-stemmed bunch if you want it to stay green."),

    ("gr-tuscan-green", "Tuscan Green", "green", 1, 4, [
        ("chard", 1.5, "cup"),
        ("apple_green", 1, "piece"),
        ("water", 0.75, "cup"),
        ("olive_oil", 1, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("gr-chard-ribollita", "Chard Ribollita", "green", 1, 6, [
        ("chard", 1, "cup"),
        ("white_beans", 0.5, "cup"),
        ("broth_veg", 0.75, "cup"),
        ("olive_oil", 1, "tbsp"),
        ("rosemary", 1, "tsp"),
        ("black_pepper", 0.25, "tsp"),
    ], None),

    # ---------------------------------------------- collard
    ("gr-sunday-greens", "Sunday Greens", "green", 1, 5, [
        ("collard", 1, "cup"),
        ("pineapple_frozen", 1, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("cayenne", 0.25, "tsp"),
    ], "Collard is the toughest leaf on the list — chop it small before it goes in, or the blade just spins it around."),

    ("gr-callaloo-cooler", "Callaloo Cooler", "green", 1, 5, [
        ("collard", 1, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("coconut_milk_light", 0.75, "cup"),
        ("ginger", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
    ], None),

    ("gr-pot-likker", "Pot Likker", "green", 1, 5, [
        ("collard", 1, "cup"),
        ("tomato_juice", 0.75, "cup"),
        ("celery", 1, "piece"),
        ("cider_vinegar", 1, "tsp"),
        ("smoked_paprika", 0.25, "tsp"),
        ("hot_sauce", 1, "tsp"),
    ], "The splash of vinegar is what makes this taste like greens off the stove rather than a salad in a cup."),

    # ---------------------------------------------- bok choy
    ("gr-hanoi-pear", "Hanoi Pear", "green", 1, 5, [
        ("bok_choy", 1, "cup"),
        ("pear", 1, "piece"),
        ("coconut_water", 0.75, "cup"),
        ("lemongrass", 1, "tbsp"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Use only the pale bottom third of the lemongrass stalk and smash it flat first — the upper stalk is woody and never breaks down."),

    ("gr-cold-sesame-green", "Cold Sesame Green", "green", 1, 4, [
        ("bok_choy", 1, "cup"),
        ("apple_green", 1, "piece"),
        ("water", 0.75, "cup"),
        ("rice_vinegar", 1, "tsp"),
        ("sesame_oil", 0.5, "tsp"),
        ("ginger", 1, "tsp"),
    ], "Toasted sesame oil is strong enough that half a teaspoon flavours the whole cup; a tablespoon would taste like salad dressing."),

    ("gr-night-market", "Night Market", "green", 1, 4, [
        ("bok_choy", 1, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("mint", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
    ], None),

    # ---------------------------------------------- dandelion
    ("gr-roots-and-rind", "Roots and Rind", "green", 1, 4, [
        ("dandelion", 1, "cup"),
        ("orange", 1, "piece"),
        ("water", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Dandelion is genuinely bitter, so this one needs both the sweet and the citrus — pulling either makes it hard going."),

    ("gr-roadside-green", "Roadside Green", "green", 1, 4, [
        ("dandelion", 1, "cup"),
        ("apple_green", 1, "piece"),
        ("apple_juice", 0.75, "cup"),
        ("maple_syrup", 2, "tsp"),
        ("lemon_juice", 1, "tbsp"),
    ], "Young dandelion leaves are far gentler than the big ragged ones; pick the small pale ones if you get the choice."),

    ("gr-garden-bitters", "Garden Bitters", "green", 1, 4, [
        ("dandelion", 1, "cup"),
        ("grapefruit", 0.5, "piece"),
        ("tonic_water", 0.75, "cup"),
        ("agave", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    # ---------------------------------------------- beet greens
    ("gr-crimson-stem", "Crimson Stem", "green", 1, 4, [
        ("beet_greens", 1.5, "cup"),
        ("raspberry_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("collagen", 1, "piece"),
        ("lime_juice", 1, "tbsp"),
    ], "Beet tops taste like mild chard with an earthy note, and raspberry covers that note exactly."),

    ("gr-dacha-green", "Dacha Green", "green", 1, 5, [
        ("beet_greens", 1, "cup"),
        ("carrot_juice", 0.75, "cup"),
        ("apple_green", 1, "piece"),
        ("dill", 1, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    # ---------------------------------------------- mixed greens
    ("gr-salad-days", "Salad Days", "green", 1, 4, [
        ("mixed_greens", 1.5, "cup"),
        ("pear", 1, "piece"),
        ("cottage_cheese", 0.5, "cup"),
        ("milk_lactose_free", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Cottage cheese blends to a clean creaminess if you give it a full thirty seconds — stop early and you get lumps."),

    # ---------------------------------------------- sprouts
    ("gr-sandwich-shop", "Sandwich Shop", "green", 1, 4, [
        ("sprouts", 1, "cup"),
        ("avocado", 0.5, "piece"),
        ("kefir", 0.75, "cup"),
        ("cucumber", 0.5, "piece"),
        ("dill", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Alfalfa sprouts tangle around the blade in a clump — scatter them over the liquid rather than dropping the whole handful in."),

    ("gr-clean-slate", "Clean Slate", "green", 1, 4, [
        ("sprouts", 1, "cup"),
        ("apple_green", 1, "piece"),
        ("celery", 1, "piece"),
        ("water", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    # ---------------------------------------------- broccoli sprouts
    ("gr-sharp-start", "Sharp Start", "green", 1, 3, [
        ("broccoli_sprouts", 0.5, "cup"),
        ("spinach", 1, "cup"),
        ("apple_green", 1, "piece"),
        ("coconut_water", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
    ], "Broccoli sprouts are peppery in a radish way — half a cup is plenty against one apple's worth of sweetness."),

    ("gr-green-spark", "Green Spark", "green", 1, 4, [
        ("broccoli_sprouts", 0.5, "cup"),
        ("kiwi", 2, "piece"),
        ("cucumber", 0.5, "piece"),
        ("water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Blend kiwi seeds briefly or not at all — run it too long and the crushed seeds turn the drink faintly bitter."),

    # ---------------------------------------------- microgreens
    ("gr-cold-labneh-green", "Cold Labneh Green", "green", 1, 4, [
        ("microgreens", 1, "cup"),
        ("labneh", 0.5, "cup"),
        ("cucumber", 0.5, "piece"),
        ("water", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Labneh is thick enough to stall the blade on its own, which is why the water goes in first and the labneh on top."),

    ("gr-little-leaf-tropical", "Little Leaf Tropical", "green", 1, 3, [
        ("microgreens", 1, "cup"),
        ("passionfruit", 2, "piece"),
        ("pineapple_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
    ], "Microgreens are far more delicate than the full-grown leaf, so add them last and keep the blend short."),

    # ---------------------------------------------- wheatgrass
    ("gr-first-cut", "First Cut", "green", 1, 4, [
        ("wheatgrass", 0.25, "cup"),
        ("orange", 1, "piece"),
        ("apple_juice", 0.5, "cup"),
        ("ginger", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "A quarter cup of wheatgrass is the whole dose — it tastes like a mown lawn at any more than that, and citrus is the only thing that covers it."),

    ("gr-green-field", "Green Field", "green", 1, 4, [
        ("wheatgrass", 0.25, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("mint", 1, "tbsp"),
        ("lime_juice", 1, "tbsp"),
    ], None),

    # ---------------------------------------------- herb-led
    ("gr-agua-verde", "Agua Verde", "green", 1, 5, [
        ("romaine", 1, "cup"),
        ("pineapple", 1, "cup"),
        ("cilantro", 3, "tbsp"),
        ("jalapeno", 0.5, "piece"),
        ("water", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
    ], "Seed the jalapeño unless you want real heat; the pith carries most of it, not the flesh."),

    ("gr-peppery-basil-cooler", "Peppery Basil Cooler", "green", 1, 4, [
        ("arugula", 1, "cup"),
        ("cucumber", 0.5, "piece"),
        ("apple_green", 1, "piece"),
        ("basil", 3, "tbsp"),
        ("water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Bruise the basil between your palms first — whole leaves dropped in cold barely give anything up."),

    ("gr-tabbouleh-sip", "Tabbouleh Sip", "green", 1, 5, [
        ("parsley", 4, "tbsp"),
        ("cucumber", 0.5, "piece"),
        ("mint", 1, "tbsp"),
        ("tahini", 1, "tbsp"),
        ("water", 0.75, "cup"),
        ("lemon_juice", 2, "tbsp"),
    ], "Flat-leaf parsley, not curly — curly parsley is tougher and tastes more like stalk than herb."),

    ("gr-cucumber-doogh", "Cucumber Doogh", "green", 1, 4, [
        ("spinach", 1, "cup"),
        ("kefir", 0.75, "cup"),
        ("cucumber", 0.5, "piece"),
        ("dill", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Salted yogurt drinks want more salt than you think — taste it, then add another pinch."),

    ("gr-mint-condition", "Mint Condition", "green", 1, 3, [
        ("butter_lettuce", 1, "cup"),
        ("honeydew", 1, "cup"),
        ("water", 0.5, "cup"),
        ("mint", 3, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Spearmint, not peppermint — peppermint leaves a cooling burn that fights the melon."),

    # ---------------------------------------------- with a protein element
    ("gr-green-apple-rebuild", "Green Apple Rebuild", "green", 1, 3, [
        ("spinach", 1.5, "cup"),
        ("apple_green", 1, "piece"),
        ("oat_milk", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("cinnamon", 0.25, "tsp"),
    ], "Pea protein has a faintly savoury edge that tart apple covers better than banana does."),

    ("gr-silken-mango-green", "Silken Mango Green", "green", 1, 4, [
        ("baby_kale", 1, "cup"),
        ("silken_tofu", 0.5, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("coconut_water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Silken tofu, not firm — firm tofu stays in grains no matter how long the blade runs."),
]
