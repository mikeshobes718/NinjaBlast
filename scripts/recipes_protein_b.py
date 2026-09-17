"""Plant-only protein blends — no dairy, egg, honey or anything else from an animal."""

RECIPES = [
    ("pr2-halva-hour", "Halva Hour", "protein", 1, 3, [
        ("soy_milk", 1, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("tahini", 2, "tbsp"),
        ("date", 2, "piece"),
        ("salt", 0.25, "tsp"),
    ], "The sesame fat and the pinch of salt are what bury the chalky edge of plant protein — leave either out and you taste the powder."),

    ("pr2-horchata-lift", "Horchata Lift", "protein", 1, 4, [
        ("rice_milk", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"),
        ("almonds", 2, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("date", 2, "piece"),
    ], "Soak the almonds in hot water for ten minutes first; they break down far smoother and you avoid the gritty bits at the bottom."),

    ("pr2-bangkok-iced-tea", "Bangkok Iced Tea", "protein", 1, 4, [
        ("black_tea", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("coconut_milk_light", 0.25, "cup"),
        ("date_syrup", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Brew the tea at double strength and chill it — normal-strength tea disappears completely behind a scoop of protein."),

    ("pr2-cardamom-chai-builder", "Cardamom Chai Builder", "protein", 1, 3, [
        ("chai_concentrate", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"),
        ("oats", 0.25, "cup"),
        ("cardamom", 0.25, "tsp"),
    ], "Ground cardamom loses its oils fast, so crush green pods yourself if you have them and use a scant quarter teaspoon."),

    ("pr2-turkish-coffee-cacao", "Turkish Coffee Cacao", "protein", 1, 3, [
        ("espresso", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("cacao_powder", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Let the espresso cool before it goes in — hot liquid makes plant protein foam up and climb the cup."),

    ("pr2-street-corn-recovery", "Street Corn Recovery", "protein", 1, 5, [
        ("soy_milk", 0.75, "cup"),
        ("silken_tofu", 0.5, "cup"),
        ("corn_frozen", 0.5, "cup"),
        ("hemp_hearts", 3, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("tajin", 0.5, "tsp"),
    ], "Blend the corn with the lime juice first for twenty seconds — the kernel skins need the head start or they stay as specks."),

    ("pr2-miso-caramel-cloud", "Miso Caramel Cloud", "protein", 1, 4, [
        ("silken_tofu", 1, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("date_syrup", 1.5, "tbsp"),
        ("miso", 0.5, "tbsp"),
        ("hemp_hearts", 2, "tbsp"),
        ("vanilla_extract", 0.5, "tsp"),
    ], "White miso plus date syrup reads as salted caramel — but drain the tofu's packing water or the whole thing goes thin and beany."),

    ("pr2-toasted-sesame-silk", "Toasted Sesame Silk", "protein", 1, 4, [
        ("silken_tofu", 1, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("sesame_seeds", 3, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Toast the sesame in a dry pan until it smells nutty and let it cool — raw seeds taste flat and never bring the roasted note."),

    ("pr2-butterfly-blue-cloud", "Butterfly Blue Cloud", "protein", 1, 3, [
        ("pea_milk", 1, "cup"),
        ("plant_protein", 1, "piece"),
        ("banana_frozen", 0.5, "cup"),
        ("coconut_butter", 1, "tbsp"),
        ("blue_matcha", 0.5, "tsp"),
    ], "Butterfly pea powder is colour, not flavour; the coconut butter is what carries it, so warm the jar in your hands if it has set hard."),

    ("pr2-pistachio-matcha-cloud", "Pistachio Matcha Cloud", "protein", 1, 3, [
        ("pistachio_milk", 0.75, "cup"),
        ("soy_protein", 1, "piece"),
        ("silken_tofu", 0.5, "cup"),
        ("matcha", 0.5, "tsp"),
        ("maple_syrup", 1, "tbsp"),
    ], "Soy isolate is the most neutral of the plant powders, which is the only reason the matcha still comes through here."),

    ("pr2-cold-brew-cacao-crush", "Night Shift Crush", "protein", 1, 3, [
        ("cold_brew", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("cacao_nibs", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Add the nibs at the end and give it one short pulse if you want the crunch to survive the crush program."),

    ("pr2-mole-noir", "Mole Noir", "protein", 1, 3, [
        ("soy_milk", 1, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("almond_butter", 1, "tbsp"),
        ("cinnamon", 0.25, "tsp"),
        ("cayenne", 0.25, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Cayenne with cacao is an old pairing — start at a quarter teaspoon, because the heat keeps building for a minute after you taste it."),

    ("pr2-mango-chili-rebuild", "Chili Lime Mango Lift", "protein", 1, 3, [
        ("mango_frozen", 1, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("tajin", 0.5, "tsp"),
    ], "Pea protein is the bitterest of the bunch; a full tablespoon of lime juice is doing real work here, not just seasoning."),

    ("pr2-guava-silk", "Guava Silk", "protein", 1, 4, [
        ("guava_nectar", 0.5, "cup"),
        ("silken_tofu", 1, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("hemp_hearts", 3, "tbsp"),
        ("lime_juice", 1, "tbsp"),
    ], "No powder in this one at all — silken tofu and hemp hearts do it, and the lime keeps the guava from turning cloying."),

    ("pr2-soursop-and-hemp", "Soursop and Hemp", "protein", 1, 4, [
        ("soursop", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("hemp_protein", 1, "piece"),
        ("agave", 1, "tbsp"),
        ("lime_juice", 0.5, "tbsp"),
    ], "Hemp protein is earthy and green-tasting on its own; soursop's sourness is one of the few fruits strong enough to cover it."),

    ("pr2-lychee-rose-silk", "Lychee Rose Silk", "protein", 1, 5, [
        ("silken_tofu", 1, "cup"),
        ("lychee", 6, "piece"),
        ("pea_milk", 0.5, "cup"),
        ("hemp_hearts", 2, "tbsp"),
        ("rose_water", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Rose water goes from perfume to soap in about a quarter teaspoon, so measure it rather than pouring from the bottle."),

    ("pr2-persimmon-tahini-oats", "Persimmon Tahini Oats", "protein", 1, 4, [
        ("persimmon", 1, "piece"),
        ("soy_milk", 1, "cup"),
        ("plant_protein", 1, "piece"),
        ("tahini", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
    ], "Use a Fuyu persimmon you can slice like an apple; an underripe Hachiya will leave your mouth feeling stripped."),

    ("pr2-fig-and-cardamom", "Sticky Fig Cardamom", "protein", 1, 4, [
        ("fig_dried", 3, "piece"),
        ("soy_milk", 1, "cup"),
        ("plant_protein", 1, "piece"),
        ("walnuts", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
    ], "Snip the hard stems off the figs and soak them five minutes in hot water — dry figs bounce around the blade and stay in chunks."),

    ("pr2-prickly-pear-rebuild", "Prickly Pear Rebuild", "protein", 1, 5, [
        ("prickly_pear", 1, "piece"),
        ("pea_milk", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Prickly pear seeds are hard as gravel and the Blast won't beat them, so scoop the flesh and press it through a fork first."),

    ("pr2-sorrel-hibiscus-cooler", "Sorrel Hibiscus Cooler", "protein", 1, 4, [
        ("hibiscus_tea", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("raspberry_frozen", 0.75, "cup"),
        ("ginger", 0.5, "tsp"),
        ("agave", 1, "tbsp"),
    ], "Brew the hibiscus strong and cold-steep it overnight if you can — boiled hibiscus goes flat and slightly stewed."),

    ("pr2-black-currant-fix", "Black Currant Fix", "protein", 1, 3, [
        ("blackcurrant", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("soy_protein", 1, "piece"),
        ("maple_syrup", 1, "tbsp"),
    ], "Black currants are sharper than they look; taste before you add the second spoon of maple, not after."),

    ("pr2-date-and-espresso-oats", "Date and Espresso Oats", "protein", 1, 4, [
        ("espresso", 0.5, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"),
        ("oats", 0.25, "cup"),
        ("date", 2, "piece"),
        ("salt", 0.25, "tsp"),
    ], "Pit the dates and tear them in half before they go in; a whole Medjool will jam under the blade every time."),

    ("pr2-peanut-ginger-crush", "Peanut Ginger Crush", "protein", 1, 4, [
        ("soy_milk", 0.75, "cup"),
        ("peanut_powder", 0.25, "cup"),
        ("plant_protein", 1, "piece"),
        ("banana_frozen", 0.5, "cup"),
        ("ginger", 0.5, "tsp"),
        ("lime_juice", 0.5, "tbsp"),
    ], "Powdered peanut butter needs a full thirty seconds to hydrate or it sits in dry pockets — blend, wait, blend again."),

    ("pr2-iron-mocha", "Iron Mocha", "protein", 1, 4, [
        ("firm_tofu", 0.5, "cup"),
        ("coffee", 0.75, "cup"),
        ("soy_milk", 0.25, "cup"),
        ("cacao_powder", 1.5, "tbsp"),
        ("date_syrup", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Firm tofu is dense enough to stall the blade, so cube it small and give this a longer run than you think it needs."),

    ("pr2-edamame-mint-cooler", "Edamame Mint Cooler", "protein", 1, 4, [
        ("edamame", 0.75, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("hemp_hearts", 2, "tbsp"),
        ("mint", 1, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 1, "tbsp"),
    ], "Buy the edamame already shelled and run it from frozen — thawed beans go mealy and the drink loses its colour."),

    ("pr2-white-bean-vanilla-cream", "White Bean Vanilla Cream", "protein", 1, 3, [
        ("white_beans", 0.5, "cup"),
        ("soy_milk", 1, "cup"),
        ("plant_protein", 1, "piece"),
        ("vanilla_bean", 0.5, "tsp"),
        ("maple_syrup", 1, "tbsp"),
    ], "Rinse canned white beans until the water runs clear; the starchy tin liquid is the entire reason people think beans taste wrong in a shake."),

    ("pr2-chickpea-cookie-dough", "Chickpea Cookie Dough", "protein", 1, 4, [
        ("chickpeas", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("almond_butter", 1, "tbsp"),
        ("dark_chocolate", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Slip the skins off the chickpeas between your fingers — it takes two minutes and is the difference between creamy and grainy."),

    ("pr2-black-bean-brownie-blend", "Black Bean Brownie Blend", "protein", 1, 4, [
        ("black_beans", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("dutch_cocoa", 1, "tbsp"),
        ("date", 2, "piece"),
        ("salt", 0.25, "tsp"),
    ], "Dutch-process cocoa is less acidic than natural, which is what keeps the beans from reading as savoury."),

    ("pr2-lentil-gingerbread", "Lentil Gingerbread", "protein", 1, 4, [
        ("lentils", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("molasses", 1, "tbsp"),
        ("ginger_ground", 0.5, "tsp"),
        ("cinnamon", 0.5, "tsp"),
    ], "Use well-cooked brown or red lentils, chilled — firm lentils stay as grit no matter how long you blend."),

    ("pr2-golden-lentil-warmer", "Golden Lentil Warmer", "protein", 1, 5, [
        ("lentils", 0.5, "cup"),
        ("broth_veg", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("coconut_milk_light", 0.25, "cup"),
        ("turmeric", 0.5, "tsp"),
        ("black_pepper", 0.25, "tsp"),
    ], "A savoury shake needs more salt than a sweet one; taste the broth first, because low-sodium stock will leave this tasting hollow."),

    ("pr2-gochujang-green-heat", "Gochujang Green Heat", "protein", 1, 5, [
        ("edamame", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("silken_tofu", 0.5, "cup"),
        ("gochujang", 0.5, "tbsp"),
        ("scallion", 1, "piece"),
        ("lime_juice", 0.5, "tbsp"),
    ], "Gochujang is sweet as well as hot, so half a tablespoon is plenty — and trim the scallion to the white and pale green only."),

    ("pr2-salmorejo-rebuild", "Salmorejo Rebuild", "protein", 1, 5, [
        ("tomato", 2, "piece"),
        ("white_beans", 0.75, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("olive_oil", 1, "tbsp"),
        ("garlic", 0.25, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "White beans stand in for the bread, so pour the olive oil in last with the blade running and it emulsifies pale pink."),

    ("pr2-sweet-potato-praline", "Sweet Potato Praline", "protein", 1, 5, [
        ("sweet_potato", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("pecans", 1, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("pumpkin_spice", 0.5, "tsp"),
    ], "Roast the sweet potato rather than boiling it and chill it overnight — boiled goes watery and takes the flavour with it."),

    ("pr2-pepita-pumpkin-cup", "Pepita Pumpkin Cup", "protein", 1, 3, [
        ("pumpkin_puree", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("pumpkin_seeds", 2, "tbsp"),
        ("molasses", 1, "tbsp"),
        ("allspice", 0.25, "tsp"),
    ], "Check the tin says pure pumpkin, not pie filling — the filling is mostly sugar and will bury everything else."),

    ("pr2-plantain-cacao-shake", "Plantain Cacao Shake", "protein", 1, 4, [
        ("plantain", 1, "piece"),
        ("soy_milk", 1, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("cinnamon", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "The plantain has to be black-spotted and soft; a yellow one is still starchy and tastes like raw potato."),

    ("pr2-jackfruit-ginger-lift", "Jackfruit Ginger Lift", "protein", 1, 4, [
        ("jackfruit", 0.75, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("ginger", 0.5, "tsp"),
        ("lime_juice", 0.5, "tbsp"),
    ], "Use ripe jackfruit in syrup, drained, not the young green tin sold for pulled-pork — they are completely different foods."),

    ("pr2-quinoa-blueberry-build", "Quinoa Blueberry Build", "protein", 1, 4, [
        ("quinoa", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("lemon_zest", 0.5, "tsp"),
    ], "Cold leftover quinoa is ideal here, and the lemon zest is what stops the blueberry and the powder from tasting muddy together."),

    ("pr2-amaranth-atole", "Amaranth Atole", "protein", 1, 4, [
        ("amaranth", 0.5, "cup"),
        ("soy_milk", 1, "cup"),
        ("plant_protein", 1, "piece"),
        ("coconut_sugar", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
    ], "Cooked amaranth thickens hard in the fridge, so loosen it with a splash of the soy milk before the rest goes in."),

    ("pr2-apricot-lassi-build", "Apricot Lassi Build", "protein", 1, 4, [
        ("almond_yogurt", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("apricot", 3, "piece"),
        ("plant_protein", 1, "piece"),
        ("agave", 1, "tbsp"),
        ("cardamom", 0.25, "tsp"),
    ], "Almond yogurt is thinner than dairy yogurt, so use fresh apricots rather than tinned or the whole thing runs like juice."),

    ("pr2-passion-fruit-set", "Passion Fruit Set", "protein", 1, 3, [
        ("coconut_yogurt", 0.5, "cup"),
        ("passionfruit", 2, "piece"),
        ("soy_milk", 0.5, "cup"),
        ("soy_protein", 1, "piece"),
        ("lime_zest", 0.5, "tsp"),
    ], "Passion fruit seeds blend to black flecks that some people love and some don't — strain the pulp through a fork if you're in the second camp."),

    ("pr2-strawberry-rhubarb-rebuild", "Strawberry Rhubarb Rebuild", "protein", 1, 5, [
        ("rhubarb", 0.5, "cup"),
        ("strawberry_frozen", 0.75, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("oats", 0.25, "cup"),
        ("maple_syrup", 1, "tbsp"),
    ], "Raw rhubarb is punishingly sour and fibrous; stew it with the maple syrup for five minutes and chill it before it goes near the cup."),

    ("pr2-goji-orange-hemp", "Goji Orange Hemp", "protein", 1, 4, [
        ("goji", 0.25, "cup"),
        ("orange", 1, "piece"),
        ("soy_milk", 0.75, "cup"),
        ("hemp_protein", 1, "piece"),
        ("hemp_hearts", 1, "tbsp"),
    ], "Soak the goji berries in the soy milk for ten minutes first — dry ones stay leathery and catch in your teeth."),

    ("pr2-acai-in-a-cup", "Acai in a Cup", "protein", 1, 3, [
        ("acai_puree", 0.5, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("almond_butter", 1, "tbsp"),
        ("banana_frozen", 0.5, "cup"),
    ], "Unsweetened acai packs are bitter and almost savoury on their own, which is exactly why the banana isn't optional."),

    ("pr2-sour-cherry-stone", "Sour Cherry Stone", "protein", 1, 4, [
        ("cherry_sour", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein_choc", 1, "piece"),
        ("cacao_nibs", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Check every cherry for a stone; one missed pit will chip the Blast's blade and there is no repairing it."),

    ("pr2-watermelon-salt-recovery", "Watermelon Salt Crush", "protein", 1, 3, [
        ("watermelon_frozen", 1, "cup"),
        ("pea_milk", 0.5, "cup"),
        ("pea_protein", 1, "piece"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Freeze watermelon in single-layer chunks on a tray, not in a bag — a frozen brick won't come apart in a portable blender."),

    ("pr2-walnut-maple-silk", "Walnut Maple Silk", "protein", 1, 4, [
        ("silken_tofu", 1, "cup"),
        ("oat_milk", 0.5, "cup"),
        ("walnuts", 2, "tbsp"),
        ("hemp_hearts", 2, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
    ], "Walnut skins carry a tannic bitterness; a thirty-second soak in hot water and a rub in a towel takes most of it off."),

    ("pr2-tofu-tiramisu", "Bittersweet Espresso Whip", "protein", 1, 4, [
        ("silken_tofu", 1, "cup"),
        ("espresso", 0.5, "cup"),
        ("soy_milk", 0.25, "cup"),
        ("hemp_hearts", 2, "tbsp"),
        ("date_syrup", 1, "tbsp"),
        ("cacao_powder", 1, "tbsp"),
    ], "No powder and no mascarpone — silken tofu whipped with cold espresso gets you the same texture if you blend it a full minute."),

    ("pr2-banana-cacao-iron", "Banana Cacao Iron", "protein", 1, 4, [
        ("firm_tofu", 0.5, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("cacao_powder", 1.5, "tbsp"),
        ("date_syrup", 1, "tbsp"),
    ], "Press the firm tofu between two plates for ten minutes first; the water you squeeze out is water that would otherwise thin the shake."),

    ("pr2-avocado-lime-rebuild", "Avocado Lime Rebuild", "protein", 1, 4, [
        ("avocado", 0.5, "piece"),
        ("soy_milk", 0.75, "cup"),
        ("soy_protein", 1, "piece"),
        ("spinach", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 1, "tbsp"),
    ], "Fat and acid together are the standard fix for a chalky powder, and half an avocado with a tablespoon of lime is the cleanest version of it."),

    ("pr2-carrot-cardamom-build", "Carrot Cardamom Build", "protein", 1, 3, [
        ("carrot_juice", 0.5, "cup"),
        ("soy_milk", 0.5, "cup"),
        ("plant_protein", 1, "piece"),
        ("cashew_butter", 1, "tbsp"),
        ("ginger", 0.5, "tsp"),
        ("cardamom", 0.25, "tsp"),
    ], "Cashew butter is the mildest of the nut butters, so it thickens this without arguing with the carrot."),

    ("pr2-beetroot-bruiser", "Beetroot Bruiser", "protein", 1, 4, [
        ("beet", 0.5, "cup"),
        ("raspberry_frozen", 0.5, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("pea_protein", 1, "piece"),
        ("lemon_juice", 1, "tbsp"),
    ], "Beet turns dull brown next to chocolate but stays vivid next to raspberry, and the lemon is what holds that colour."),

    ("pr2-blue-spirulina-surf", "Blue Spirulina Surf", "protein", 1, 3, [
        ("pineapple_frozen", 0.75, "cup"),
        ("pea_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("coconut_butter", 1, "tbsp"),
        ("blue_spirulina", 0.5, "tsp"),
    ], "Blue spirulina is far milder than the green kind, but it stains a plastic cup — rinse straight after drinking."),

    ("pr2-sea-moss-mango-build", "Sea Moss Mango Build", "protein", 1, 3, [
        ("mango", 1, "piece"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("sea_moss", 1, "tbsp"),
        ("lime_juice", 0.5, "tbsp"),
    ], "Sea moss gel thickens as it sits, so drink this one straight away or it sets to a spoonable pudding in the fridge."),

    ("pr2-lucuma-maca-malt", "Lucuma Maca Malt", "protein", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("almond_butter", 1, "tbsp"),
        ("lucuma", 1, "tbsp"),
        ("maca", 0.5, "tbsp"),
        ("date", 1, "piece"),
    ], "Lucuma tastes like malt and maple; maca is bitter and needs the date, so don't scale the maca up on its own."),

    ("pr2-baobab-berry-snap", "Baobab Berry Snap", "protein", 1, 3, [
        ("berries_mixed_frozen", 0.75, "cup"),
        ("soy_milk", 0.75, "cup"),
        ("plant_protein", 1, "piece"),
        ("baobab", 1, "tbsp"),
        ("camu_camu", 0.5, "tsp"),
    ], "Baobab and camu camu are both sharply sour powders — between them you need no other acid, and a whole tablespoon of camu would be undrinkable."),
]
