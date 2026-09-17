"""Breakfast blends for the Blast — oats, grains, seeds and protein that hold until lunch."""

RECIPES = [
    # ---------------------------------------------------------------- oat builds
    ("bf-steel-cut-sunday", "Steel Cut Sunday", "breakfast", 1, 5, [
        ("milk_2", 0.75, "cup"),
        ("steel_cut_oats", 0.5, "cup"),
        ("date", 2, "piece"),
        ("walnuts", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
    ], "Cooked steel-cut oats blend cleanest straight from the fridge — warm ones turn gluey under the blade."),

    ("bf-the-mill-shake", "The Mill Shake", "breakfast", 1, 3, [
        ("oat_milk", 1, "cup"),
        ("oat_flour", 0.25, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("vanilla_bean", 0.5, "tsp"),
        ("maple_syrup", 1, "tsp"),
    ], "Oat flour hydrates instantly, so pour it over the milk and give it a minute before the blade runs or you get a paste ring on the wall."),

    ("bf-pear-bran-wake-up", "Pear and Bran Wake-Up", "breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("oat_bran", 0.25, "cup"),
        ("pear", 1, "piece"),
        ("flax", 1, "tbsp"),
        ("honey", 1, "tsp"),
    ], "Leave the pear skin on — it is most of the fibre and it disappears completely at this ratio."),

    ("bf-swiss-muesli-cup", "Swiss Muesli Cup", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("muesli", 0.5, "cup"),
        ("apple_green", 0.5, "piece"),
        ("golden_raisin", 2, "tbsp"),
        ("lemon_juice", 1, "tsp"),
    ], "Let the muesli soak in the milk for a full minute first — the dried fruit in it is what jams a dry blade."),

    ("bf-trail-mix-morning", "Trail Mix Morning", "breakfast", 1, 3, [
        ("cashew_milk", 0.75, "cup"),
        ("granola", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("cranberry_dried", 2, "tbsp"),
    ], "Use a clustery granola rather than a loose one; the clusters break into flecks you can still feel, which is the point."),

    ("bf-turkish-oat-cup", "Turkish Oat Cup", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("espresso", 0.25, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("date_syrup", 1, "tbsp"),
    ], "Brew the espresso ahead and chill it — hot coffee on oats makes porridge before the lid is even on."),

    ("bf-black-currant-porridge", "Black Currant Porridge Cup", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("blackcurrant", 0.5, "cup"),
        ("honey", 2, "tsp"),
    ], "Black currants are sharper than they look; taste before you add the second spoon of honey."),

    # ------------------------------------------------- overnight oats and bircher
    ("bf-bircher-classic", "Bircher Classic", "breakfast", 1, 5, [
        ("apple_juice", 0.5, "cup"),
        ("oats", 0.33, "cup"),
        ("apple", 1, "piece"),
        ("greek_yogurt_whole", 0.25, "cup"),
        ("lemon_juice", 1, "tsp"),
        ("almonds", 1, "tbsp"),
    ], "The original is grated apple soaked overnight — if you have the night, soak the oats in the juice and this blends in ten seconds."),

    ("bf-alpine-bircher", "Alpine Bircher", "breakfast", 1, 5, [
        ("milk_2", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("berries_mixed_frozen", 0.5, "cup"),
        ("hazelnut_butter", 1, "tbsp"),
        ("honey", 1, "tsp"),
    ], "Hazelnut butter separates in the jar; stir it properly before you spoon it in or you get a slick of oil on top."),

    ("bf-overnight-vanilla-jar", "Overnight Vanilla Jar", "breakfast", 1, 3, [
        ("almond_milk_vanilla", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("chia", 1, "tbsp"),
        ("greek_yogurt_nonfat", 0.25, "cup"),
        ("maple_syrup", 2, "tsp"),
    ], "Oats and chia both want the liquid first — add them to the milk, count to sixty, then blend."),

    ("bf-overnight-cocoa-jar", "Overnight Cocoa Jar", "breakfast", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"),
        ("salt", 0.25, "tsp"),
    ], "The pinch of salt is not optional with cacao — without it the whole thing tastes flat and chalky."),

    ("bf-lunchbox-jar", "Lunchbox Jar", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("peanut_butter", 1.5, "tbsp"),
        ("raspberry_jam", 1, "tbsp"),
    ], "Use a seedy jam rather than jelly — the seeds survive the blade and give it something to be."),

    ("bf-hazelnut-bircher", "Hazelnut Bircher", "breakfast", 1, 5, [
        ("milk_whole", 0.75, "cup"),
        ("muesli", 0.33, "cup"),
        ("pear", 0.5, "piece"),
        ("hazelnuts", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
    ], None),

    # ------------------------------------------------------------- grain shakes
    ("bf-andes-morning", "Andes Morning", "breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("quinoa", 0.5, "cup"),
        ("banana", 0.5, "piece"),
        ("maple_syrup", 2, "tsp"),
        ("cinnamon", 0.25, "tsp"),
    ], "Rinse and cool the quinoa properly — any leftover saponin reads as soap in a cold drink."),

    ("bf-buckwheat-blini-shake", "Buckwheat Blini Shake", "breakfast", 1, 4, [
        ("buttermilk", 0.75, "cup"),
        ("buckwheat", 0.5, "cup"),
        ("honey", 1, "tbsp"),
        ("lemon_zest", 0.5, "tsp"),
    ], "Buttermilk plus buckwheat is a tang-on-tang build; the honey is doing real work, don't cut it."),

    ("bf-millet-and-honey", "Millet and Honey Morning", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("millet", 0.5, "cup"),
        ("honey", 1, "tbsp"),
        ("apricot_dried", 3, "piece"),
        ("cardamom", 0.25, "tsp"),
    ], "Soak the dried apricots in a splash of hot water for a minute so they blend instead of bouncing."),

    ("bf-alegria-morning", "Alegria Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("amaranth", 0.5, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("coconut_sugar", 2, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Named for the Mexican amaranth bar — if you can find popped amaranth, a spoonful on top keeps the crunch."),

    ("bf-highland-teff-shake", "Highland Teff Shake", "breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("teff", 0.5, "cup"),
        ("date", 2, "piece"),
        ("almond_butter", 1, "tbsp"),
    ], "Teff carries a faint cocoa note of its own, so go easy on anything you add for sweetness until you taste it."),

    ("bf-horchata-morning-rice", "Horchata Morning Rice", "breakfast", 1, 4, [
        ("rice_milk", 0.75, "cup"),
        ("brown_rice", 0.5, "cup"),
        ("almonds", 2, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("condensed_milk", 1, "tbsp"),
    ], "Soak the almonds in hot water ten minutes and the skins slip off — that is the difference between silky and gritty."),

    ("bf-golden-apricot-wheat", "Golden Apricot Wheat", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("wheat_germ", 0.25, "cup"),
        ("apricot_dried", 4, "piece"),
        ("yogurt_vanilla", 0.25, "cup"),
        ("honey", 1, "tsp"),
    ], "Wheat germ goes rancid quickly — keep the jar in the freezer and smell it before it goes in."),

    # ------------------------------------------------- chia and flax, thinned out
    ("bf-vanilla-chia-set", "Vanilla Chia Set", "breakfast", 1, 4, [
        ("milk_2", 1, "cup"),
        ("chia", 2, "tbsp"),
        ("vanilla_bean", 0.5, "tsp"),
        ("maple_syrup", 2, "tsp"),
    ], "Chia needs to go in with the liquid and sit a minute or it clumps on the blade in a single grey knot."),

    ("bf-mango-chia-cup", "Mango Chia Cup", "breakfast", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"),
        ("chia", 1.5, "tbsp"),
        ("mango_frozen", 0.75, "cup"),
        ("lime_juice", 2, "tsp"),
    ], "Frozen mango chills the mix before the chia has swelled, so give the seeds their minute in the coconut milk first."),

    ("bf-cocoa-chia-pudding", "Cocoa Chia Pudding", "breakfast", 1, 4, [
        ("oat_milk", 1, "cup"),
        ("chia", 2, "tbsp"),
        ("cacao_powder", 1, "tbsp"),
        ("date_paste", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("bf-cinnamon-flax-morning", "Cinnamon Flax Morning", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("flax", 2, "tbsp"),
        ("applesauce", 0.5, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("maple_syrup", 1, "tsp"),
    ], "Buy flaxseed whole and grind it as you need it; pre-ground flax loses its nuttiness within weeks of opening."),

    ("bf-raspberry-lime-chia", "Raspberry Lime Chia", "breakfast", 1, 4, [
        ("coconut_water", 0.75, "cup"),
        ("chia", 1.5, "tbsp"),
        ("raspberry_frozen", 0.75, "cup"),
        ("lime_zest", 0.5, "tsp"),
        ("honey", 2, "tsp"),
    ], "Zest the lime before you juice anything — zest off a squeezed half is a miserable job."),

    ("bf-soft-pear-morning", "Soft Pear Morning", "breakfast", 1, 4, [
        ("almond_milk", 1, "cup"),
        ("psyllium", 1, "tsp"),
        ("pear", 1, "piece"),
        ("oats", 2, "tbsp"),
        ("ginger_ground", 0.25, "tsp"),
    ], "Psyllium thickens in under a minute and keeps going — drink this one soon after it is made or it sets in the cup."),

    ("bf-blackberry-flax-rise", "Blackberry Flax Rise", "breakfast", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("blackberry_frozen", 0.75, "cup"),
        ("flax", 2, "tbsp"),
        ("honey", 2, "tsp"),
    ], "Blackberry seeds never fully break down — lean into it, or swap to blueberries if that bothers you."),

    # --------------------------------------------------- the cereal shelf
    ("bf-bottom-of-the-bowl", "Bottom of the Bowl", "breakfast", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("cornflakes", 1, "cup"),
        ("banana", 0.5, "piece"),
        ("sugar", 2, "tsp"),
    ], "This is the sweet milk left at the end of the bowl, on purpose — let the flakes go soft in the milk before blending."),

    ("bf-crispy-treat-morning", "Crispy Treat Morning", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("rice_cereal", 1, "cup"),
        ("marshmallow_fluff", 1, "tbsp"),
        ("peanut_butter", 1, "tbsp"),
    ], "Add half the cereal at the start and the rest after ten seconds of blending, so some of it stays gritty."),

    ("bf-graham-cracker-morning", "Graham Cracker Morning", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("graham_cracker", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("honey", 2, "tsp"),
        ("cinnamon", 0.25, "tsp"),
    ], None),

    ("bf-cereal-milk-cup", "Cereal Milk Cup", "breakfast", 1, 3, [
        ("milk_whole", 1, "cup"),
        ("cornflakes", 0.75, "cup"),
        ("oats", 2, "tbsp"),
        ("brown_sugar", 2, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Toast the cornflakes on a tray for five minutes first if you want the version that tastes like the ice cream shop."),

    # ------------------------------------------------------ pastry, done honestly
    ("bf-cinnamon-roll-morning", "Cinnamon Roll Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("cream_cheese", 2, "tbsp"),
        ("cinnamon", 1, "tsp"),
        ("brown_sugar", 1, "tbsp"),
    ], "The cream cheese is the icing — it has to be soft or it stays in pale specks."),

    ("bf-bakery-loaf-cup", "Bakery Loaf Cup", "breakfast", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("oat_flour", 0.25, "cup"),
        ("walnuts", 1, "tbsp"),
        ("nutmeg", 0.25, "tsp"),
    ], "The blacker the banana before it went in the freezer, the closer this gets to the loaf."),

    ("bf-frosted-carrot-morning", "Frosted Carrot Morning", "breakfast", 1, 5, [
        ("milk_2", 0.75, "cup"),
        ("carrot", 1, "piece"),
        ("oats", 0.25, "cup"),
        ("cream_cheese", 1, "tbsp"),
        ("raisin", 2, "tbsp"),
        ("allspice", 0.25, "tsp"),
    ], "Grate the carrot rather than chunking it — the Blast will chew chunks, but you will find orange threads in the last mouthful."),

    ("bf-streusel-apple-morning", "Streusel Apple Morning", "breakfast", 1, 4, [
        ("apple_juice", 0.5, "cup"),
        ("apple", 1, "piece"),
        ("oats", 0.33, "cup"),
        ("pecans", 1, "tbsp"),
        ("apple_pie_spice", 0.5, "tsp"),
        ("brown_sugar", 2, "tsp"),
    ], "Use two different apples if you have them — one sharp, one sweet — which is what a good pie does anyway."),

    ("bf-autumn-spice-bran", "Autumn Spice Bran", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("pumpkin_puree", 0.5, "cup"),
        ("oat_bran", 0.25, "cup"),
        ("pumpkin_spice", 0.5, "tsp"),
        ("maple_syrup", 1, "tbsp"),
    ], "Canned pumpkin, not pie filling — the filling is already sugared and will take the drink somewhere sickly."),

    ("bf-muffin-basket-morning", "Muffin Basket Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("oat_flour", 0.25, "cup"),
        ("lemon_zest", 0.5, "tsp"),
        ("sugar", 2, "tsp"),
    ], "Lemon zest is what makes a blueberry muffin taste like a blueberry muffin rather than just blueberries."),

    ("bf-french-toast-tuesday", "French Toast Tuesday", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("egg_white", 0.25, "cup"),
        ("oats", 0.33, "cup"),
        ("maple_syrup", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("nutmeg", 0.25, "tsp"),
    ], "Only pasteurized whites belong in a cold drink — check the carton says so before you pour."),

    ("bf-short-stack-shake", "Short Stack Shake", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("pancake", 0.5, "cup"),
        ("maple_syrup", 1, "tbsp"),
        ("butter", 1, "tsp"),
        ("banana_frozen", 0.5, "cup"),
    ], "Yesterday's leftover pancakes work better than fresh ones; a little staleness keeps them from turning to glue."),

    ("bf-toast-and-peanut-morning", "Toast and Peanut Morning", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("banana", 0.5, "piece"),
        ("salt", 0.25, "tsp"),
    ], "Toast the oats first and this stops being oatmeal and starts being toast."),

    ("bf-buttered-toast-and-jam", "Buttered Toast and Jam", "breakfast", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("oat_flour", 0.25, "cup"),
        ("strawberry_jam", 1.5, "tbsp"),
        ("butter", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Salted butter, and only a teaspoon — any more and it beads on the surface as it warms up."),

    ("bf-almond-croissant-morning", "Almond Croissant Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("almond_flour", 0.25, "cup"),
        ("oats", 0.25, "cup"),
        ("almond_extract", 0.25, "tsp"),
        ("powdered_sugar", 1, "tbsp"),
    ], "Almond extract is ferocious — a quarter teaspoon is already at the edge, and half will taste like marzipan gone wrong."),

    ("bf-crumb-coffee-cake-cup", "Crumb Coffee Cake Cup", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("sour_cream", 2, "tbsp"),
        ("brown_sugar", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("pecans", 1, "tbsp"),
    ], "Sour cream is what makes a coffee cake tender, and it does the same thing here — yogurt is not the same swap."),

    ("bf-lemon-poppy-seed-loaf", "Lemon Poppy Seed Loaf", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("greek_yogurt_whole", 0.25, "cup"),
        ("oat_flour", 0.25, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("lemon_zest", 1, "tsp"),
        ("poppy_seeds", 1, "tsp"),
    ], "Add the poppy seeds at the very end and pulse once — blending them fully turns the whole cup a dull grey."),

    ("bf-cherry-danish-morning", "Cherry Danish Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("cherry_frozen", 0.75, "cup"),
        ("cream_cheese", 2, "tbsp"),
        ("oats", 0.25, "cup"),
        ("almond_extract", 0.25, "tsp"),
    ], None),

    # ------------------------------------------- egg white and yogurt, high protein
    ("bf-egg-white-oat-builder", "Egg White Oat Builder", "breakfast", 1, 3, [
        ("milk_skim", 0.75, "cup"),
        ("egg_white", 0.5, "cup"),
        ("oats", 0.33, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Pasteurized whites blend to a foam head — let it stand thirty seconds and the foam settles back in."),

    ("bf-egg-white-berry-rise", "Egg White Berry Rise", "breakfast", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("egg_white", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"),
        ("oat_bran", 2, "tbsp"),
        ("honey", 2, "tsp"),
    ], None),

    ("bf-skyr-oat-morning", "Skyr Oat Morning", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("skyr", 0.5, "cup"),
        ("oats", 0.25, "cup"),
        ("blueberry_frozen", 0.5, "cup"),
        ("maple_syrup", 1, "tsp"),
    ], "Skyr is thick enough to stall the blade on its own, so it goes in after the milk, never first."),

    ("bf-cottage-crunch-morning", "Cottage Crunch Morning", "breakfast", 1, 4, [
        ("milk_2", 0.75, "cup"),
        ("cottage_cheese", 0.5, "cup"),
        ("granola", 0.33, "cup"),
        ("date", 2, "piece"),
        ("cinnamon", 0.25, "tsp"),
    ], "Blend the cottage cheese with the milk alone for ten seconds first — that is what kills the curds."),

    ("bf-parfait-in-a-cup", "Parfait in a Cup", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("greek_yogurt_2", 0.5, "cup"),
        ("granola", 0.33, "cup"),
        ("strawberry_frozen", 0.5, "cup"),
        ("honey", 2, "tsp"),
    ], None),

    ("bf-quark-and-berry-morning", "Quark and Berry Morning", "breakfast", 1, 3, [
        ("milk_skim", 0.75, "cup"),
        ("quark", 0.5, "cup"),
        ("raspberry_frozen", 0.75, "cup"),
        ("flax", 1, "tbsp"),
        ("agave", 2, "tsp"),
    ], "Quark is milder and less sour than Greek yogurt, so it takes fruit that would otherwise need sweetening."),

    ("bf-kefir-bircher-cup", "Kefir Bircher Cup", "breakfast", 1, 4, [
        ("kefir", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("apple", 0.5, "piece"),
        ("hemp_hearts", 1, "tbsp"),
        ("honey", 2, "tsp"),
    ], "Let the oats sit in the kefir a minute before blending; it is thick, so they hydrate slower than they would in milk."),

    ("bf-labneh-and-date-morning", "Labneh and Date Morning", "breakfast", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("labneh", 0.33, "cup"),
        ("date", 3, "piece"),
        ("tahini", 1, "tbsp"),
        ("sesame_seeds", 1, "tsp"),
    ], "Labneh, dates and tahini is a Levantine breakfast plate — a pinch of salt makes all three louder."),

    ("bf-casein-slow-oat", "Slow Build Oat", "breakfast", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("casein", 1, "piece"),
        ("oats", 0.33, "cup"),
        ("almond_butter", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
    ], "Casein thickens as it sits, so if you are drinking this at your desk in twenty minutes, add another splash of milk now."),

    # ------------------------------------------------- avocado and savoury leaning
    ("bf-avocado-oat-morning", "Avocado Oat Morning", "breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("avocado", 0.5, "piece"),
        ("oats", 0.25, "cup"),
        ("lime_juice", 2, "tsp"),
        ("maple_syrup", 2, "tsp"),
    ], "A half avocado is the limit before this stops being a drink and starts being a dip."),

    ("bf-green-builder-morning", "Green Builder Morning", "breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("egg_white", 0.5, "cup"),
        ("avocado_frozen", 0.5, "cup"),
        ("spinach", 1, "cup"),
        ("hemp_hearts", 1, "tbsp"),
    ], "Frozen avocado gives you cold and creamy in one ingredient, so you do not need ice watering it down."),

    ("bf-savory-tomato-oat-cup", "Savory Tomato Oat Cup", "breakfast", 1, 4, [
        ("tomato_juice", 0.75, "cup"),
        ("oats", 0.25, "cup"),
        ("olive_oil", 1, "tsp"),
        ("smoked_paprika", 0.25, "tsp"),
        ("black_pepper", 0.25, "tsp"),
    ], "Closer to salmorejo than to porridge — the oats are doing the job the stale bread does there."),

    ("bf-miso-morning-oat", "Miso Morning Oat", "breakfast", 1, 4, [
        ("broth_veg", 0.75, "cup"),
        ("oats", 0.25, "cup"),
        ("miso", 1, "tsp"),
        ("silken_tofu", 0.33, "cup"),
        ("scallion", 1, "piece"),
    ], "White miso only, and keep the broth cool — heat past a simmer flattens miso into plain salt."),

    ("bf-sweet-potato-tahini-morning", "Sweet Potato Tahini Morning", "breakfast", 1, 5, [
        ("milk_2", 0.75, "cup"),
        ("sweet_potato", 0.5, "cup"),
        ("tahini", 1, "tbsp"),
        ("date_syrup", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
    ], "Roast the sweet potato rather than boiling it — boiled, it brings water and no sweetness."),

    ("bf-matcha-avocado-morning", "Matcha Avocado Morning", "breakfast", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("avocado", 0.5, "piece"),
        ("matcha", 1, "tsp"),
        ("oats", 2, "tbsp"),
        ("honey", 2, "tsp"),
    ], "Sift the matcha or rub it through your fingers on the way in; it clumps into bitter green pellets otherwise."),

    ("bf-hummus-morning-cup", "Savoury Chickpea Morning", "breakfast", 1, 4, [
        ("broth_veg", 0.75, "cup"),
        ("chickpeas", 0.5, "cup"),
        ("oat_bran", 2, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("cumin", 0.25, "tsp"),
        ("olive_oil", 1, "tsp"),
    ], "Peel the chickpeas if you have five spare minutes — the skins are the only thing standing between this and smooth."),

    # ------------------------------------------------------ fast, four ingredients
    ("bf-two-minute-oat", "Two Minute Oat", "breakfast", 1, 2, [
        ("oat_milk", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("honey", 2, "tsp"),
    ], "Pour the milk, tip the oats in, find your keys, then blend — the minute they sit is what makes it smooth."),

    ("bf-late-for-work", "Late for Work", "breakfast", 1, 2, [
        ("milk_2", 0.75, "cup"),
        ("granola", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"),
    ], None),

    ("bf-four-thing-peanut", "Four Thing Peanut", "breakfast", 1, 2, [
        ("milk_2", 0.75, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("banana_frozen", 0.75, "cup"),
        ("oats", 0.25, "cup"),
    ], None),

    ("bf-doorstep-yogurt-cup", "Doorstep Yogurt Cup", "breakfast", 1, 2, [
        ("milk_skim", 0.75, "cup"),
        ("greek_yogurt_nonfat", 0.5, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("flax", 1, "tbsp"),
    ], None),

    ("bf-grab-the-granola", "Grab the Granola", "breakfast", 1, 2, [
        ("kefir", 0.75, "cup"),
        ("granola", 0.5, "cup"),
        ("date", 2, "piece"),
    ], "Pitted dates or you will hear about it — check each one, even the bags that claim to be pitted."),

    ("bf-desk-drawer-chia", "Desk Drawer Chia", "breakfast", 1, 3, [
        ("almond_milk_vanilla", 1, "cup"),
        ("chia", 2, "tbsp"),
        ("peanut_powder", 2, "tbsp"),
        ("maple_syrup", 2, "tsp"),
    ], "Powdered peanut butter is the trick for a desk drawer — it will not go rancid and it thickens as the chia sets."),

    ("bf-ten-past-eight", "Ten Past Eight", "breakfast", 1, 2, [
        ("oat_milk", 0.75, "cup"),
        ("muesli", 0.5, "cup"),
        ("pear", 1, "piece"),
    ], "A ripe pear needs no sweetener here; a hard one needs a teaspoon of honey."),

    ("bf-cold-brew-oat-run", "Cold Brew Oat Run", "breakfast", 1, 3, [
        ("cold_brew", 0.25, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("oats", 0.33, "cup"),
        ("date", 2, "piece"),
    ], "Cold brew concentrate is roughly three times the strength of drip — a quarter cup is a full coffee's worth."),

    ("bf-goji-millet-gold", "Goji Millet Gold", "breakfast", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("millet", 0.5, "cup"),
        ("goji", 0.25, "cup"),
        ("turmeric", 0.25, "tsp"),
        ("honey", 2, "tsp"),
    ], "Soak the goji berries five minutes or they stay leathery — the soaking water goes in too."),
]
