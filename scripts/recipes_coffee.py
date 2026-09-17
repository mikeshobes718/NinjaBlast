"""Coffee, tea and cacao drinks for the Blast: frappés, fat coffees, matcha and chai."""

RECIPES = [
    # ------------------------------------------------ frappés and café classics
    ("cf-athens-frappe", "Athens Frappé", "coffee", 1, 3, [
        ("instant_coffee", 1, "tbsp"),
        ("water", 0.5, "cup"),
        ("evaporated_milk", 2, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Greek frappé is foam first — give the instant coffee, sugar and a splash of the water ten seconds on their own before the ice and milk join them."),

    ("cf-saigon-ice", "Saigon Ice", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("coffee_ice", 0.75, "cup"),
        ("ice", 0.25, "cup"),
    ], "Frozen coffee cubes instead of plain ice are what keep this from melting into brown water halfway down the cup."),

    ("cf-cafe-bombon", "Café Bombón Freeze", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("condensed_milk", 1.5, "tbsp"),
        ("milk_whole", 0.25, "cup"),
        ("ice", 1, "cup"),
    ], None),

    ("cf-brown-sugar-shakerato", "Brown Sugar Shakerato", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("oat_milk_barista", 0.5, "cup"),
        ("brown_sugar", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "Barista oat milk is formulated not to split against espresso — the regular kind can curdle at the edges."),

    ("cf-cafe-de-olla", "Café de Olla Freeze", "coffee", 1, 4, [
        ("coffee", 0.75, "cup"),
        ("molasses", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("orange_zest", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], "Molasses stands in for piloncillo here; a full tablespoon tastes assertive warm and lands about right once it is frozen."),

    ("cf-cardamom-turkish", "Cardamom Turkish Freeze", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("milk_whole", 0.25, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Cardamom belongs in with the coffee rather than sprinkled on top — it needs the liquid to open up."),

    ("cf-horchata-cafe", "Horchata con Café", "coffee", 1, 3, [
        ("rice_milk", 0.75, "cup"),
        ("coffee", 0.5, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("condensed_milk", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Rice milk is thin, so the cinnamon carries the body here — use more than feels sensible."),

    ("cf-midnight-mocktini", "Midnight Mocktini", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("cold_brew", 0.25, "cup"),
        ("simple_syrup", 1, "tbsp"),
        ("vanilla_extract", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "The crema is the whole point, so pull the espresso straight into the cup and blend it while it is still fresh."),

    # ------------------------------------------------------ mochas, cacao range
    ("cf-dutch-process-mocha", "Dutch Process Mocha", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("dutch_cocoa", 1.5, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Dutch cocoa is alkalised, so it reads rounder and darker than natural cacao and needs less sugar to stop it tasting sharp."),

    ("cf-seventy-percent-mocha", "Seventy Percent Mocha", "coffee", 1, 4, [
        ("coffee", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("dark_chocolate", 2, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Salt is not optional in anything chocolate — a quarter teaspoon is the difference between bitter and deep."),

    ("cf-white-velvet-mocha", "White Velvet Mocha", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("white_chocolate", 2, "tbsp"),
        ("vanilla_bean", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("cf-oaxaca-mocha", "Oaxaca Mocha", "coffee", 1, 4, [
        ("coffee", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("cayenne", 0.25, "tsp"),
        ("coconut_sugar", 1, "tbsp"),
    ], "Cayenne and cacao are an old pairing — the heat should arrive after the chocolate, not with it, so keep it to a scant quarter teaspoon."),

    ("cf-deep-cocoa-cup", "Deep Cocoa Cup", "coffee", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("dutch_cocoa", 2, "tbsp"),
        ("espresso_powder", 0.5, "tsp"),
        ("maple_syrup", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Espresso powder deepens a chocolate drink without tasting of coffee; half a teaspoon does it, a whole one tips it into mocha."),

    # ------------------------------------------------------------- fat coffees
    ("cf-ghee-coffee-ritual", "Ghee Coffee Ritual", "coffee", 1, 3, [
        ("coffee", 1, "cup"),
        ("ghee", 1, "tsp"),
        ("mct_oil", 1, "tbsp"),
        ("collagen", 1, "piece"),
        ("salt", 0.25, "tsp"),
    ], "Fat coffee has to be blended rather than stirred — run the full cycle or it separates into a slick before you finish the cup."),

    ("cf-mct-cold-start", "MCT Cold Start", "coffee", 1, 2, [
        ("cold_brew", 0.5, "cup"),
        ("water", 0.5, "cup"),
        ("mct_oil", 1, "tbsp"),
        ("lions_mane", 1, "tsp"),
        ("allulose", 1, "tbsp"),
    ], "Start MCT oil at a teaspoon and work up; a full tablespoon on an empty stomach is a lot the first time."),

    ("cf-keto-cocoa-espresso", "Keto Cocoa Espresso", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("coconut_milk_canned", 0.25, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("erythritol", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Erythritol reads cold on the tongue, which suits a frozen drink and would taste strange in the same recipe served hot."),

    ("cf-buttered-collagen-black", "Buttered Collagen Black", "coffee", 1, 3, [
        ("coffee", 0.75, "cup"),
        ("butter", 1, "tsp"),
        ("collagen", 1, "piece"),
        ("cinnamon", 0.25, "tsp"),
        ("maple_syrup", 1, "tsp"),
    ], None),

    # --------------------------------------------------------- whipped builds
    ("cf-dalgona-cloud", "Dalgona Cloud", "coffee", 1, 3, [
        ("instant_coffee", 1, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("water", 2, "tbsp"),
        ("milk_2", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], "Only instant coffee whips — brewed coffee and espresso will never build that foam, however long you run the blade."),

    ("cf-snowcap-matcha", "Snowcap Matcha", "coffee", 1, 3, [
        ("matcha", 1, "tsp"),
        ("water", 0.25, "cup"),
        ("condensed_milk", 1.5, "tbsp"),
        ("milk_2", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "Matcha clumps unless it meets liquid first — wet it with the water at the bottom of the cup before the milk and ice go in."),

    # ------------------------------------------------------------- affogato-ish
    ("cf-nocciola-affogato", "Nocciola Affogato", "coffee", 2, 3, [
        ("espresso", 0.25, "cup"),
        ("gelato", 0.5, "cup"),
        ("hazelnut_butter", 1, "tbsp"),
        ("milk_whole", 0.25, "cup"),
    ], "Add the espresso last and blend in short bursts; long blending melts the gelato and you lose the thickness that makes it an affogato."),

    ("cf-olive-oil-affogato", "Olive Oil Affogato", "coffee", 2, 3, [
        ("espresso", 0.25, "cup"),
        ("ice_cream", 0.5, "cup"),
        ("olive_oil", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("milk_whole", 0.25, "cup"),
    ], "Use a grassy, peppery olive oil rather than a mild one — with vanilla and salt it reads as savoury caramel."),

    # -------------------------------------------------------- indulgent brews
    ("cf-burnt-sugar-cold-brew", "Burnt Sugar Cold Brew", "coffee", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("caramel_sauce", 2, "tbsp"),
        ("lucuma", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("coffee_ice", 0.5, "cup"),
    ], "Lucuma tastes like caramel left in the sun; it stretches the caramel sauce so you can use less of it."),

    ("cf-tahini-halva-coffee", "Tahini Halva Coffee", "coffee", 1, 4, [
        ("espresso", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("tahini", 1, "tbsp"),
        ("date", 2, "piece"),
        ("sesame_seeds", 1, "tsp"),
    ], "Stir the tahini jar down to the bottom first — the separated oil on top is what makes it blend smooth instead of gritty."),

    ("cf-pistachio-rose-latte", "Pistachio Rose Latte", "coffee", 1, 3, [
        ("espresso", 0.25, "cup"),
        ("pistachio_milk", 0.75, "cup"),
        ("rose_water", 0.5, "tsp"),
        ("honey", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Rose water goes from perfume to soap in about half a teaspoon, so measure it rather than pouring."),

    # --------------------------------------------------------------- tea builds
    ("cf-bangkok-street-tea", "Bangkok Street Tea", "coffee", 1, 4, [
        ("black_tea", 0.75, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("evaporated_milk", 0.25, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "Brew the tea at double strength and chill it first — a cup of ice dilutes everything by roughly half."),

    ("cf-masala-chai-chill", "Masala Chai Chill", "coffee", 1, 3, [
        ("chai_concentrate", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("ginger", 1, "tsp"),
        ("ice", 1, "cup"),
    ], "Fresh ginger and extra cardamom wake up bottled chai concentrate, which is usually sweet and shy on spice."),

    ("cf-bergamot-fog", "Bergamot Fog", "coffee", 1, 4, [
        ("black_tea", 0.75, "cup"),
        ("oat_milk_barista", 0.5, "cup"),
        ("orange_zest", 0.5, "tsp"),
        ("vanilla_bean", 0.5, "tsp"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Orange zest stands in for the bergamot in Earl Grey — take only the coloured skin, the white pith under it is bitter."),

    ("cf-roast-house-tea", "Roast House Tea Latte", "coffee", 1, 4, [
        ("black_tea", 0.75, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("brown_sugar", 1, "tbsp"),
        ("sesame_seeds", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Toast the sesame in a dry pan for a minute first; that roasted edge is what makes this taste like hōjicha rather than plain tea."),

    ("cf-kyoto-cloud", "Kyoto Cloud", "coffee", 1, 3, [
        ("matcha", 1, "tsp"),
        ("water", 0.25, "cup"),
        ("oat_milk", 0.75, "cup"),
        ("agave", 2, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("cf-matcha-mango-wave", "Matcha Mango Wave", "coffee", 1, 3, [
        ("matcha", 1, "tsp"),
        ("coconut_water", 0.5, "cup"),
        ("mango_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tsp"),
        ("honey", 1, "tsp"),
    ], None),

    ("cf-sencha-citrus-snow", "Sencha Citrus Snow", "coffee", 1, 3, [
        ("green_tea", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("lime_zest", 0.5, "tsp"),
        ("stevia", 0.25, "tsp"),
        ("ice", 1.25, "cup"),
    ], "Brew the green tea just off the boil and no longer than two minutes — scalded tea turns bitter, and cold makes that worse."),

    ("cf-sorrel-cold-brew", "Sorrel Cold Brew", "coffee", 1, 3, [
        ("hibiscus_tea", 0.75, "cup"),
        ("cold_brew", 0.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("allulose", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Hibiscus is tart enough to read as fruit, so this needs far less sweetener than any milk-based coffee."),

    # ------------------------------------------------------------- yerba maté
    ("cf-mate-verde-lift", "Mate Verde Lift", "coffee", 1, 3, [
        ("yerba_mate", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("mint", 1, "tbsp"),
        ("honey", 2, "tsp"),
        ("ice", 1, "cup"),
    ], "Slap the mint between your palms before it goes in — bruising releases the oil, while shredding it on the blade just tastes green."),

    ("cf-mate-cacao-charge", "Mate Cacao Charge", "coffee", 1, 3, [
        ("yerba_mate", 0.75, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"),
        ("maca", 1, "tsp"),
        ("almond_butter", 1, "tbsp"),
    ], "Maca is malty and faintly bitter; the cacao and banana are what make it taste deliberate rather than like a supplement."),

    # -------------------------------------------------- evening and light cups
    ("cf-midnight-decaf-mocha", "Midnight Decaf Mocha", "coffee", 1, 3, [
        ("coffee_decaf", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("dutch_cocoa", 1, "tbsp"),
        ("honey", 2, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("cf-chamomile-decaf-cream", "Chamomile Decaf Cream", "coffee", 1, 3, [
        ("coffee_decaf", 0.5, "cup"),
        ("chamomile_tea", 0.5, "cup"),
        ("oat_milk", 0.25, "cup"),
        ("vanilla_bean", 0.5, "tsp"),
        ("allulose", 1, "tbsp"),
    ], "Chamomile turns bitter past about five minutes of steeping, and that bitterness stacks with the coffee."),

    ("cf-black-velvet-cold-brew", "Black Velvet Cold Brew", "coffee", 1, 2, [
        ("cold_brew", 0.5, "cup"),
        ("water", 0.5, "cup"),
        ("coffee_ice", 0.5, "cup"),
        ("vanilla_extract", 0.25, "tsp"),
        ("stevia", 0.25, "tsp"),
    ], "Cold brew is far less acidic than drip, so it takes sweetener differently — start at half what you would use in iced drip, then taste."),

    ("cf-peppermint-espresso-frost", "Peppermint Espresso Frost", "coffee", 1, 2, [
        ("espresso", 0.5, "cup"),
        ("water", 0.25, "cup"),
        ("peppermint_extract", 0.25, "tsp"),
        ("erythritol", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Peppermint extract is brutal by volume: a quarter teaspoon flavours the whole cup, half a teaspoon tastes like toothpaste."),

    # ------------------------------------------- protein and breakfast builds
    ("cf-cold-brew-vanilla-lift", "Cold Brew Vanilla Lift", "coffee", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("milk_skim", 0.5, "cup"),
        ("whey_vanilla", 1, "piece"),
        ("coffee_ice", 0.75, "cup"),
    ], "Freeze whatever coffee is left in the pot in an ice tray — those cubes are the single best upgrade to any blended iced coffee."),

    ("cf-doppio-power-shake", "Doppio Power Shake", "coffee", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("whey_isolate", 1, "piece"),
        ("banana_frozen", 0.5, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Let the espresso sit a minute before it meets the whey; near-boiling liquid makes the protein seize into lumps."),

    ("cf-cocoa-cold-brew-recovery", "Cocoa Cold Brew Recovery", "coffee", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("water", 0.25, "cup"),
        ("whey_chocolate", 1, "piece"),
        ("coffee_ice", 0.5, "cup"),
        ("cacao_nibs", 1, "tsp"),
    ], None),

    ("cf-matcha-morning-build", "Matcha Morning Build", "coffee", 1, 3, [
        ("matcha", 1, "tsp"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("banana_frozen", 0.5, "cup"),
        ("honey", 1, "tsp"),
    ], None),

    ("cf-chai-protein-chill", "Chai Protein Chill", "coffee", 1, 3, [
        ("chai_concentrate", 0.5, "cup"),
        ("almond_milk", 0.5, "cup"),
        ("whey_vanilla", 1, "piece"),
        ("ginger_ground", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("cf-velvet-cottage-coffee", "Velvet Cottage Coffee", "coffee", 1, 4, [
        ("cottage_cheese", 0.5, "cup"),
        ("cold_brew", 0.5, "cup"),
        ("milk_skim", 0.25, "cup"),
        ("maple_syrup", 1, "tbsp"),
        ("coffee_ice", 0.5, "cup"),
    ], "Cottage cheese only goes properly smooth if it starts with the liquid and runs the whole cycle; stop early and it stays grainy."),

    ("cf-cold-brew-peanut-bar", "Cold Brew Peanut Bar", "coffee", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("peanut_powder", 0.25, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("cacao_powder", 1, "tsp"),
    ], "Powdered peanut butter carries the flavour with a fraction of the oil, so the shake stays drinkable instead of claggy."),

    ("cf-cinnamon-cold-brew-oats", "Cinnamon Cold Brew Oats", "coffee", 1, 4, [
        ("cold_brew", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("oats", 3, "tbsp"),
        ("date", 2, "piece"),
        ("cinnamon", 0.5, "tsp"),
    ], "Soak the oats in the cold brew for five minutes before you blend and the texture goes from sandy to creamy."),

    ("cf-chai-oat-sunrise", "Chai Oat Sunrise", "coffee", 1, 4, [
        ("chai_concentrate", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("oats", 3, "tbsp"),
        ("banana", 0.5, "piece"),
        ("cardamom", 0.25, "tsp"),
    ], None),

    ("cf-matcha-chia-start", "Matcha Chia Start", "coffee", 1, 4, [
        ("matcha", 1, "tsp"),
        ("coconut_milk_bev", 0.75, "cup"),
        ("chia", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"),
        ("maple_syrup", 2, "tsp"),
    ], "Add the chia at the end and give it two minutes before drinking — straight in, it clumps around the blade."),

    ("cf-yerba-breakfast-boost", "Yerba Breakfast Boost", "coffee", 1, 3, [
        ("yerba_mate", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"),
        ("banana_frozen", 0.5, "cup"),
        ("almond_butter", 1, "tbsp"),
    ], None),

    ("cf-espresso-meringue-shake", "Espresso Meringue Shake", "coffee", 1, 3, [
        ("egg_white", 0.5, "cup"),
        ("espresso", 0.25, "cup"),
        ("milk_skim", 0.5, "cup"),
        ("allulose", 1, "tbsp"),
        ("coffee_ice", 0.5, "cup"),
    ], "Use pasteurised whites from a carton rather than a shell egg, and run it long enough to build the foam on top."),

    ("cf-tofu-mocha-silk", "Tofu Mocha Silk", "coffee", 1, 3, [
        ("silken_tofu", 0.5, "cup"),
        ("coffee", 0.5, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("date_syrup", 1, "tbsp"),
        ("coffee_ice", 0.5, "cup"),
    ], "Silken tofu is the dairy-free route to milkshake texture; drain the packing water or the drink tastes faintly of the box."),

    ("cf-speculoos-cold-brew", "Speculoos Cold Brew", "coffee", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("whey_cookies", 1, "piece"),
        ("biscoff", 0.25, "cup"),
        ("coffee_ice", 0.5, "cup"),
    ], None),

    ("cf-rooibos-vanilla-wind-down", "Rooibos Vanilla Wind-Down", "coffee", 1, 3, [
        ("rooibos_tea", 0.75, "cup"),
        ("pea_milk", 0.25, "cup"),
        ("whey_vanilla", 1, "piece"),
        ("date", 1, "piece"),
        ("nutmeg", 0.25, "tsp"),
    ], "Rooibos carries no caffeine at all, which makes it the one tea base that still works as a shake after dinner."),

    ("cf-late-shift-decaf", "Late Shift Decaf", "coffee", 1, 3, [
        ("coffee_decaf", 0.5, "cup"),
        ("milk_2", 0.5, "cup"),
        ("casein", 1, "piece"),
        ("almond_butter", 1, "tbsp"),
        ("reishi", 1, "tsp"),
    ], "Casein keeps thickening as it stands, so drink it within a few minutes or blend it looser than you think you want."),

    ("cf-cold-brew-banana-oats", "Cold Brew Banana Oats", "coffee", 1, 4, [
        ("cold_brew", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("oats", 3, "tbsp"),
        ("almond_butter", 1, "tbsp"),
    ], None),
]
