"""Frozen and blended cocktails for the Blast — shareable, bar-balanced, built for the CRUSH program."""

RECIPES = [
    # ---- margaritas, across fruit and smoke ----
    ("ck-fresa-brava", "Fresa Brava", "cocktail", 2, 5, [
        ("tequila", 2, "piece"),
        ("strawberry_frozen", 1, "cup"),
        ("margarita_mix", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("tajin", 0.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Wet the rim with a spent lime shell and roll it in Tajín before you blend, not after — the glass has to be dry-handed or the seasoning slides off."),

    ("ck-golden-hour-margarita", "Golden Hour Margarita", "cocktail", 2, 4, [
        ("tequila", 2, "piece"),
        ("mango_frozen", 1, "cup"),
        ("orange_juice", 0.25, "cup"),
        ("lime_juice", 0.25, "cup"),
        ("triple_sec", 2, "tbsp"),
        ("ice", 1, "cup"),
    ], "Taste it before you pour: anything this cold reads about a third less sweet than it did at room temperature, so a frozen margarita carries more sugar than a shaken one and still tastes dry."),

    ("ck-dusk-in-oaxaca", "Dusk in Oaxaca", "cocktail", 2, 5, [
        ("mezcal", 2, "piece"),
        ("date_syrup", 1.5, "tbsp"),
        ("lime_juice", 0.25, "cup"),
        ("orange_juice", 0.25, "cup"),
        ("tajin", 0.5, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Date syrup stands in for tamarind here — sticky, dark and a little sour, so hold back on other sweeteners until you've tasted."),

    ("ck-sandia-ahumada", "Sandía Ahumada", "cocktail", 2, 4, [
        ("mezcal", 2, "piece"),
        ("watermelon_frozen", 1, "cup"),
        ("watermelon_juice", 0.25, "cup"),
        ("lime_juice", 0.25, "cup"),
        ("agave", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Watermelon is mostly water, so it freezes hard and thins fast — keep the added ice low or you'll end up with pink slush that tastes of nothing."),

    ("ck-desert-bloom", "Desert Bloom", "cocktail", 2, 6, [
        ("tequila", 2, "piece"),
        ("prickly_pear", 2, "piece"),
        ("cactus_water", 0.5, "cup"),
        ("lime_juice", 0.25, "cup"),
        ("simple_syrup", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Peel prickly pear with a fork and a knife, never your fingers — the glochids are invisible and they sit in the skin."),

    ("ck-cool-heat-margarita", "Cool Heat Margarita", "cocktail", 2, 6, [
        ("tequila", 2, "piece"),
        ("cucumber", 0.5, "piece"),
        ("jalapeno", 0.5, "piece"),
        ("margarita_mix", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Scrape the seeds and white ribs out of the jalapeño — that's where the burn lives, and the green pepper flavour you actually want is in the flesh."),

    ("ck-smoke-and-serrano", "Smoke and Serrano", "cocktail", 2, 5, [
        ("mezcal", 2, "piece"),
        ("serrano", 0.5, "piece"),
        ("pineapple_juice", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Serrano is sharper and faster than jalapeño; start with half and blend for five seconds less than you think, because heat keeps climbing as it sits."),

    ("ck-laguna-azul", "Laguna Azul", "cocktail", 2, 4, [
        ("tequila", 2, "piece"),
        ("blue_curacao", 2, "tbsp"),
        ("limeade_frozen", 0.25, "cup"),
        ("pineapple_juice", 0.25, "cup"),
        ("ice", 1.25, "cup"),
    ], "Frozen limeade concentrate is sour and sweet in one spoon, which is why bars keep it around for slush drinks — no separate syrup needed."),

    # ---- daiquiris ----
    ("ck-havana-lime-freeze", "Havana Lime Freeze", "cocktail", 1, 3, [
        ("white_rum", 1, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("simple_syrup", 1.5, "tbsp"),
        ("water", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "There is nowhere to hide in a plain daiquiri — squeeze the lime to order, since bottled juice tastes cooked and the whole drink rests on it."),

    ("ck-golden-banana-freeze", "Golden Banana Freeze", "cocktail", 2, 4, [
        ("white_rum", 2, "piece"),
        ("banana_frozen", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("orange_juice", 0.5, "cup"),
        ("brown_sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Brown sugar rather than white — the molasses edge is what makes a banana daiquiri taste like rum instead of milkshake."),

    ("ck-maracuya-daiquiri", "Maracuyá Daiquiri", "cocktail", 2, 3, [
        ("white_rum", 2, "piece"),
        ("passionfruit_juice", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("simple_syrup", 1.5, "tbsp"),
        ("ice", 1.25, "cup"),
    ], None),

    ("ck-papa-doble-freeze", "Papa Doble Freeze", "cocktail", 2, 6, [
        ("white_rum", 2, "piece"),
        ("grapefruit", 1, "piece"),
        ("white_grape_juice", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("chambord", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Cut the white pith off the grapefruit segments before they go in; blended pith turns bitter in a way no amount of syrup fixes."),

    # ---- coladas and painkillers ----
    ("ck-tortola-painkiller", "Tortola Painkiller", "cocktail", 2, 4, [
        ("dark_rum", 2, "piece"),
        ("pineapple_juice", 0.5, "cup"),
        ("orange_juice", 0.25, "cup"),
        ("cream_of_coconut", 0.25, "cup"),
        ("nutmeg", 0.25, "tbsp"),
        ("ice", 1, "cup"),
    ], "Grate the nutmeg over the top after pouring rather than blending it in — the aroma is half the drink and it dies under the blade."),

    ("ck-toasted-colada", "Toasted Colada", "cocktail", 2, 5, [
        ("dark_rum", 2, "piece"),
        ("pina_colada_mix", 0.5, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("coconut_shredded", 2, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Toast the shredded coconut dry in a pan until it just colours, then let it cool — warm coconut will loosen the whole blend."),

    ("ck-lava-flow", "Lava Flow", "cocktail", 2, 5, [
        ("white_rum", 2, "piece"),
        ("strawberry_frozen", 0.75, "cup"),
        ("pina_colada_mix", 0.5, "cup"),
        ("banana", 0.5, "piece"),
        ("ice", 0.75, "cup"),
    ], "For the striped look, blend the strawberry alone first, spoon it into the glass, then blend the colada side and pour it down the middle."),

    # ---- mojitos ----
    ("ck-mojito-negro", "Mojito Negro", "cocktail", 2, 5, [
        ("white_rum", 2, "piece"),
        ("blackberry_frozen", 1, "cup"),
        ("mint", 2, "tbsp"),
        ("lemon_lime_soda", 0.5, "cup"),
        ("lime_juice", 0.25, "cup"),
        ("ice", 1, "cup"),
    ], "Clap the mint between your palms before it goes in; shredding it on the blade for too long turns it grassy and grey."),

    ("ck-coconut-mint-freeze", "Coconut Mint Freeze", "cocktail", 2, 4, [
        ("coconut_rum", 2, "piece"),
        ("mint", 2, "tbsp"),
        ("lime_juice", 0.25, "cup"),
        ("coconut_water", 0.5, "cup"),
        ("agave", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], None),

    # ---- palomas ----
    ("ck-paloma-rosada", "Paloma Rosada", "cocktail", 2, 5, [
        ("tequila", 2, "piece"),
        ("grapefruit", 1, "piece"),
        ("hibiscus_tea", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("agave", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Brew the hibiscus double strength and chill it — hot tea poured over ice in the cup melts your texture before the blade even turns."),

    ("ck-humo-y-toronja", "Humo y Toronja", "cocktail", 2, 5, [
        ("mezcal", 2, "piece"),
        ("grapefruit", 1, "piece"),
        ("cactus_water", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("agave", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "A pinch of salt on the rim does more for grapefruit than sugar does — it pushes the bitterness back and lets the fruit through."),

    # ---- prosecco and aperitivo ----
    ("ck-venetian-freeze", "Venetian Freeze", "cocktail", 2, 4, [
        ("peach_frozen", 1, "cup"),
        ("elderflower_liqueur", 2, "tbsp"),
        ("white_grape_juice", 0.5, "cup"),
        ("prosecco", 0.5, "cup"),
        ("ice", 0.5, "cup"),
    ], "Blend everything but the prosecco, then stir the prosecco in at the top of the cup — blending it flat wastes the only bubbles in the drink."),

    ("ck-rossini-freeze", "Rossini Freeze", "cocktail", 2, 3, [
        ("strawberry_frozen", 1, "cup"),
        ("white_grape_juice", 0.5, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("prosecco", 0.5, "cup"),
        ("ice", 0.5, "cup"),
    ], "Same rule as a Bellini: the wine goes in last, folded through with a spoon, never spun on the blade."),

    ("ck-sunday-mimosa-freeze", "Sunday Mimosa Freeze", "cocktail", 2, 3, [
        ("orange_juice", 0.75, "cup"),
        ("grand_marnier", 1, "tbsp"),
        ("orange_zest", 0.5, "tbsp"),
        ("prosecco", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "Zest the orange before you juice it — a spoon of zest is what separates this from orange juice with wine in it."),

    ("ck-aperol-sunset-slush", "Aperol Sunset Slush", "cocktail", 2, 3, [
        ("aperol", 0.25, "cup"),
        ("orange_juice", 0.5, "cup"),
        ("prosecco", 0.5, "cup"),
        ("ice", 1.25, "cup"),
    ], "Aperol is bitter-sweet already, so this needs no syrup at all — it needs acid, which is why the orange should be fresh rather than from a carton."),

    ("ck-campari-sorbetto", "Campari Sorbetto", "cocktail", 2, 4, [
        ("campari", 0.25, "cup"),
        ("orange_juice", 0.5, "cup"),
        ("sorbet", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Let the sorbet sit out two minutes before blending; rock-hard sorbet makes the blade cavitate and you'll be stirring the cup instead of drinking."),

    # ---- frosé and sangria ----
    ("ck-frose-hour", "Frosé Hour", "cocktail", 2, 4, [
        ("rose_wine", 0.75, "cup"),
        ("grapefruit", 1, "piece"),
        ("strawberry_frozen", 0.5, "cup"),
        ("simple_syrup", 1.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Freeze the rosé in an ice tray the night before and use those cubes in place of half the plain ice — it's the only way frosé doesn't taste watered."),

    ("ck-red-sangria-slush", "Red Sangria Slush", "cocktail", 2, 6, [
        ("red_wine", 0.75, "cup"),
        ("brandy", 1, "piece"),
        ("orange", 1, "piece"),
        ("apple_juice", 0.25, "cup"),
        ("cinnamon", 0.25, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Use a young, fruity red — anything oaky turns bitter and dusty once it's frozen and sweetened."),

    ("ck-kalimotxo-slush", "Kalimotxo Slush", "cocktail", 2, 3, [
        ("red_wine", 0.75, "cup"),
        ("cola", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Let the cola go flat on purpose first; blending fizzy cola builds pressure under the lid and foams over the moment you open it."),

    ("ck-orchard-sangria-slush", "Orchard Sangria Slush", "cocktail", 2, 6, [
        ("white_wine", 0.75, "cup"),
        ("apple_green", 1, "piece"),
        ("vermouth_dry", 2, "tbsp"),
        ("elderflower_liqueur", 1, "tbsp"),
        ("white_grape_juice", 0.25, "cup"),
        ("ice", 1.25, "cup"),
    ], "A splash of dry vermouth gives a white sangria the herbal backbone that fruit juice alone never gets to."),

    # ---- coffee and cream ----
    ("ck-midnight-oil", "Midnight Oil", "cocktail", 2, 4, [
        ("vodka", 2, "piece"),
        ("coffee_liqueur", 2, "tbsp"),
        ("espresso", 0.5, "cup"),
        ("coffee_ice", 0.75, "cup"),
        ("simple_syrup", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Freeze leftover espresso into a tray and use those cubes — coffee ice keeps it cold without diluting the coffee, which plain ice always does."),

    ("ck-dublin-fog", "Dublin Fog", "cocktail", 2, 5, [
        ("whiskey", 2, "piece"),
        ("coffee", 0.75, "cup"),
        ("brown_sugar", 1.5, "tbsp"),
        ("heavy_cream", 0.25, "cup"),
        ("ice", 1, "cup"),
    ], "Blend the coffee and whiskey first, then pulse the cream in for two seconds only — over-blended cream stiffens and you lose the float."),

    ("ck-cafe-bandido", "Café Bandido", "cocktail", 2, 3, [
        ("tequila", 2, "piece"),
        ("coffee_liqueur", 2, "tbsp"),
        ("cold_brew", 0.5, "cup"),
        ("cinnamon", 0.25, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Reposado works better than blanco here — the barrel sweetness meets the coffee halfway instead of fighting it."),

    ("ck-bushwacker", "Bushwacker", "cocktail", 2, 4, [
        ("dark_rum", 1, "piece"),
        ("coffee_liqueur", 2, "tbsp"),
        ("irish_cream", 2, "tbsp"),
        ("ice_cream", 0.5, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "This is a Gulf Coast beach drink and it lives or dies on thickness — if it pours rather than slumps, add ice cream, not more ice."),

    ("ck-alexander-on-ice", "Alexander on Ice", "cocktail", 2, 4, [
        ("brandy", 2, "piece"),
        ("creme_de_cacao", 2, "tbsp"),
        ("milk_whole", 0.5, "cup"),
        ("heavy_cream", 0.25, "cup"),
        ("nutmeg", 0.25, "tbsp"),
        ("ice", 1, "cup"),
    ], None),

    ("ck-grasshopper-freeze", "Grasshopper Freeze", "cocktail", 2, 3, [
        ("creme_de_menthe", 2, "tbsp"),
        ("creme_de_cacao", 2, "tbsp"),
        ("ice_cream", 0.75, "cup"),
        ("milk_whole", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Green crème de menthe colours it, white keeps it pale — the flavour is identical, so pick by the glass you're pouring into."),

    ("ck-roasted-almond-freeze", "Roasted Almond Freeze", "cocktail", 2, 3, [
        ("vodka", 1, "piece"),
        ("amaretto", 2, "tbsp"),
        ("coffee_liqueur", 2, "tbsp"),
        ("half_and_half", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], None),

    ("ck-chocolate-monkey", "Chocolate Monkey", "cocktail", 2, 4, [
        ("white_rum", 2, "piece"),
        ("banana_frozen", 1, "cup"),
        ("creme_de_cacao", 2, "tbsp"),
        ("milk_whole", 0.5, "cup"),
        ("chocolate_syrup", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "A pinch of salt in anything chocolate — it doesn't make the drink salty, it makes the cocoa taste like cocoa."),

    # ---- cachaça and pisco ----
    ("ck-caipirinha-freeze", "Caipirinha Freeze", "cocktail", 2, 5, [
        ("cachaca", 2, "piece"),
        ("lime", 1, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("sugar", 2, "tbsp"),
        ("water", 0.5, "cup"),
        ("ice", 1.5, "cup"),
    ], "Quarter the lime and cut out the white core before it goes in whole — that core is the bitter part, and a blender finds it instantly."),

    ("ck-caipifruta-maracuja", "Caipifruta Maracujá", "cocktail", 2, 5, [
        ("cachaca", 2, "piece"),
        ("passionfruit", 2, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("sugar", 1.5, "tbsp"),
        ("water", 0.5, "cup"),
        ("ice", 1.25, "cup"),
    ], "Leave some of the passion fruit seeds in and pulse rather than blend — the crunch is the point in Brazil, not a flaw."),

    ("ck-pisco-sour-freeze", "Pisco Sour Freeze", "cocktail", 2, 4, [
        ("pisco", 2, "piece"),
        ("lime_juice", 0.25, "cup"),
        ("simple_syrup", 2, "tbsp"),
        ("egg_white", 0.25, "cup"),
        ("water", 0.25, "cup"),
        ("ice", 1.25, "cup"),
    ], "Run it ten seconds longer than feels necessary — the egg white needs the extra time to build the foam cap that makes it a sour."),

    ("ck-lucuma-pisco-freeze", "Lúcuma Pisco Freeze", "cocktail", 2, 4, [
        ("pisco", 2, "piece"),
        ("lucuma", 2, "tbsp"),
        ("milk_whole", 0.5, "cup"),
        ("condensed_milk", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Lúcuma powder tastes like maple and sweet potato and it's very absorbent — add it last so it doesn't cake on the bottom of the cup."),

    # ---- savoury and beer ----
    ("ck-michelada-frappe", "Michelada Frappé", "cocktail", 1, 4, [
        ("beer", 0.75, "cup"),
        ("tomato_juice", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("worcestershire", 0.5, "tbsp"),
        ("hot_sauce", 0.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Pour the beer down the side of the cup and blend on the shortest run you can — the foam wants to climb, and a light lager gives you the most room."),

    ("ck-beerita-freeze", "Beerita Freeze", "cocktail", 2, 3, [
        ("beer", 0.75, "cup"),
        ("tequila", 1, "piece"),
        ("limeade_frozen", 0.25, "cup"),
        ("ice", 1.25, "cup"),
    ], "Let the beer sit open for ten minutes first; flat beer blends cleanly and the drink doesn't lose half its volume to foam."),

    ("ck-garden-mary-freeze", "Garden Mary Freeze", "cocktail", 1, 5, [
        ("vodka", 1, "piece"),
        ("tomato_juice", 0.75, "cup"),
        ("celery", 0.5, "piece"),
        ("lemon_juice", 2, "tbsp"),
        ("worcestershire", 0.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Blending the celery in rather than using it as a stirrer gives you the vegetal note all the way through instead of only at the first sip."),

    # ---- hibiscus, elderflower, limoncello ----
    ("ck-jamaica-rosa", "Jamaica Rosa", "cocktail", 2, 4, [
        ("gin", 2, "piece"),
        ("hibiscus_tea", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Steep hibiscus cold overnight instead of boiling it — hot water pulls out a tannic edge that fights the gin."),

    ("ck-elderflower-hedgerow", "Elderflower Hedgerow", "cocktail", 2, 5, [
        ("gin", 2, "piece"),
        ("elderflower_liqueur", 2, "tbsp"),
        ("cucumber", 0.5, "piece"),
        ("lemon_juice", 2, "tbsp"),
        ("white_grape_juice", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "Peel the cucumber if the skin is waxed; the wax is bitter and blending drives it through the whole drink."),

    ("ck-sorrel-freeze", "Sorrel Freeze", "cocktail", 2, 5, [
        ("dark_rum", 2, "piece"),
        ("hibiscus_tea", 0.75, "cup"),
        ("ginger", 0.5, "tbsp"),
        ("clove", 0.25, "tbsp"),
        ("brown_sugar", 1.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Cloves go a long way — a quarter spoon is the whole Caribbean Christmas note, and double that tastes like a cough drop."),

    ("ck-sgroppino-freeze", "Sgroppino Freeze", "cocktail", 2, 3, [
        ("vodka", 1, "piece"),
        ("limoncello", 2, "tbsp"),
        ("sorbet", 0.75, "cup"),
        ("prosecco", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Venetians serve this between courses, which is why it stays sharp — resist the urge to sweeten it, and fold the prosecco in off the blade."),

    ("ck-amalfi-blue", "Amalfi Blue", "cocktail", 2, 4, [
        ("limoncello", 0.25, "cup"),
        ("blueberry_frozen", 1, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("water", 0.5, "cup"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Keep the limoncello in the freezer — it won't solidify, and starting it that cold means less ice is needed to set the drink."),

    # ---- gin, aperitivo, and the rest of the back bar ----
    ("ck-negroni-frappe", "Negroni Frappé", "cocktail", 1, 4, [
        ("gin", 1, "piece"),
        ("campari", 1, "tbsp"),
        ("vermouth_sweet", 1, "tbsp"),
        ("orange_juice", 0.5, "cup"),
        ("orange_zest", 0.5, "tbsp"),
        ("ice", 1, "cup"),
    ], "Frozen bitterness lands harder than stirred, so the splash of orange juice isn't a shortcut — it's what keeps this drinkable at slush temperature."),

    ("ck-juniper-slush", "Juniper Slush", "cocktail", 2, 3, [
        ("gin", 2, "piece"),
        ("tonic_water", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("simple_syrup", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Blend the tonic in with everything else and accept it goes flat — quinine is what you're after here, not the fizz."),

    ("ck-melon-ball-freeze", "Melon Ball Freeze", "cocktail", 2, 5, [
        ("melon_liqueur", 0.25, "cup"),
        ("vodka", 1, "piece"),
        ("honeydew", 1, "cup"),
        ("pineapple_juice", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Freeze the honeydew cubes first — fresh melon is so watery that it blends to soup unless it comes in cold and hard."),

    ("ck-french-martini-freeze", "French Martini Freeze", "cocktail", 2, 3, [
        ("vodka", 2, "piece"),
        ("chambord", 2, "tbsp"),
        ("pineapple_juice", 0.75, "cup"),
        ("ice", 1.25, "cup"),
    ], "The foam on top comes from the pineapple juice, so use the kind with pulp and don't let it sit before you pour."),

    ("ck-fuzzy-navel-freeze", "Fuzzy Navel Freeze", "cocktail", 2, 3, [
        ("peach_schnapps", 0.25, "cup"),
        ("vodka", 1, "piece"),
        ("orange_juice", 0.75, "cup"),
        ("peach_frozen", 0.75, "cup"),
        ("ice", 0.5, "cup"),
    ], None),

    ("ck-lychee-sake-slush", "Lychee Sake Slush", "cocktail", 2, 5, [
        ("sake", 0.5, "cup"),
        ("lychee", 6, "piece"),
        ("white_grape_juice", 0.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Pit the lychees properly — the stones are slippery and hard enough to mark a blade."),

    ("ck-watermelon-soju-slush", "Watermelon Soju Slush", "cocktail", 2, 4, [
        ("soju", 0.5, "cup"),
        ("watermelon_frozen", 1, "cup"),
        ("watermelon_juice", 0.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "In Korea this gets served in the hollowed-out melon; in a Blast cup, the move is to keep it barely sweet so the fruit reads clean."),

    ("ck-peach-porch-bourbon", "Peach Porch Bourbon", "cocktail", 2, 5, [
        ("bourbon", 2, "piece"),
        ("peach_frozen", 1, "cup"),
        ("black_tea", 0.5, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Warm the honey with a spoon of hot water before it goes in, or it hits the cold peaches and seizes into a lump."),

    ("ck-whiskey-sour-freeze", "Whiskey Sour Freeze", "cocktail", 1, 4, [
        ("whiskey", 1, "piece"),
        ("lemon_juice", 2, "tbsp"),
        ("simple_syrup", 1.5, "tbsp"),
        ("egg_white", 0.25, "cup"),
        ("water", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "Two parts sour to one part sweet is the ratio to hold onto — then nudge the syrup up a touch because the cold flattens it."),

    ("ck-bluegrass-julep-freeze", "Bluegrass Julep Freeze", "cocktail", 2, 4, [
        ("bourbon", 2, "piece"),
        ("mint", 3, "tbsp"),
        ("simple_syrup", 2, "tbsp"),
        ("water", 0.5, "cup"),
        ("ice", 1.5, "cup"),
    ], "A julep is supposed to be crushed ice and nothing else, so this one wants the full ice load — frost on the outside of the cup means you got it right."),

    ("ck-dark-and-stormy-freeze", "Dark and Stormy Freeze", "cocktail", 2, 4, [
        ("dark_rum", 2, "piece"),
        ("ginger_beer", 0.75, "cup"),
        ("ginger", 0.5, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "A knob of fresh ginger alongside the ginger beer puts the heat back that blending takes out."),

    ("ck-bourbon-street-hurricane", "Bourbon Street Hurricane", "cocktail", 2, 4, [
        ("dark_rum", 1, "piece"),
        ("white_rum", 1, "piece"),
        ("passionfruit_juice", 0.5, "cup"),
        ("orange_juice", 0.25, "cup"),
        ("grenadine", 2, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Hold back the grenadine and drizzle it in after pouring — it sinks and gives you the sunset the drink is named for."),

    ("ck-spiced-pear-freeze", "Spiced Pear Freeze", "cocktail", 2, 5, [
        ("spiced_rum", 2, "piece"),
        ("pear", 1, "piece"),
        ("apple_juice", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("cinnamon", 0.25, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Use a pear that gives slightly at the neck; a firm one blends to grit and tastes of nothing at all."),

    ("ck-guava-bandera", "Guava Bandera", "cocktail", 2, 3, [
        ("tequila", 2, "piece"),
        ("guava_nectar", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("tajin", 0.25, "tbsp"),
        ("ice", 1.25, "cup"),
    ], "Guava nectar is already sweetened, so the lime here is doing structural work — don't cut it back."),

    ("ck-crimson-cooler", "Crimson Cooler", "cocktail", 2, 4, [
        ("gin", 2, "piece"),
        ("cranberry_frozen", 0.75, "cup"),
        ("cranberry_juice", 0.5, "cup"),
        ("orange_zest", 0.5, "tbsp"),
        ("simple_syrup", 2, "tbsp"),
        ("ice", 1, "cup"),
    ], "Raw cranberries are aggressively sour, so this needs roughly twice the syrup you'd use with any other berry."),

    ("ck-cherry-amaretto-chill", "Cherry Amaretto Chill", "cocktail", 2, 4, [
        ("bourbon", 1, "piece"),
        ("amaretto", 0.25, "cup"),
        ("cherry_frozen", 1, "cup"),
        ("cherry_juice", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Amaretto and cherry stone are the same almond note, which is why this tastes like one ingredient rather than two."),

    ("ck-blood-orange-fizz-freeze", "Blood Orange Fizz Freeze", "cocktail", 2, 5, [
        ("vodka", 1, "piece"),
        ("blood_orange", 2, "piece"),
        ("white_grape_juice", 0.5, "cup"),
        ("elderflower_liqueur", 1, "tbsp"),
        ("prosecco", 0.5, "cup"),
        ("ice", 1, "cup"),
    ], "Blood oranges fade to brown once cut, so segment them straight into the cup and blend right away to keep the colour."),
]
