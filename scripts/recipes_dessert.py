"""Dessert canon: diner milkshakes, cookie and candy shakes, pie-and-cake-in-a-cup,
dairy-free nice cream, sorbet and granita blends, grown-up dark chocolate, and a
lighter shelf for when you want dessert without the whole dessert."""

RECIPES = [

    # ------------------------------------------------- diner counter classics
    ("ds-soda-fountain-classic", "Soda Fountain Classic", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("vanilla_bean", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Half a cup of milk, not a full one — thin milkshakes are almost always a liquid problem, never an ice cream problem."),

    ("ds-fudge-counter", "Fudge Counter Shake", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 1, "cup"),
        ("dutch_cocoa", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("ds-pink-counter", "Pink Counter", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("strawberry_frozen", 0.75, "cup"),
        ("strawberry_jam", 1, "tbsp"),
    ], "Frozen strawberries beat fresh here — fresh ones bring water, and water is what makes a pink shake taste watery."),

    ("ds-black-and-white", "Black And White", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("chocolate_syrup", 2, "tbsp"),
        ("vanilla_extract", 1, "tsp"),
    ], "Pulse rather than run it — a few short bursts leave dark ribbons through the vanilla instead of blending it all to brown."),

    ("ds-malt-shop-memory", "Malt Shop Memory", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("oat_flour", 2, "tbsp"),
        ("brown_sugar", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "No malt powder in the house: oat flour with brown sugar lands in the same toasted, slightly savoury place."),

    ("ds-banana-counter", "Banana Counter Shake", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("banana", 1, "piece"),
        ("nutmeg", 0.25, "tsp"),
    ], None),

    ("ds-brooklyn-egg-cream", "Brooklyn Egg Cream", "dessert", 1, 2, [
        ("milk_whole", 0.75, "cup"),
        ("chocolate_syrup", 2, "tbsp"),
        ("sparkling_water", 0.5, "cup"),
        ("ice", 0.5, "cup"),
    ], "Blend the milk and syrup first, then add the sparkling water and pulse once — a long blend flattens every bubble out of it."),

    ("ds-too-thick-for-a-straw", "Too Thick For A Straw", "dessert", 2, 3, [
        ("milk_whole", 0.33, "cup"),
        ("ice_cream", 1, "cup"),
        ("heavy_cream", 2, "tbsp"),
        ("vanilla_bean", 1, "tsp"),
    ], "Let the ice cream sit out four or five minutes first; rock-hard scoops just cavitate and the blade spins in an air pocket."),

    # --------------------------------------------------- cookies and candy bar
    ("ds-midnight-sandwich", "Midnight Sandwich", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("choc_cookie", 0.5, "cup"),
        ("salt", 0.25, "tsp"),
    ], "Hold back two cookies and drop them in for the last three seconds — you want rubble, not a uniform grey shake."),

    ("ds-speculoos-drift", "Speculoos Drift", "dessert", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("biscoff", 0.25, "cup"),
        ("cookie_butter", 1, "tbsp"),
    ], "Speculoos are already cinnamon-heavy, so resist adding more spice; the frozen banana is doing the creamy work in place of ice cream."),

    ("ds-highland-shortbread", "Highland Shortbread", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("shortbread", 0.33, "cup"),
        ("vanilla_bean", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("ds-vanilla-wafer-icebox", "Vanilla Wafer Icebox", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("pudding_vanilla", 0.5, "cup"),
        ("vanilla_wafer", 0.33, "cup"),
        ("banana", 1, "piece"),
        ("ice", 0.5, "cup"),
    ], "This is the old icebox cake, so let it stand two minutes after blending — the wafers soften and the texture stops being sandy."),

    ("ds-corner-piece-brownie", "Corner Piece Brownie", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 0.75, "cup"),
        ("brownie", 0.5, "cup"),
        ("espresso_powder", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "A teaspoon of espresso powder doesn't read as coffee; it just makes the chocolate taste darker and more like a real brownie edge."),

    ("ds-confetti-candle", "Confetti Candle", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("powdered_sugar", 1, "tbsp"),
        ("almond_extract", 0.5, "tsp"),
        ("sprinkles", 1, "tbsp"),
    ], "Almond extract is the whole trick behind boxed birthday cake flavour — half a teaspoon, no more, or it turns medicinal."),

    ("ds-campfire-graham", "Campfire Graham", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("graham_cracker", 0.25, "cup"),
        ("marshmallow_fluff", 2, "tbsp"),
        ("chocolate_syrup", 1, "tbsp"),
    ], "Fluff sticks to everything — spoon it onto the ice cream rather than into the milk, so it doesn't weld itself to the bottom of the cup."),

    ("ds-deep-cup-peanut", "Deep Cup Peanut", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 1, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Use the salted peanut butter, not the fancy unsalted stuff; the salt is the entire reason a peanut butter cup works."),

    ("ds-salt-lick-caramel", "Salt Lick Caramel", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("caramel_sauce", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Add the salt, taste, then add a little more — caramel without salt reads as flat sweetness, and most people stop short."),

    ("ds-butterscotch-parlour", "Butterscotch Parlour", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 1, "cup"),
        ("butterscotch_sauce", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("ds-raspberry-in-white", "Raspberry In White", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("raspberry_frozen", 0.75, "cup"),
        ("white_chocolate", 2, "tbsp"),
        ("lemon_juice", 1, "tsp"),
    ], "White chocolate has no cocoa solids to cut the sugar, so the raspberries and the squeeze of lemon are doing all the balancing."),

    ("ds-chocolate-covered-pretzel", "Chocolate Covered Pretzel", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 1, "cup"),
        ("pretzel", 0.33, "cup"),
        ("chocolate_syrup", 1, "tbsp"),
    ], None),

    # ------------------------------------------------------- pie and cake in a cup
    ("ds-florida-icebox", "Florida Icebox", "dessert", 2, 5, [
        ("lime_juice", 0.25, "cup"),
        ("condensed_milk", 0.25, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("graham_cracker", 0.25, "cup"),
        ("lime_zest", 1, "tsp"),
    ], "Zest the limes before you juice them — it is impossible afterwards, and the zest is where the perfume actually lives."),

    ("ds-lemon-curd-cloud", "Lemon Curd Cloud", "dessert", 1, 4, [
        ("milk_whole", 0.5, "cup"),
        ("greek_yogurt_whole", 0.5, "cup"),
        ("lemon_curd", 2, "tbsp"),
        ("shortbread", 0.25, "cup"),
        ("ice", 0.5, "cup"),
    ], "Whole-milk yogurt, not nonfat — the fat is what keeps curd from tasting like sweetened lemon squash."),

    ("ds-harvest-field-pumpkin", "Harvest Field Pumpkin", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("pumpkin_puree", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("pumpkin_spice", 1, "tsp"),
        ("maple_syrup", 1, "tbsp"),
    ], "Check the tin — pumpkin pie filling is already sweetened and spiced, and stacking this on top of it is too much."),

    ("ds-orchard-lane", "Orchard Lane", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("applesauce", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("apple_pie_spice", 1, "tsp"),
        ("graham_cracker", 0.25, "cup"),
    ], None),

    ("ds-pecan-pie-in-a-cup", "Pecan Pie In A Cup", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("pecans", 3, "tbsp"),
        ("molasses", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Toast the pecans in a dry pan for two minutes if you have them raw — untoasted pecans taste papery and vanish into the milk."),

    ("ds-carrot-cake-sundae", "Carrot Cake Sundae", "dessert", 2, 6, [
        ("milk_whole", 0.5, "cup"),
        ("carrot", 1, "piece"),
        ("cream_cheese", 2, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("golden_raisin", 2, "tbsp"),
    ], "Grate the carrot rather than chunking it; the Blast will turn shreds creamy but it leaves chunks as orange confetti."),

    ("ds-mascarpone-and-coffee", "Mascarpone And Coffee", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("mascarpone", 0.25, "cup"),
        ("coffee_ice", 0.75, "cup"),
        ("sugar", 1, "tbsp"),
        ("dutch_cocoa", 1, "tsp"),
    ], "Freezing leftover coffee in an ice tray is the whole trick — plain ice dilutes it, coffee cubes only make it stronger."),

    ("ds-cherry-on-the-cheesecake", "Cherry On The Cheesecake", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("cream_cheese", 3, "tbsp"),
        ("cherry_frozen", 0.75, "cup"),
        ("graham_cracker", 0.25, "cup"),
        ("lemon_juice", 2, "tsp"),
    ], "The lemon juice isn't optional — cheesecake reads as cheesecake because of the acid, not because of the cheese."),

    ("ds-passion-fruit-cheesecake", "Passion Fruit Cheesecake", "dessert", 2, 5, [
        ("milk_whole", 0.5, "cup"),
        ("cream_cheese", 3, "tbsp"),
        ("passionfruit", 2, "piece"),
        ("shortbread", 0.25, "cup"),
        ("honey", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Passion fruit seeds crack under the blade and turn slightly bitter; scoop the pulp and leave half the seeds behind."),

    ("ds-lemon-poppy-cheesecake", "Lemon Poppy Cheesecake", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("cream_cheese", 3, "tbsp"),
        ("lemon_juice", 2, "tbsp"),
        ("poppy_seeds", 1, "tsp"),
        ("powdered_sugar", 2, "tbsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("ds-banoffee-stack", "Banoffee Stack", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("banana_frozen", 1, "cup"),
        ("dulce_de_leche", 2, "tbsp"),
        ("graham_cracker", 0.25, "cup"),
        ("salt", 0.25, "tsp"),
    ], "Frozen banana instead of fresh keeps this thick enough to stand a spoon in, which is the point of banoffee."),

    ("ds-tres-leches-cup", "Tres Leches Cup", "dessert", 2, 4, [
        ("milk_whole", 0.33, "cup"),
        ("evaporated_milk", 0.25, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("pancake", 0.5, "cup"),
        ("cinnamon", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "A leftover pancake stands in for the sponge; tear it up and let it soak in the milks for a minute before you hit blend."),

    ("ds-dulce-de-leche-freeze", "Dulce De Leche Freeze", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("dulce_de_leche", 3, "tbsp"),
        ("ice", 1, "cup"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("ds-beet-velvet-cake", "Beet Velvet Cake", "dessert", 2, 5, [
        ("milk_whole", 0.5, "cup"),
        ("beet", 0.25, "cup"),
        ("cacao_powder", 2, "tbsp"),
        ("cream_cheese", 2, "tbsp"),
        ("sugar", 1, "tbsp"),
    ], "Cooked beet is where red velvet got its colour long before food dye; a quarter cup is plenty, more and it tastes like soil."),

    ("ds-sticky-toffee-pudding", "Sticky Toffee Pudding", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("date", 3, "piece"),
        ("molasses", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Soak the dates in hot water for five minutes and drain them — dry dates leave little leathery specks the blade won't catch."),

    # ------------------------------------------------ nice cream, no dairy at all
    ("ds-soft-serve-no-machine", "Soft Serve, No Machine", "dessert", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("banana_frozen", 1.5, "cup"),
        ("vanilla_extract", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Frozen banana is the entire reason a dairy-free shake comes out creamy instead of icy — slice it before freezing or it welds into a brick."),

    ("ds-mango-lime-nice-cream", "Mango Lime Nice Cream", "dessert", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("mango_frozen", 1.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("date", 2, "piece"),
    ], "Lime with mango is not a garnish — without the acid, frozen mango on its own tastes cloying about halfway down the cup."),

    ("ds-acai-bowl-in-a-cup", "Açaí Bowl In A Cup", "dessert", 1, 3, [
        ("almond_milk", 0.5, "cup"),
        ("acai_puree", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("date", 2, "piece"),
    ], "Unsweetened açaí is genuinely bitter and earthy; the dates and the banana are what turn it into a dessert rather than a chore."),

    ("ds-dark-cherry-nice-cream", "Dark Cherry Nice Cream", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("cherry_frozen", 1, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("almond_butter", 1, "tbsp"),
    ], "The spoon of almond butter is there for fat, not flavour — fat is what stops a fruit-only blend from setting up like a slushie."),

    ("ds-dragon-fruit-soft-serve", "Dragon Fruit Soft Serve", "dessert", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("dragonfruit_frozen", 1, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("lime_juice", 2, "tsp"),
    ], None),

    ("ds-peanut-butter-soft-serve", "Peanut Butter Soft Serve", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 1.5, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Start with half the oat milk and add the rest only if the blade stalls — this one should be scoopable, not pourable."),

    ("ds-cacao-nice-cream", "Cacao Nice Cream", "dessert", 1, 3, [
        ("almond_milk", 0.5, "cup"),
        ("banana_frozen", 1.5, "cup"),
        ("cacao_powder", 2, "tbsp"),
        ("date", 2, "piece"),
    ], None),

    ("ds-field-strawberry-soft-serve", "Field Strawberry Soft Serve", "dessert", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("strawberry_frozen", 1, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("sea_moss", 1, "tsp"),
        ("lemon_juice", 1, "tsp"),
    ], "A teaspoon of sea moss gel is a flavourless thickener — it holds a dairy-free blend together the way egg yolk holds custard."),

    ("ds-pineapple-whip", "Pineapple Whip", "dessert", 1, 3, [
        ("coconut_water", 0.5, "cup"),
        ("pineapple_frozen", 1.5, "cup"),
        ("coconut_cream", 3, "tbsp"),
        ("lime_juice", 2, "tsp"),
    ], "Coconut cream, not coconut milk beverage — the thin carton stuff will not hold the swirl and you end up with pineapple juice."),

    ("ds-toasted-coconut-soft-serve", "Toasted Coconut Soft Serve", "dessert", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("coconut_frozen", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("coconut_shredded", 2, "tbsp"),
    ], None),

    ("ds-avocado-lime-freeze", "Avocado Lime Freeze", "dessert", 1, 4, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("avocado_frozen", 0.5, "cup"),
        ("banana_frozen", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("date", 2, "piece"),
    ], "Avocado in dessert is standard across Brazil and Vietnam; it brings fat and silk, and the lime keeps it from tasting like guacamole."),

    ("ds-fig-and-tahini-freeze", "Fig And Tahini Freeze", "dessert", 1, 4, [
        ("almond_milk", 0.5, "cup"),
        ("banana_frozen", 1, "cup"),
        ("fig_dried", 3, "piece"),
        ("tahini", 1, "tbsp"),
    ], "Snip the hard stem off each dried fig first — it never breaks down and it is the one bit you'll notice."),

    ("ds-palm-grove-shake", "Palm Grove Shake", "dessert", 1, 3, [
        ("almond_milk", 0.5, "cup"),
        ("banana_frozen", 1, "cup"),
        ("date", 4, "piece"),
        ("cinnamon", 0.5, "tsp"),
    ], "Medjool dates, not Deglet Noor — Medjools are soft enough to blend smooth and caramel enough that you need nothing else."),

    ("ds-soursop-freeze", "Soursop Freeze", "dessert", 1, 5, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("soursop", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("lime_juice", 2, "tsp"),
        ("date", 2, "piece"),
    ], "Soursop hides big black seeds in the pulp and they are bitter — pick them out by hand before anything goes near the blade."),

    ("ds-lucuma-cream", "Lucuma Cream", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("lucuma", 1, "tbsp"),
        ("date", 2, "piece"),
    ], "Lucuma tastes like maple and sweet potato had a fruit; it is subtle, so don't bury it under cocoa or coffee."),

    # ------------------------------------------------------ ice, sorbet, granita
    ("ds-sandia-granita", "Sandía Granita", "dessert", 1, 4, [
        ("water", 0.25, "cup"),
        ("watermelon_frozen", 1.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("mint", 1, "tbsp"),
    ], "Freeze the watermelon in cubes the night before and you need almost no added water, which is what keeps a granita from going slushy."),

    ("ds-espresso-granita", "Espresso Granita", "dessert", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("coffee_ice", 1, "cup"),
        ("ice", 0.5, "cup"),
        ("brown_sugar", 1, "tbsp"),
    ], "Sweeten the espresso while it is still hot so the sugar dissolves; stirred into a cold blend it stays gritty."),

    ("ds-blood-orange-ice", "Blood Orange Ice", "dessert", 1, 5, [
        ("orange_juice", 0.5, "cup"),
        ("blood_orange", 2, "piece"),
        ("ice", 1, "cup"),
        ("agave", 1, "tbsp"),
    ], None),

    ("ds-raspberry-rose-ice", "Raspberry Rose Ice", "dessert", 1, 3, [
        ("water", 0.5, "cup"),
        ("raspberry_frozen", 1.25, "cup"),
        ("rose_water", 0.5, "tsp"),
        ("sugar", 1, "tbsp"),
        ("lemon_juice", 2, "tsp"),
    ], "Rose water goes from lovely to soap at about a teaspoon — start with half and smell the cup before you add more."),

    ("ds-sicilian-lemon-ice", "Sicilian Lemon Ice", "dessert", 1, 4, [
        ("water", 0.5, "cup"),
        ("lemon_juice", 0.25, "cup"),
        ("ice", 1.25, "cup"),
        ("sugar", 2, "tbsp"),
        ("lemon_zest", 1, "tsp"),
    ], "Sugar and acid in roughly equal spoons is the sorbet ratio; too little sugar and it freezes into a solid lump rather than a slush."),

    ("ds-drowned-gelato", "Drowned Gelato", "dessert", 1, 2, [
        ("espresso", 0.33, "cup"),
        ("milk_whole", 0.25, "cup"),
        ("gelato", 1, "cup"),
        ("dutch_cocoa", 1, "tsp"),
    ], "Pull the espresso and let it cool thirty seconds before it hits the gelato, or the first half melts to soup before the blade turns."),

    ("ds-saigon-mocha-freeze", "Saigon Mocha Freeze", "dessert", 1, 3, [
        ("coffee", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 1, "cup"),
        ("dutch_cocoa", 1, "tsp"),
    ], None),

    ("ds-cold-brew-hazelnut-freeze", "Cold Brew Hazelnut Freeze", "dessert", 1, 3, [
        ("cold_brew", 0.33, "cup"),
        ("oat_milk", 0.33, "cup"),
        ("banana_frozen", 1, "cup"),
        ("hazelnut_butter", 1, "tbsp"),
        ("date", 2, "piece"),
    ], None),

    # -------------------------------------------- dark chocolate for grown-ups
    ("ds-cacao-and-chilli", "Cacao And Chilli", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("cacao_powder", 2, "tbsp"),
        ("cayenne", 0.25, "tsp"),
        ("date", 2, "piece"),
    ], "The heat should arrive after the chocolate, not with it — a quarter teaspoon is a warm finish, half is a dare."),

    ("ds-cacao-and-orange-peel", "Cacao And Orange Peel", "dessert", 1, 3, [
        ("orange_juice", 0.33, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("cacao_powder", 2, "tbsp"),
        ("orange_zest", 1, "tsp"),
        ("date_syrup", 1, "tbsp"),
    ], None),

    ("ds-bitter-chocolate-and-sea-salt", "Bitter Chocolate And Sea Salt", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 0.75, "cup"),
        ("dark_chocolate", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Chop the bar before it goes in; whole squares bounce off the blade and you end up with shards rather than a smooth blend."),

    ("ds-chocolate-tahini-freeze", "Chocolate Tahini Freeze", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("cacao_powder", 2, "tbsp"),
        ("tahini", 1, "tbsp"),
        ("date", 2, "piece"),
    ], "Stir the tahini jar all the way to the bottom first — the oil that sits on top is not the sesame paste you want here."),

    ("ds-halva-shake", "Halva Shake", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("tahini", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("sesame_seeds", 1, "tbsp"),
    ], "Tahini is bitter on its own and that is the point — the honey should only take the edge off, not cover it."),

    ("ds-mexican-chocolate-freeze", "Mexican Chocolate Freeze", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream_choc", 0.75, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("cinnamon", 1, "tsp"),
        ("cayenne", 0.25, "tsp"),
    ], None),

    ("ds-cacao-nib-crunch", "Cacao Nib Crunch", "dessert", 1, 3, [
        ("almond_milk", 0.5, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("cacao_nibs", 2, "tbsp"),
        ("date", 3, "piece"),
        ("salt", 0.25, "tsp"),
    ], "Nibs are unsweetened chocolate with no sugar and no fat added back, so they stay crunchy and bitter — the dates carry the sweetness."),

    ("ds-chocolate-and-olive-oil", "Chocolate And Olive Oil", "dessert", 2, 3, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("dark_chocolate", 2, "tbsp"),
        ("olive_oil", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Use the peppery green olive oil you'd finish a salad with, not the neutral cooking one; that bitterness is what makes this work."),

    # ----------------------------------------------------------- lighter shelf
    ("ds-one-banana-frozen", "One Banana, Frozen", "dessert", 1, 2, [
        ("water", 0.25, "cup"),
        ("banana_frozen", 1.5, "cup"),
        ("cinnamon", 0.5, "tsp"),
    ], "This is frozen banana and nothing else, and it is genuinely good — but it is not a milkshake, and it will not pretend to be one."),

    ("ds-lemon-frozen-yogurt", "Lemon Frozen Yogurt", "dessert", 1, 3, [
        ("milk_skim", 0.33, "cup"),
        ("greek_yogurt_nonfat", 0.75, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("ds-cookie-crumb-lite", "Cookie Crumb Lite", "dessert", 1, 3, [
        ("milk_skim", 0.75, "cup"),
        ("whey_cookies", 1, "piece"),
        ("banana_frozen", 0.75, "cup"),
        ("cacao_powder", 1, "tsp"),
    ], "A cookies-and-cream protein powder gets you the flavour without the cookies, but it will never have the rubble — accept that or eat the real one."),

    ("ds-light-caramel-malt", "Light Caramel Malt", "dessert", 1, 3, [
        ("milk_lactose_free", 0.75, "cup"),
        ("whey_vanilla", 1, "piece"),
        ("ice", 1, "cup"),
        ("caramel_sauce", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "One teaspoon of real caramel sauce plus salt beats three teaspoons of caramel syrup, because salt is what your tongue reads as caramel."),

    ("ds-lean-chocolate-thickshake", "Lean Chocolate Thickshake", "dessert", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("banana_frozen", 0.75, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("xanthan", 0.125, "tsp"),
    ], "An eighth of a teaspoon of xanthan is the whole difference between a thin protein shake and one that coats the glass — any more turns it slimy."),

    ("ds-light-cheesecake-cup", "Light Cheesecake Cup", "dessert", 1, 4, [
        ("milk_skim", 0.5, "cup"),
        ("cottage_cheese", 0.5, "cup"),
        ("strawberry_frozen", 0.75, "cup"),
        ("lemon_zest", 1, "tsp"),
        ("stevia", 0.25, "tsp"),
    ], None),

    ("ds-alphonso-freeze", "Alphonso Freeze", "dessert", 1, 3, [
        ("milk_skim", 0.33, "cup"),
        ("greek_yogurt_nonfat", 0.5, "cup"),
        ("mango_frozen", 1, "cup"),
        ("lime_juice", 2, "tsp"),
    ], None),

    ("ds-black-currant-skyr-freeze", "Black Currant Skyr Freeze", "dessert", 1, 4, [
        ("milk_skim", 0.5, "cup"),
        ("skyr", 0.5, "cup"),
        ("blackcurrant", 0.75, "cup"),
        ("honey", 2, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("ds-peanut-butter-lite", "Peanut Butter Lite", "dessert", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("peanut_powder", 3, "tbsp"),
        ("plant_protein", 1, "piece"),
    ], "Powdered peanut butter has most of the oil pressed out, so it tastes peanutty but blends thin — the frozen banana is carrying the body."),

    ("ds-sour-cherry-kefir-freeze", "Sour Cherry Kefir Freeze", "dessert", 1, 4, [
        ("kefir", 0.75, "cup"),
        ("cherry_sour", 0.75, "cup"),
        ("ice", 0.75, "cup"),
        ("honey", 2, "tsp"),
    ], None),

    # -------------------------------------------------------------- long tail
    ("ds-horchata-freeze", "Horchata Freeze", "dessert", 1, 4, [
        ("rice_milk", 0.75, "cup"),
        ("ice", 1, "cup"),
        ("almonds", 2, "tbsp"),
        ("cinnamon", 1, "tsp"),
        ("date_syrup", 1, "tbsp"),
    ], None),

    ("ds-pistachio-rose-freeze", "Pistachio And Rose", "dessert", 2, 4, [
        ("pistachio_milk", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("pistachio_butter", 2, "tbsp"),
        ("rose_water", 0.5, "tsp"),
        ("cardamom", 0.25, "tsp"),
    ], None),

    ("ds-guava-cream-cheese-freeze", "Guava And Queso", "dessert", 2, 5, [
        ("guava_nectar", 0.5, "cup"),
        ("cream_cheese", 3, "tbsp"),
        ("ice", 1, "cup"),
        ("lime_juice", 2, "tsp"),
        ("graham_cracker", 0.25, "cup"),
    ], None),

    ("ds-mango-sticky-rice-shake", "Mango Sticky Rice", "dessert", 2, 5, [
        ("coconut_milk_canned", 0.33, "cup"),
        ("mango_frozen", 1, "cup"),
        ("brown_rice", 0.33, "cup"),
        ("salt", 0.25, "tsp"),
        ("coconut_sugar", 1, "tbsp"),
    ], "The salt is not optional — mango sticky rice is a salty-sweet dish, and without it this just tastes like a mango smoothie."),

    ("ds-sesame-black-freeze", "Black Sesame Freeze", "dessert", 2, 4, [
        ("milk_whole", 0.5, "cup"),
        ("ice_cream", 0.75, "cup"),
        ("sesame_seeds", 3, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Toast the sesame hard, almost to the edge of burning; pale sesame gives you texture and no flavour at all."),

    ("ds-maple-pecan-nice-cream", "Maple Pecan Nice Cream", "dessert", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 1.25, "cup"),
        ("pecans", 2, "tbsp"),
        ("maple_extract", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Maple extract rather than syrup keeps this thick — syrup is liquid, and liquid is the enemy of a scoopable blend."),

    ("ds-coconut-lime-pie", "Coconut Lime Pie", "dessert", 2, 4, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("coconut_yogurt", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("graham_cracker", 0.25, "cup"),
        ("maple_syrup", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("ds-cornflake-milk-shake", "Cereal Milk", "dessert", 2, 4, [
        ("milk_whole", 0.75, "cup"),
        ("cornflakes", 0.75, "cup"),
        ("ice_cream", 0.5, "cup"),
        ("brown_sugar", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Let the cornflakes steep in the cold milk for five minutes before blending; that soak is the flavour, the blending is just texture."),

    ("ds-olive-oil-orange-sorbet", "Orange And Olive Oil Ice", "dessert", 1, 4, [
        ("orange_juice", 0.75, "cup"),
        ("ice", 1.25, "cup"),
        ("olive_oil", 1, "tsp"),
        ("orange_zest", 1, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "A dairy-free ice with a teaspoon of good olive oil comes out rounder and less icy, because fat is what mouthfeel is made of."),
]
