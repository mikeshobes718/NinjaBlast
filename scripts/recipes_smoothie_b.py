"""World smoothies: drinks borrowed from elsewhere, adapted to the Blast cup."""

RECIPES = [
    # ---------------------------------------------------------- South Asia
    ("sm2-namkeen-lassi", "Namkeen Lassi", "smoothie", 1, 3, [
        ("yogurt_plain", 0.75, "cup"),
        ("water", 0.5, "cup"),
        ("ice", 0.5, "cup"),
        ("cumin", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
        ("mint", 1, "tbsp"),
    ], "Toast the cumin in a dry pan for thirty seconds before it goes in — ground cumin straight from the jar tastes dusty here."),

    ("sm2-falooda-blended", "Falooda, Blended", "smoothie", 1, 5, [
        ("milk_whole", 0.75, "cup"),
        ("ice_cream", 0.5, "cup"),
        ("rose_water", 2, "tsp"),
        ("chia", 1, "tbsp"),
        ("pistachios", 1, "tbsp"),
    ], "Falooda is built on basil seeds and vermicelli; chia is the closest stand-in, so add it last and let the cup sit two minutes before drinking."),

    ("sm2-thandai-cooler", "Thandai Cooler", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("almonds", 2, "tbsp"),
        ("cardamom", 0.5, "tsp"),
        ("black_pepper", 0.25, "tsp"),
        ("rose_water", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Soak the almonds in hot water for ten minutes and the blade will turn them to cream instead of grit."),

    ("sm2-masala-chai-date", "Masala Chai Date Shake", "smoothie", 1, 4, [
        ("chai_concentrate", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("date", 3, "piece"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Tear the dates open and check for pits, then soak them in the warm concentrate — cold dates ride around the blade in lumps."),

    ("sm2-aam-panna-cooler", "Aam Panna Cooler", "smoothie", 1, 6, [
        ("mango", 1, "piece"),
        ("water", 0.75, "cup"),
        ("cumin", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
        ("mint", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "The original uses boiled raw green mango; pick the firmest, least ripe fruit you can find so the drink stays sour rather than sweet."),

    ("sm2-kulfi-shake", "Rose Pistachio Kulfi Shake", "smoothie", 1, 4, [
        ("milk_whole", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("pistachios", 2, "tbsp"),
        ("rose_water", 1, "tsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "Blend the pistachios with the milk alone for ten seconds first — once ice is in the cup the nuts never break down."),

    ("sm2-badam-milk-freeze", "Badam Milk Freeze", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("almonds", 2, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-solkadhi-style", "Solkadhi-Style Coconut Cooler", "smoothie", 1, 4, [
        ("coconut_milk_light", 0.75, "cup"),
        ("cranberry_frozen", 0.5, "cup"),
        ("garlic", 0.25, "tsp"),
        ("cilantro", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Solkadhi gets its pink sourness from kokum, which is hard to find — cranberry hits the same sour-and-pink note without pretending to be the same fruit."),

    # ------------------------------------------------ Mexico & Central America
    ("sm2-blended-horchata", "Horchata, Blended", "smoothie", 1, 3, [
        ("rice_milk", 1, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("vanilla_extract", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], "Real horchata means soaking raw rice overnight and straining it; rice milk with cinnamon gets you most of the way in three minutes."),

    ("sm2-agua-de-sandia", "Agua de Sandía", "smoothie", 1, 4, [
        ("watermelon_frozen", 1.5, "cup"),
        ("water", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 2, "tsp"),
        ("mint", 1, "tbsp"),
    ], None),

    ("sm2-pepino-limon", "Agua de Pepino con Limón", "smoothie", 1, 4, [
        ("cucumber", 1, "piece"),
        ("water", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("agave", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Peel half the cucumber and leave the rest — all skin turns it bitter, no skin and you lose the green flavour."),

    ("sm2-agua-de-jamaica", "Agua de Jamaica", "smoothie", 1, 3, [
        ("hibiscus_tea", 1, "cup"),
        ("strawberry", 3, "piece"),
        ("agave", 1, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Steep the hibiscus twice as strong as you would drink it — the ice in the cup is going to dilute it by half."),

    ("sm2-horchata-ajonjoli", "Horchata de Ajonjolí", "smoothie", 1, 5, [
        ("sesame_seeds", 3, "tbsp"),
        ("rice_milk", 0.75, "cup"),
        ("water", 0.25, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Toast the sesame until it starts popping and smells nutty; raw seeds make this taste like wet paper."),

    ("sm2-tamarind-style-cooler", "Tamarind-Style Sour Cooler", "smoothie", 1, 4, [
        ("prune", 3, "piece"),
        ("water", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("brown_sugar", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "This is not agua de tamarindo — prune and lime build the same dark sweet-sour shape, and the pinch of salt is what makes it read as tamarind at all."),

    ("sm2-jicama-limon", "Jícama con Limón", "smoothie", 1, 6, [
        ("jicama", 1, "cup"),
        ("water", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("tajin", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Jicama skin is fibrous and will not break down — peel it thickly with a knife rather than a vegetable peeler."),

    ("sm2-agua-de-tuna", "Agua de Tuna", "smoothie", 1, 6, [
        ("prickly_pear", 2, "piece"),
        ("water", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Buy prickly pears already de-spined, and keep the blend short — the seeds stay whole and pleasant if you don't pulverise them."),

    ("sm2-fresas-con-crema", "Fresas con Crema, Blended", "smoothie", 2, 3, [
        ("strawberry_frozen", 1, "cup"),
        ("sour_cream", 0.25, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("milk_whole", 0.5, "cup"),
    ], None),

    ("sm2-atol-de-elote-chilled", "Atol de Elote, Chilled", "smoothie", 1, 4, [
        ("corn_frozen", 0.75, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("sugar", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("sm2-tepache-style-freeze", "Tepache-Style Pineapple Freeze", "smoothie", 1, 3, [
        ("pineapple_frozen", 1, "cup"),
        ("kombucha", 0.75, "cup"),
        ("brown_sugar", 2, "tsp"),
        ("cinnamon", 0.25, "tsp"),
        ("clove", 0.25, "tsp"),
    ], "Tepache ferments for days on pineapple rind; kombucha lends the same tang and fizz so you can drink it today."),

    # -------------------------------------------------------- South America
    ("sm2-acai-na-tigela-drink", "Açaí na Tigela, Drinkable", "smoothie", 1, 3, [
        ("acai_puree", 1, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("apple_juice", 0.5, "cup"),
        ("granola", 0.25, "cup"),
    ], "In Brazil this is a bowl you eat with a spoon and granola on top; blending the granola in thickens it instead, so leave a spoonful for the surface."),

    ("sm2-vitamina-de-abacate", "Vitamina de Abacate", "smoothie", 1, 4, [
        ("avocado", 0.5, "piece"),
        ("milk_whole", 0.75, "cup"),
        ("sugar", 1, "tbsp"),
        ("lime_juice", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-limonada-suica", "Limonada Suíça", "smoothie", 2, 4, [
        ("lime", 1, "piece"),
        ("water", 0.75, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 1, "cup"),
    ], "The whole lime goes in, peel and all, but blend it for seconds only — the pith turns the drink bitter fast."),

    ("sm2-vitamina-de-mamao", "Vitamina de Mamão", "smoothie", 1, 4, [
        ("papaya", 1, "cup"),
        ("orange_juice", 0.5, "cup"),
        ("oats", 2, "tbsp"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-lucuma-milkshake", "Lúcuma Milkshake", "smoothie", 1, 3, [
        ("lucuma", 2, "tbsp"),
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("sm2-chicha-morada-style", "Chicha Morada-Style Cooler", "smoothie", 1, 4, [
        ("blackcurrant", 0.75, "cup"),
        ("pineapple_juice", 0.75, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("clove", 0.25, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Purple corn is what makes the real thing; black currants give the same deep colour and tannic edge, which is the closest honest substitute."),

    ("sm2-maracuya-en-leche", "Maracuyá en Leche", "smoothie", 1, 3, [
        ("passionfruit_juice", 0.5, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Passion fruit is acidic enough to curdle milk if it sits — blend it and drink it, don't make it ahead."),

    ("sm2-avena-colombiana", "Avena Colombiana", "smoothie", 1, 4, [
        ("oats", 0.25, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Soak the oats in the milk for five minutes first; they blend smooth instead of leaving flecks."),

    ("sm2-mote-con-huesillo", "Mote con Huesillo, Blended", "smoothie", 1, 6, [
        ("apricot_dried", 4, "piece"),
        ("water", 0.75, "cup"),
        ("quinoa", 0.25, "cup"),
        ("brown_sugar", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "The Chilean original is whole dried peaches and husked wheat sitting in syrup — dried apricot and cooked quinoa are the stand-ins that blend."),

    ("sm2-camu-camu-limeade", "Camu Camu Limeade", "smoothie", 1, 3, [
        ("camu_camu", 1, "tsp"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.75, "cup"),
        ("honey", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Camu camu is startlingly sour for a powder — a teaspoon is already assertive, so taste before you reach for more."),

    # ------------------------------------------------------ Southeast Asia
    ("sm2-avocado-shake-manila", "Manila Avocado Shake", "smoothie", 1, 4, [
        ("avocado", 0.5, "piece"),
        ("evaporated_milk", 0.5, "cup"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-halo-halo-blended", "Halo-Halo, Blended", "smoothie", 2, 5, [
        ("evaporated_milk", 0.5, "cup"),
        ("jackfruit", 0.5, "cup"),
        ("coconut_sweetened", 2, "tbsp"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Halo-halo is layers you stir at the table, and blending trades those layers for something you can drink — a fair swap, but not the same dessert."),

    ("sm2-ube-style-purple-shake", "Ube-Style Purple Shake", "smoothie", 1, 3, [
        ("dragonfruit_frozen", 1, "cup"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("vanilla_bean", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "There is no ube here — dragon fruit borrows the colour only, so call it what it is rather than serving it as ube."),

    ("sm2-cha-yen-blended", "Cha Yen, Blended", "smoothie", 1, 5, [
        ("black_tea", 0.75, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("evaporated_milk", 2, "tbsp"),
        ("vanilla_extract", 0.5, "tsp"),
        ("clove", 0.25, "tsp"),
        ("ice", 1.25, "cup"),
    ], "Brew the tea at double strength and chill it first — warm tea melts the ice and you end up with beige milk."),

    ("sm2-pandan-style-coconut", "Pandan-Style Coconut Freeze", "smoothie", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"),
        ("coconut_meat", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("matcha", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Pandan isn't in the pantry; the matcha is here for the grassy colour and a little bitterness, not to imitate the leaf."),

    ("sm2-es-teler-blended", "Es Teler, Blended", "smoothie", 2, 6, [
        ("avocado", 0.5, "piece"),
        ("jackfruit", 0.5, "cup"),
        ("coconut_meat", 0.25, "cup"),
        ("coconut_milk_bev", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Young coconut meat is soft and blends away; mature coconut stays chewy, so buy the frozen young kind if you can."),

    ("sm2-cendol-style-freeze", "Cendol-Style Palm Sugar Freeze", "smoothie", 1, 3, [
        ("coconut_milk_canned", 0.5, "cup"),
        ("rice_milk", 0.5, "cup"),
        ("coconut_sugar", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "The green rice-flour worms cannot survive a blender, so this is the other half of cendol: coconut milk and dark palm sugar with salt."),

    ("sm2-bandung-style-freeze", "Bandung Rose Milk Freeze", "smoothie", 1, 3, [
        ("evaporated_milk", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("rose_water", 2, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-sinh-to-mang-cau", "Sinh Tố Mãng Cầu", "smoothie", 1, 5, [
        ("soursop", 1, "cup"),
        ("coconut_milk_bev", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("lime_juice", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Soursop seeds are hard and bitter — pick every one out by hand before blending, they do not break down."),

    ("sm2-chanh-muoi-style", "Chanh Muối, Blended", "smoothie", 1, 4, [
        ("lime", 1, "piece"),
        ("water", 1, "cup"),
        ("sugar", 1, "tbsp"),
        ("salt", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], "The real version uses limes salted in a jar for months; fresh lime with salt is the quick approximation, and it wants more salt than feels reasonable."),

    # ------------------------------------------------------------ East Asia
    ("sm2-matcha-white-peach", "Matcha and White Peach", "smoothie", 1, 3, [
        ("matcha", 1, "tsp"),
        ("peach_frozen", 1, "cup"),
        ("milk_2", 0.75, "cup"),
        ("honey", 2, "tsp"),
    ], "Stir the matcha into a splash of the milk with a spoon before anything else goes in, or it clumps against the frozen fruit."),

    ("sm2-amazake-style", "Amazake-Style Rice Cooler", "smoothie", 1, 4, [
        ("brown_rice", 0.5, "cup"),
        ("rice_milk", 0.75, "cup"),
        ("ginger", 1, "tsp"),
        ("honey", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Amazake gets its sweetness from koji fermenting overnight; this borrows the rice body and grated ginger finish, not the fermentation."),

    ("sm2-misugaru-style-shake", "Misugaru-Style Grain Shake", "smoothie", 1, 5, [
        ("milk_2", 0.75, "cup"),
        ("oats", 3, "tbsp"),
        ("sesame_seeds", 1, "tbsp"),
        ("almonds", 1, "tbsp"),
        ("honey", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Misugaru is a roasted multigrain powder — toast the oats, sesame and almonds in a dry pan first and you get much closer to it."),

    ("sm2-sujeonggwa-style", "Sujeonggwa-Style Persimmon Punch", "smoothie", 1, 5, [
        ("persimmon", 1, "piece"),
        ("water", 0.75, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("ginger", 1, "tsp"),
        ("brown_sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Sujeonggwa uses dried persimmon softened in spiced syrup; a very ripe hachiya, soft to the point of collapse, is the fresh-fruit route."),

    ("sm2-lychee-green-tea", "Lychee Green Tea Freeze", "smoothie", 1, 6, [
        ("lychee", 8, "piece"),
        ("green_tea", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("lime_juice", 1, "tsp"),
        ("ice", 1, "cup"),
    ], "Tinned lychees work and save you ten minutes of peeling — drop the honey to a teaspoon if you use them, they come packed in syrup."),

    ("sm2-papaya-milk-taiwan", "Papaya Milk, Taiwanese Style", "smoothie", 1, 4, [
        ("papaya", 1, "cup"),
        ("milk_whole", 0.75, "cup"),
        ("sugar", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Blend it briefly and drink it straight away — papaya enzymes turn milk bitter within about ten minutes."),

    ("sm2-melon-cream-soda-float", "Melon Cream Soda Float", "smoothie", 1, 3, [
        ("honeydew", 1, "cup"),
        ("cream_soda", 0.5, "cup"),
        ("ice_cream", 0.25, "cup"),
        ("ice", 0.5, "cup"),
    ], "Soda foams violently under the blade — pour it in last and run the blender only a few seconds."),

    ("sm2-black-sesame-soy", "Black Sesame Soy Milk", "smoothie", 1, 4, [
        ("soy_milk", 0.75, "cup"),
        ("sesame_seeds", 3, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Black sesame if you can get it, and toast it until it pops — untoasted seeds give you colour without the roasted flavour that carries this drink."),

    ("sm2-mango-pomelo-style", "Mango Pomelo Sago-Style", "smoothie", 2, 6, [
        ("mango_frozen", 1, "cup"),
        ("grapefruit", 0.5, "piece"),
        ("coconut_milk_bev", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Pomelo is milder than grapefruit, so strip every bit of white membrane off the segments or the bitterness takes over."),

    ("sm2-goji-red-date-cooler", "Goji and Red Date Cooler", "smoothie", 1, 5, [
        ("goji", 0.25, "cup"),
        ("date", 2, "piece"),
        ("black_tea", 0.75, "cup"),
        ("ginger", 1, "tsp"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Soak the goji berries in the hot tea for five minutes — dry ones stay leathery and leave shreds in the drink."),

    # ------------------------------------------------------------ Caribbean
    ("sm2-morir-sonando", "Morir Soñando", "smoothie", 1, 3, [
        ("orange_juice", 0.75, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("sugar", 2, "tsp"),
        ("vanilla_extract", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], "Both the juice and the milk have to be properly cold before they meet, or the acid curdles the milk into threads."),

    ("sm2-sorrel-freeze", "Sorrel Agua Helada", "smoothie", 1, 4, [
        ("hibiscus_tea", 1, "cup"),
        ("ginger", 1, "tsp"),
        ("clove", 0.25, "tsp"),
        ("brown_sugar", 1, "tbsp"),
        ("orange_zest", 1, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-guava-con-queso", "Guayaba y Queso", "smoothie", 1, 5, [
        ("guava", 2, "piece"),
        ("cream_cheese", 2, "tbsp"),
        ("milk_whole", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Guava seeds are gritty and survive blending — scoop the seedy centres out and use the flesh around them."),

    ("sm2-coquito-style-freeze", "Coquito-Style Freeze", "smoothie", 2, 4, [
        ("coconut_milk_canned", 0.5, "cup"),
        ("condensed_milk", 3, "tbsp"),
        ("milk_2", 0.5, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("nutmeg", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-peanut-punch", "Peanut Punch", "smoothie", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("condensed_milk", 2, "tbsp"),
        ("oats", 2, "tbsp"),
        ("nutmeg", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-irish-moss-drink", "Irish Moss Drink", "smoothie", 1, 3, [
        ("sea_moss", 2, "tbsp"),
        ("milk_whole", 0.75, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("vanilla_extract", 0.5, "tsp"),
        ("nutmeg", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Sea moss gel keeps thickening in the cup, so drink this within a few minutes or it sets into something closer to pudding."),

    # ----------------------------------- Middle East, Persia, North Africa, Iberia
    ("sm2-beirut-fruit-cocktail", "Beirut Fruit Cocktail", "smoothie", 1, 5, [
        ("mango_frozen", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("orange_juice", 0.75, "cup"),
        ("orange_blossom", 1, "tsp"),
        ("honey", 2, "tsp"),
        ("pistachios", 1, "tbsp"),
    ], None),

    ("sm2-doogh-style-cooler", "Doogh-Style Cooler", "smoothie", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("sparkling_water", 0.5, "cup"),
        ("mint", 1, "tbsp"),
        ("salt", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Add the sparkling water last and blend for three seconds — any longer and you have flat salty yogurt."),

    ("sm2-tahini-molasses-shake", "Tahini and Molasses Shake", "smoothie", 1, 3, [
        ("tahini", 2, "tbsp"),
        ("molasses", 1, "tbsp"),
        ("milk_whole", 0.75, "cup"),
        ("date", 2, "piece"),
        ("ice", 0.75, "cup"),
    ], "Tahini stirred into grape or date molasses is a Levantine breakfast spread — this is that, drinkable, and it wants the molasses to stay assertive."),

    ("sm2-halva-shake", "Pistachio Halva Shake", "smoothie", 1, 3, [
        ("pistachio_butter", 2, "tbsp"),
        ("tahini", 1, "tbsp"),
        ("milk_2", 0.75, "cup"),
        ("honey", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "The salt is not optional — halva is sweet enough to go flat without it."),

    ("sm2-sahlab-style-freeze", "Sahlab-Style Freeze", "smoothie", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("rose_water", 1, "tsp"),
        ("coconut_shredded", 2, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Sahlab is a hot winter drink thickened with orchid-root flour; cold and unthickened, this keeps the rose-and-cinnamon flavour and drops the texture."),

    ("sm2-jallab-style", "Jallab-Style Cooler", "smoothie", 1, 3, [
        ("date_syrup", 2, "tbsp"),
        ("rose_water", 1, "tsp"),
        ("golden_raisin", 2, "tbsp"),
        ("pine_nuts", 1, "tbsp"),
        ("water", 0.75, "cup"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-laban-cucumber-mint", "Laban with Cucumber and Mint", "smoothie", 1, 4, [
        ("labneh", 0.25, "cup"),
        ("water", 0.75, "cup"),
        ("cucumber", 0.5, "piece"),
        ("mint", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Labneh is thick enough to stall the blade on its own — the water goes in first, then everything else on top."),

    ("sm2-sharbat-e-talebi", "Sharbat-e Talebi", "smoothie", 1, 4, [
        ("cantaloupe", 1.25, "cup"),
        ("rose_water", 1, "tsp"),
        ("water", 0.5, "cup"),
        ("sugar", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-sekanjabin-cucumber", "Sekanjabin Cucumber Cooler", "smoothie", 1, 4, [
        ("cucumber", 0.5, "piece"),
        ("mint", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("cider_vinegar", 1, "tbsp"),
        ("water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], "Sekanjabin is a honey-and-vinegar syrup, and the balance is personal — start with half the vinegar and add the rest by taste."),

    ("sm2-sharbat-e-rivas", "Sharbat-e Rivas", "smoothie", 1, 5, [
        ("rhubarb", 0.75, "cup"),
        ("water", 0.75, "cup"),
        ("sugar", 2, "tbsp"),
        ("rose_water", 1, "tsp"),
        ("lime_juice", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Raw rhubarb is harsh and squeaky — toss it with the sugar and let it sit five minutes before blending so it softens and gives up juice."),

    ("sm2-qamar-al-din-style", "Qamar al-Din Apricot Cooler", "smoothie", 1, 6, [
        ("apricot_dried", 5, "piece"),
        ("water", 1, "cup"),
        ("orange_blossom", 1, "tsp"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "The proper version starts with sheets of apricot paste soaked for hours; dried apricots in hot water for ten minutes is the weeknight route."),

    ("sm2-moroccan-avocado-milk", "Moroccan Avocado Milk", "smoothie", 1, 4, [
        ("avocado", 0.5, "piece"),
        ("milk_whole", 0.75, "cup"),
        ("almonds", 2, "tbsp"),
        ("orange_blossom", 1, "tsp"),
        ("honey", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Orange blossom water is strong — a teaspoon perfumes the whole cup, and a tablespoon makes it taste like soap."),

    ("sm2-salgam-style-cooler", "Şalgam-Style Savoury Cooler", "smoothie", 1, 3, [
        ("beet_juice", 0.75, "cup"),
        ("pickle", 0.25, "cup"),
        ("water", 0.25, "cup"),
        ("salt", 0.25, "tsp"),
        ("cayenne", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Turkish şalgam is fermented purple carrot and turnip, sour and salty rather than sweet; beet juice and pickle brine get you the same territory."),

    ("sm2-kefir-sour-cherry", "Kefir and Sour Cherry", "smoothie", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("cherry_sour", 0.75, "cup"),
        ("honey", 1, "tbsp"),
        ("mint", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("sm2-leche-merengada", "Leche Merengada", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("egg_white", 0.25, "cup"),
        ("sugar", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("lemon_zest", 1, "tsp"),
        ("ice", 1, "cup"),
    ], "Use pasteurised whites from a carton, and blend long enough to foam — the froth is the whole character of the drink."),

    # --------------------------------------------------------------- Africa
    ("sm2-baobab-mango-cooler", "Baobab and Mango Cooler", "smoothie", 1, 3, [
        ("baobab", 1, "tbsp"),
        ("mango_frozen", 1, "cup"),
        ("water", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("lime_juice", 1, "tsp"),
    ], "Baobab powder is tart and chalky and will float in clumps — shake it into the water first, then add the fruit."),

    ("sm2-zobo-style-freeze", "Zobo-Style Hibiscus Freeze", "smoothie", 1, 4, [
        ("hibiscus_tea", 0.75, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("ginger", 1, "tsp"),
        ("clove", 0.25, "tsp"),
        ("sugar", 1, "tbsp"),
    ], "Zobo is usually brewed with pineapple rind and ginger together; using the fruit itself makes it sweeter, so ease off the sugar."),

    ("sm2-kunu-style-millet", "Kunu-Style Millet Cooler", "smoothie", 1, 5, [
        ("millet", 0.5, "cup"),
        ("rice_milk", 0.75, "cup"),
        ("ginger", 1, "tsp"),
        ("clove", 0.25, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("sm2-spris-style-layers", "Spris, Blended", "smoothie", 1, 6, [
        ("avocado", 0.5, "piece"),
        ("mango_frozen", 0.5, "cup"),
        ("guava", 1, "piece"),
        ("orange_juice", 0.75, "cup"),
        ("lime_juice", 1, "tsp"),
    ], "In Ethiopian juice houses spris comes layered in stripes and you eat it with a spoon — one cup and one blade means you get the flavours without the stripes."),

    # --------------------------------------------------------------- Europe
    ("sm2-greek-yogurt-honey-thyme", "Yogurt with Thyme Honey", "smoothie", 1, 3, [
        ("greek_yogurt_whole", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("honey", 1, "tbsp"),
        ("walnuts", 2, "tbsp"),
        ("thyme", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("sm2-granita-di-limone", "Granita di Limone", "smoothie", 1, 4, [
        ("lemon_juice", 0.25, "cup"),
        ("water", 0.5, "cup"),
        ("sugar", 2, "tbsp"),
        ("lemon_zest", 1, "tsp"),
        ("ice", 1.5, "cup"),
    ], "A real granita is scraped from a tray over two hours; a cup packed with ice on CRUSH is the shortcut, and it wants more sugar than you'd think because cold mutes sweetness."),

    ("sm2-granita-di-gelsi", "Granita di Gelsi", "smoothie", 1, 3, [
        ("mulberry", 1, "cup"),
        ("water", 0.5, "cup"),
        ("sugar", 1, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-granita-di-mandorla", "Granita di Mandorla", "smoothie", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("almond_extract", 0.25, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "In Sicily this is breakfast, eaten with a brioche dunked into it; the extract is powerful, so a quarter teaspoon is the whole dose."),

    ("sm2-blackcurrant-saft-freeze", "Blackcurrant Saft Freeze", "smoothie", 1, 3, [
        ("blackcurrant", 0.75, "cup"),
        ("water", 0.75, "cup"),
        ("sugar", 1, "tbsp"),
        ("lemon_juice", 1, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("sm2-uzvar-style-freeze", "Uzvar-Style Dried Fruit Freeze", "smoothie", 1, 5, [
        ("prune", 3, "piece"),
        ("apricot_dried", 3, "piece"),
        ("water", 1, "cup"),
        ("honey", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Uzvar is dried fruit simmered and left overnight; soak the prunes and apricots in hot water for ten minutes and you get a usable version of the same smoky sweetness."),
]
