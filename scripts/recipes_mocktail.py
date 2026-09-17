"""Alcohol-free drinks built like cocktails: tea tannin, vinegar shrubs, salt,
chilli and bitter citrus, agua frescas, ginger builds and sparkling slushes."""

RECIPES = [

    # ------------------------------------------------ frozen virgin classics
    ("mk-havana-chill", "Havana Chill", "mocktail", 1, 5, [
        ("mint", 3, "tbsp"),
        ("lime_juice", 3, "tbsp"),
        ("simple_syrup", 1, "tbsp"),
        ("ice", 1.25, "cup"),
        ("sparkling_water", 0.5, "cup"),
    ], "Blend the mint, lime and ice first and pour the sparkling water in at the end — bubbles do not survive the blade."),

    ("mk-nada-rita", "Nada-Rita", "mocktail", 1, 4, [
        ("limeade_frozen", 0.25, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.5, "cup"),
        ("ice", 1, "cup"),
        ("orange_zest", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Rub a cut lime around the rim and roll it in coarse salt before you pour; the rim is most of what makes it read as a margarita."),

    ("mk-isla-nada", "Isla Nada", "mocktail", 2, 5, [
        ("pineapple_frozen", 1, "cup"),
        ("coconut_milk_canned", 0.5, "cup"),
        ("cream_of_coconut", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], "Cream of coconut is sweet and canned coconut milk is not — you need both, one for body and one for the sweetness."),

    ("mk-cuba-nada", "Cuba Nada", "mocktail", 1, 3, [
        ("cola", 0.75, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("date_syrup", 1, "tsp"),
        ("lime_zest", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], "A teaspoon of date syrup gives the molasses note that rum usually brings, so the cola stops tasting like just cola."),

    ("mk-michelada-cero", "Michelada Cero", "mocktail", 1, 4, [
        ("tomato_juice", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("hot_sauce", 1, "tsp"),
        ("worcestershire", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Without the beer you lose the carbonation, so chill the tomato juice hard and keep the ice coarse or it turns to soup."),

    # ---------------------------------------------------- shrubs and switchel
    ("mk-strawberry-balsamic-shrub", "Strawberry Balsamic Shrub", "mocktail", 1, 5, [
        ("strawberry", 6, "piece"),
        ("balsamic", 1.5, "tsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.75, "cup"),
        ("sparkling_water", 0.75, "cup"),
    ], "The vinegar should read as brightness, not as vinegar — start at a teaspoon and add the last half only if the fruit tastes flat."),

    ("mk-haymakers-switchel", "Haymaker's Switchel", "mocktail", 1, 4, [
        ("water", 1, "cup"),
        ("cider_vinegar", 1, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("ginger", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Grate the ginger rather than chunking it; the Blast will not fully break down a knob of fibre and you get strings in the last mouthful."),

    ("mk-blackberry-thyme-shrub", "Blackberry Thyme Shrub", "mocktail", 1, 5, [
        ("blackberry_frozen", 0.75, "cup"),
        ("cider_vinegar", 2, "tsp"),
        ("honey", 1, "tbsp"),
        ("thyme", 1, "tsp"),
        ("sparkling_water", 0.75, "cup"),
    ], "Strip the thyme leaves off the stem — the woody stems never break down and they taste like twigs."),

    ("mk-orchard-shrub", "Orchard Shrub", "mocktail", 1, 4, [
        ("apple_green", 1, "piece"),
        ("cider_vinegar", 2, "tsp"),
        ("maple_syrup", 1, "tbsp"),
        ("ice", 0.5, "cup"),
        ("sparkling_water", 0.75, "cup"),
    ], "Leave the skin on the green apple; that is where the tannin and most of the colour live."),

    ("mk-rhubarb-sour", "Rhubarb Sour", "mocktail", 1, 5, [
        ("rhubarb", 0.75, "cup"),
        ("sugar", 1.5, "tbsp"),
        ("lemon_juice", 1, "tbsp"),
        ("ice", 0.5, "cup"),
        ("sparkling_water", 0.75, "cup"),
    ], "Raw rhubarb is stringy, so slice it thin across the stalk and give it a full extra blend cycle before anything else goes in."),

    # ------------------------------------------------------- hibiscus and tea
    ("mk-jamaica-frost", "Jamaica Frost", "mocktail", 1, 4, [
        ("hibiscus_tea", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("agave", 1, "tbsp"),
        ("ice", 1, "cup"),
        ("salt", 0.25, "tsp"),
    ], "Brew the hibiscus at double strength and chill it — ice dilutes it back down to where you wanted it."),

    ("mk-hibiscus-rosemary", "Hibiscus and Rosemary", "mocktail", 1, 4, [
        ("hibiscus_tea", 1, "cup"),
        ("rosemary", 1, "tsp"),
        ("lemon_juice", 1, "tbsp"),
        ("maple_syrup", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Rosemary goes soapy if you overdo it; one teaspoon of picked needles is the ceiling for a single cup."),

    ("mk-sorrel-party-punch", "Sorrel Party Punch", "mocktail", 2, 6, [
        ("hibiscus_tea", 1.5, "cup"),
        ("ginger", 1, "tbsp"),
        ("clove", 0.25, "tsp"),
        ("lime_juice", 2, "tbsp"),
        ("brown_sugar", 2, "tbsp"),
        ("ice", 0.75, "cup"),
    ], None),

    ("mk-peach-tannin-tea", "Peach Tannin Tea", "mocktail", 1, 4, [
        ("black_tea", 1, "cup"),
        ("peach_frozen", 1, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("honey", 1, "tbsp"),
    ], "Brew the tea strong and chill it first; hot tea melts the fruit and you lose the frozen texture entirely."),

    ("mk-pomegranate-black-tea", "Pomegranate Black Tea", "mocktail", 1, 4, [
        ("black_tea", 1, "cup"),
        ("pomegranate_juice", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("honey", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Let the tea steep a minute past where you normally would — the extra tannin is what stands in for the dry edge of a wine."),

    ("mk-maghrebi-mint-freeze", "Maghrebi Mint Freeze", "mocktail", 1, 4, [
        ("green_tea", 1, "cup"),
        ("mint", 3, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Green tea turns bitter if it was brewed too hot, and freezing it does not hide that — brew it at about 80C."),

    ("mk-mate-limon", "Mate Limon", "mocktail", 1, 4, [
        ("yerba_mate", 1, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("mint", 1, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 1, "cup"),
    ], "Mate is properly bitter and that is the point — sweeten it less than you think, then add the lemon and taste again."),

    ("mk-mate-mule", "Mate Mule", "mocktail", 1, 4, [
        ("yerba_mate", 0.75, "cup"),
        ("ginger_beer", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("ice", 1, "cup"),
    ], None),

    ("mk-rooibos-amber", "Rooibos Amber", "mocktail", 1, 4, [
        ("rooibos_tea", 1, "cup"),
        ("orange", 1, "piece"),
        ("cardamom", 0.25, "tsp"),
        ("honey", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Peel the orange but leave a strip of pith-free zest in the cup — rooibos is soft and needs the oil for lift."),

    ("mk-chamomile-gold", "Chamomile Gold", "mocktail", 1, 4, [
        ("chamomile_tea", 1, "cup"),
        ("lemon_juice", 1.5, "tbsp"),
        ("honey", 1, "tbsp"),
        ("orange_blossom", 0.5, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Orange blossom water is a perfume, not a flavour — half a teaspoon perfumes the whole cup and a full one ruins it."),

    ("mk-peppermint-frost", "Peppermint Frost", "mocktail", 1, 3, [
        ("peppermint_tea", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("honey", 2, "tsp"),
        ("ice", 1, "cup"),
        ("salt", 0.25, "tsp"),
    ], "Brewed peppermint tea beats peppermint extract here; the extract tastes like toothpaste once the drink is cold."),

    # ------------------------------------------------------- ginger and fizz
    ("mk-stormy-ginger-lime", "Stormy Ginger Lime", "mocktail", 1, 3, [
        ("ginger_beer", 1, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("molasses", 1, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "A teaspoon of molasses is the whole trick — it is the dark, burnt-sugar note the drink is missing."),

    ("mk-ginger-kombucha-highball", "Ginger Kombucha Highball", "mocktail", 1, 3, [
        ("kombucha", 1, "cup"),
        ("ginger", 1, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Pulse rather than run it; kombucha foams hard and a long blend pushes it up past the lid."),

    ("mk-golden-ginger-spritz", "Golden Ginger Spritz", "mocktail", 1, 5, [
        ("ginger", 1, "tbsp"),
        ("turmeric_fresh", 1, "tsp"),
        ("lemon_juice", 2, "tbsp"),
        ("black_pepper", 0.25, "tsp"),
        ("ginger_ale", 0.75, "cup"),
    ], "Fresh turmeric stains everything it touches, including the gasket — rinse the cup straight away rather than after."),

    ("mk-tepache-chill", "Tepache Chill", "mocktail", 1, 5, [
        ("pineapple", 1, "cup"),
        ("kombucha", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
        ("coconut_sugar", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Use the core of the pineapple as well as the flesh — it is where the funk that makes this taste fermented comes from."),

    ("mk-birch-and-lime", "Birch and Lime", "mocktail", 1, 3, [
        ("root_beer", 1, "cup"),
        ("lime_juice", 1.5, "tbsp"),
        ("vanilla_extract", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("mk-spiced-cherry-cola", "Spiced Cherry Cola", "mocktail", 1, 4, [
        ("cola", 1, "cup"),
        ("cherry_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("allspice", 0.25, "tsp"),
    ], "Let the cola go flat on purpose before blending, then top the glass with a splash of fresh cola for the bubbles."),

    # ------------------------------------------ bitter and aperitivo builds
    ("mk-bitter-sunset", "Bitter Sunset", "mocktail", 1, 4, [
        ("grapefruit", 1, "piece"),
        ("tonic_water", 0.75, "cup"),
        ("orange_zest", 0.5, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Leave a little of the white pith on the grapefruit segments — that bitterness is the whole reason this works before dinner."),

    ("mk-no-groni-freeze", "No-Groni Freeze", "mocktail", 1, 5, [
        ("grapefruit", 0.5, "piece"),
        ("cranberry_juice", 0.25, "cup"),
        ("tonic_water", 0.5, "cup"),
        ("orange_zest", 0.5, "tsp"),
        ("ice", 1, "cup"),
    ], None),

    ("mk-sour-cranberry-aperitivo", "Sour Cranberry Aperitivo", "mocktail", 1, 4, [
        ("cranberry_frozen", 0.75, "cup"),
        ("tonic_water", 0.75, "cup"),
        ("agave", 1, "tbsp"),
        ("orange_zest", 0.5, "tsp"),
        ("ice", 0.5, "cup"),
    ], None),

    ("mk-blood-orange-aperitivo", "Blood Orange Aperitivo", "mocktail", 1, 4, [
        ("blood_orange", 1, "piece"),
        ("cranberry_juice", 0.25, "cup"),
        ("tonic_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], None),

    ("mk-sevilla-spritz", "Sevilla Spritz", "mocktail", 1, 4, [
        ("marmalade", 2, "tbsp"),
        ("lemon_juice", 1.5, "tbsp"),
        ("sparkling_water", 1, "cup"),
        ("ice", 0.75, "cup"),
    ], "Marmalade rather than orange juice: the shredded peel carries the bitterness that juice alone cannot."),

    ("mk-fennel-and-grapefruit", "Fennel and Grapefruit", "mocktail", 1, 5, [
        ("fennel", 0.5, "cup"),
        ("grapefruit", 1, "piece"),
        ("sparkling_water", 0.5, "cup"),
        ("agave", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Use the white bulb, not the fronds — fronds taste like dill and take the drink somewhere else entirely."),

    ("mk-basil-bitter-smash", "Basil Bitter Smash", "mocktail", 1, 5, [
        ("basil", 3, "tbsp"),
        ("grapefruit", 1, "piece"),
        ("simple_syrup", 1, "tbsp"),
        ("sparkling_water", 0.5, "cup"),
        ("salt", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "Slap the basil between your palms before it goes in; torn basil in a blender bruises black, slapped basil gives up its oil first."),

    ("mk-concord-and-pepper", "Concord and Pepper", "mocktail", 1, 3, [
        ("grape_juice", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("black_pepper", 0.25, "tsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 1, "cup"),
    ], "Black pepper and grape is how you get a red-wine shape out of juice; grind it coarse so you taste it in flashes."),

    ("mk-beet-and-pepper-sour", "Beet and Pepper Sour", "mocktail", 1, 5, [
        ("beet", 0.5, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("black_pepper", 0.25, "tsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.5, "cup"),
    ], "Cooked beet, not raw — raw beet blends to grit and tastes like soil rather than earth."),

    # ---------------------------------------------- chilli, salt and tamarind
    ("mk-tamarindo-heat", "Tamarindo Heat", "mocktail", 1, 5, [
        ("date_paste", 2, "tbsp"),
        ("lime_juice", 3, "tbsp"),
        ("water", 1, "cup"),
        ("tajin", 1, "tsp"),
        ("ice", 0.75, "cup"),
    ], "Date paste with that much lime lands close to tamarind — sticky, sour and dark — so do not cut the lime back."),

    ("mk-jicama-chili-slush", "Jicama Chili Slush", "mocktail", 1, 6, [
        ("jicama", 1, "cup"),
        ("lime_juice", 3, "tbsp"),
        ("water", 0.75, "cup"),
        ("tajin", 1, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Peel jicama with a knife rather than a peeler; the skin is thicker than it looks and the fibrous layer under it is what makes drinks woolly."),

    ("mk-sandia-con-tajin", "Sandia con Tajin", "mocktail", 2, 4, [
        ("watermelon_frozen", 1.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("tajin", 1, "tsp"),
        ("water", 0.5, "cup"),
    ], None),

    ("mk-fire-and-cherry", "Fire and Cherry", "mocktail", 1, 4, [
        ("cherry_juice", 0.75, "cup"),
        ("cherry_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("cayenne", 0.25, "tsp"),
        ("salt", 0.25, "tsp"),
    ], "Add the cayenne in two goes and taste between them; heat in a cold drink creeps up about thirty seconds after the sip."),

    ("mk-verde-sour", "Verde Sour", "mocktail", 1, 5, [
        ("cucumber", 0.5, "piece"),
        ("cilantro", 2, "tbsp"),
        ("jalapeno", 0.5, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.75, "cup"),
        ("salt", 0.25, "tsp"),
    ], "Scrape the seeds and white ribs out of the jalapeno — you want the green pepper flavour, not just the burn."),

    # ------------------------------------------------------------ aguas frescas
    ("mk-melon-y-pepino", "Melon y Pepino", "mocktail", 2, 6, [
        ("honeydew", 1.5, "cup"),
        ("cucumber", 0.5, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.5, "cup"),
        ("salt", 0.25, "tsp"),
    ], "A pinch of salt is what turns melon water into a drink you would be handed at a bar rather than a glass of melon."),

    ("mk-guanabana-fresca", "Guanabana Fresca", "mocktail", 1, 5, [
        ("soursop", 1, "cup"),
        ("coconut_milk_bev", 0.5, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("ice", 0.5, "cup"),
    ], "Pick out the black seeds before blending — they are bitter and they are hard enough to mark the blade."),

    ("mk-prickly-pear-sunset", "Prickly Pear Sunset", "mocktail", 1, 5, [
        ("prickly_pear", 2, "piece"),
        ("lime_juice", 2, "tbsp"),
        ("water", 0.75, "cup"),
        ("agave", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("ice", 0.5, "cup"),
    ], "Handle prickly pears with a fork and a knife, never bare hands, and halve them to scoop the flesh out of the skin."),

    ("mk-lemongrass-slush", "Lemongrass Slush", "mocktail", 1, 6, [
        ("lemongrass", 1, "tbsp"),
        ("lime_juice", 2, "tbsp"),
        ("honey", 1, "tbsp"),
        ("water", 1, "cup"),
        ("ice", 1, "cup"),
    ], "Only the pale bottom third of the stalk is tender enough to blend; slice it into coins and keep the green top for another day."),

    ("mk-sour-cherry-and-rosemary", "Sour Cherry and Rosemary", "mocktail", 1, 5, [
        ("cherry_sour", 0.75, "cup"),
        ("rosemary", 1, "tsp"),
        ("sugar", 1, "tbsp"),
        ("water", 0.75, "cup"),
        ("ice", 0.5, "cup"),
    ], None),

    # ---------------------------------------------- floral and aromatic builds
    ("mk-rose-and-lychee", "Rose and Lychee", "mocktail", 1, 5, [
        ("lychee", 8, "piece"),
        ("rose_water", 0.5, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], "Rose water without acid tastes like soap; the tablespoon of lime is doing structural work, not seasoning."),

    ("mk-orange-blossom-fizz", "Orange Blossom Fizz", "mocktail", 1, 4, [
        ("orange_juice", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("orange_blossom", 0.5, "tsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], None),

    ("mk-cardamom-pomegranate", "Cardamom Pomegranate", "mocktail", 1, 4, [
        ("pomegranate_juice", 0.75, "cup"),
        ("cardamom", 0.25, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("honey", 1, "tsp"),
        ("ice", 1, "cup"),
    ], "Ground cardamom fades fast in the jar — if yours smells of nothing when you open it, use more or it will not register at all."),

    ("mk-winter-garden-punch", "Winter Garden Punch", "mocktail", 2, 5, [
        ("pomegranate_juice", 1, "cup"),
        ("rosemary", 1, "tsp"),
        ("lemon_juice", 2, "tbsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], None),

    ("mk-passionfruit-sour", "Passionfruit Sour", "mocktail", 1, 4, [
        ("passionfruit_juice", 0.75, "cup"),
        ("egg_white", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("simple_syrup", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Pasteurised egg white gives you the foam cap a proper sour needs; blend it thirty seconds longer than feels necessary."),

    # -------------------------------------------- sparkling slushes and garden
    ("mk-raspberry-snow", "Raspberry Snow", "mocktail", 1, 4, [
        ("raspberry_frozen", 1, "cup"),
        ("water", 0.5, "cup"),
        ("lemon_juice", 1.5, "tbsp"),
        ("sugar", 1, "tbsp"),
        ("sparkling_water", 0.5, "cup"),
    ], "Blend the slush with plain water, then stir the sparkling water in by hand at the glass so it stays a fizzy slush and not a foam."),

    ("mk-kiwi-basil-fizz", "Kiwi Basil Fizz", "mocktail", 1, 4, [
        ("kiwi", 2, "piece"),
        ("basil", 2, "tbsp"),
        ("lime_juice", 1, "tbsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.5, "cup"),
    ], None),

    ("mk-starfruit-spritz", "Starfruit Spritz", "mocktail", 1, 4, [
        ("starfruit", 2, "piece"),
        ("white_grape_juice", 0.5, "cup"),
        ("lemon_zest", 0.5, "tsp"),
        ("sparkling_water", 0.5, "cup"),
        ("ice", 0.75, "cup"),
    ], "Trim the brown edges off the five ridges first; they are tough and they are the bitter part."),

    ("mk-garden-tonic", "Garden Tonic", "mocktail", 1, 5, [
        ("cucumber", 0.5, "piece"),
        ("rosemary", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
        ("tonic_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], "Cucumber and tonic is the gin shape without the gin — keep the peel on for the grassy note the botanicals usually supply."),

    ("mk-celery-salt-fizz", "Celery Salt Fizz", "mocktail", 1, 4, [
        ("celery", 2, "piece"),
        ("lime_juice", 1.5, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("sparkling_water", 0.75, "cup"),
        ("ice", 0.75, "cup"),
    ], "String the celery with a peeler before it goes in, or the fibres wrap the blade and the drink never gets smooth."),

    ("mk-pina-con-hinojo", "Pina con Hinojo", "mocktail", 1, 5, [
        ("pineapple_frozen", 1, "cup"),
        ("fennel", 0.5, "cup"),
        ("lime_juice", 2, "tbsp"),
        ("coconut_water", 0.75, "cup"),
    ], None),

    # ------------------------------------------------- after a workout
    ("mk-second-wind", "Second Wind", "mocktail", 1, 3, [
        ("coconut_water", 1, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
    ], None),

    ("mk-cactus-cooler", "Cactus Cooler", "mocktail", 1, 4, [
        ("cactus_water", 1, "cup"),
        ("watermelon_frozen", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.25, "tsp"),
        ("mint", 1, "tbsp"),
    ], "Cactus water is much milder than coconut water, so this one needs the watermelon frozen solid or it tastes like it has been watered down."),

    ("mk-grapefruit-salt-soda", "Grapefruit Salt Soda", "mocktail", 1, 4, [
        ("grapefruit", 1, "piece"),
        ("sparkling_water", 0.75, "cup"),
        ("salt", 0.25, "tsp"),
        ("simple_syrup", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], None),
]
