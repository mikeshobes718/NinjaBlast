"""Core smoothie canon: berries, tropical, stone fruit, melon, citrus, nut-butter
creams, yogurt and kefir blends, chocolate-fruit pairings, orchard fruit and
freezer medleys."""

RECIPES = [

    # ---------------------------------------------------------------- berries
    ("sm1-midnight-bramble", "Midnight Bramble", "smoothie", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("blackberry_frozen", 1, "cup"),
        ("date", 1, "piece"),
        ("vanilla_bean", 0.5, "tsp"),
    ], None),

    ("sm1-cassis-chill", "Cassis Chill", "smoothie", 1, 3, [
        ("cashew_milk", 0.75, "cup"),
        ("blackcurrant", 0.75, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("honey", 2, "tsp"),
    ], None),

    ("sm1-gooseberry-frost", "Gooseberry Frost", "smoothie", 1, 4, [
        ("white_grape_juice", 0.75, "cup"),
        ("gooseberry", 0.75, "cup"),
        ("ice", 0.75, "cup"),
        ("mint", 1, "tbsp"),
    ], "Top and tail the gooseberries with your thumbnail first; the little stem ends are woody and they float."),

    ("sm1-raspberry-rose-cloud", "Raspberry Rose Cloud", "smoothie", 1, 3, [
        ("pistachio_milk", 1, "cup"),
        ("raspberry_frozen", 1, "cup"),
        ("rose_water", 0.5, "tsp"),
        ("honey", 1, "tsp"),
    ], "Rose water goes from lovely to soapy fast; half a teaspoon is the whole point and a full one is a mistake."),

    ("sm1-blueberry-thyme-field", "Blueberry Thyme Field", "smoothie", 1, 4, [
        ("kombucha", 0.75, "cup"),
        ("blueberry_frozen", 1, "cup"),
        ("thyme", 1, "tsp"),
        ("lemon_juice", 1, "tbsp"),
        ("agave", 2, "tsp"),
    ], "Strip the thyme leaves off the stem — the stems shred but never soften."),

    ("sm1-acai-toasted-coconut", "Acai and Toasted Coconut", "smoothie", 1, 4, [
        ("coconut_milk_bev", 0.75, "cup"),
        ("acai_puree", 0.5, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("coconut_shredded", 1, "tbsp"),
    ], "Toast the shredded coconut in a dry pan for a minute first — untoasted it just adds texture, toasted it adds flavour."),

    ("sm1-bog-and-orchard", "Bog and Orchard", "smoothie", 1, 3, [
        ("apple_juice", 0.75, "cup"),
        ("cranberry_frozen", 0.5, "cup"),
        ("apple_green", 0.5, "piece"),
        ("maple_syrup", 2, "tsp"),
        ("cinnamon", 0.25, "tsp"),
    ], None),

    ("sm1-rhubarb-fool", "Rhubarb Fool", "smoothie", 1, 5, [
        ("milk_whole", 0.5, "cup"),
        ("greek_yogurt_whole", 0.5, "cup"),
        ("rhubarb", 0.75, "cup"),
        ("strawberry_frozen", 0.5, "cup"),
        ("brown_sugar", 2, "tsp"),
    ], "Use raw rhubarb only if it is young and pink — older stalks need stewing and cooling first or the drink turns stringy."),

    ("sm1-bramble-kefir", "Bramble Kefir", "smoothie", 1, 2, [
        ("kefir", 0.75, "cup"),
        ("berries_mixed_frozen", 1, "cup"),
        ("honey", 2, "tsp"),
    ], "Kefir thins out the longer it runs, so pulse it in short bursts rather than holding the button down."),

    ("sm1-barely-sweet-berry", "Barely Sweet Berry", "smoothie", 1, 2, [
        ("water", 0.75, "cup"),
        ("raspberry_frozen", 0.75, "cup"),
        ("strawberry_frozen", 0.5, "cup"),
        ("lemon_juice", 1, "tbsp"),
    ], None),

    # ---------------------------------------------------------------- tropical
    ("sm1-guanabana-cream", "Guanábana Cream", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("soursop", 0.75, "cup"),
        ("ice", 0.5, "cup"),
        ("condensed_milk", 1, "tbsp"),
    ], "Pick every black seed out of the soursop pulp before it goes near the blade — they are hard and bitter."),

    ("sm1-lychee-snow", "Lychee Drift", "smoothie", 1, 5, [
        ("coconut_water", 0.75, "cup"),
        ("lychee", 8, "piece"),
        ("ice", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
    ], "Canned lychees work, but drain them and cut the syrup with extra lime or this gets cloying."),

    ("sm1-jackfruit-sunbeam", "Jackfruit Sunbeam", "smoothie", 1, 4, [
        ("mango_nectar", 0.5, "cup"),
        ("jackfruit", 0.75, "cup"),
        ("ice", 0.75, "cup"),
        ("lime_zest", 0.5, "tsp"),
    ], None),

    ("sm1-passionfruit-kefir-cooler", "Passion Fruit Kefir Cooler", "smoothie", 1, 4, [
        ("kefir", 0.75, "cup"),
        ("passionfruit", 3, "piece"),
        ("pineapple_frozen", 0.5, "cup"),
        ("honey", 2, "tsp"),
    ], None),

    ("sm1-papaya-and-ginger", "Papaya and Ginger", "smoothie", 1, 4, [
        ("coconut_water", 0.5, "cup"),
        ("papaya", 1, "cup"),
        ("ice", 0.5, "cup"),
        ("ginger", 1, "tsp"),
        ("lime_juice", 1, "tbsp"),
    ], None),

    ("sm1-pina-con-tajin", "Piña con Tajín", "smoothie", 1, 3, [
        ("water", 0.5, "cup"),
        ("pineapple_frozen", 1.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("tajin", 0.5, "tsp"),
    ], "Rim the cup with a little extra chili-lime seasoning rather than adding more inside, or the whole drink turns salty."),

    ("sm1-guava-con-queso", "Guava con Queso", "smoothie", 1, 4, [
        ("guava_nectar", 0.75, "cup"),
        ("guava", 1, "piece"),
        ("cream_cheese", 0.25, "cup"),
        ("ice", 0.75, "cup"),
    ], "Let the cream cheese sit out ten minutes — straight from the fridge it leaves white specks that never blend."),

    ("sm1-pink-pitaya-cloud", "Pink Pitaya Cloud", "smoothie", 1, 3, [
        ("coconut_milk_light", 0.75, "cup"),
        ("dragonfruit_frozen", 1, "cup"),
        ("banana_frozen", 0.25, "cup"),
        ("lime_juice", 2, "tsp"),
    ], "Pitaya is all colour and very little flavour, so the banana is doing real work here — do not leave it out."),

    ("sm1-coconut-lime-snow", "Coconut Lime Snow", "smoothie", 1, 3, [
        ("coconut_milk_bev", 0.75, "cup"),
        ("coconut_frozen", 0.5, "cup"),
        ("ice", 1, "cup"),
        ("lime_zest", 1, "tsp"),
        ("maple_syrup", 2, "tsp"),
    ], "Zest the lime before you juice anything else that day — zest off a cut lime is a losing battle."),

    ("sm1-mango-chamomile-cooler", "Mango Chamomile Cooler", "smoothie", 1, 3, [
        ("chamomile_tea", 0.75, "cup"),
        ("mango_frozen", 1, "cup"),
        ("honey", 2, "tsp"),
    ], "Brew the chamomile double strength and chill it — hot tea will melt the mango into slush before it blends."),

    # ------------------------------------------------------------- stone fruit
    ("sm1-apricot-cardamom-cream", "Apricot Cardamom Cream", "smoothie", 1, 5, [
        ("milk_2", 0.5, "cup"),
        ("greek_yogurt_whole", 0.5, "cup"),
        ("apricot", 4, "piece"),
        ("ice", 0.5, "cup"),
        ("cardamom", 0.25, "tsp"),
    ], "A quarter teaspoon of cardamom is plenty — it is a spice that takes over a whole cup if you let it."),

    ("sm1-nectarine-honeycomb", "Nectarine Honeycomb", "smoothie", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("nectarine", 1, "piece"),
        ("ice", 0.5, "cup"),
        ("honey", 2, "tsp"),
        ("bee_pollen", 1, "tsp"),
    ], "Leave the nectarine skins on — they are thin and they give the drink a pink blush the flesh alone won't."),

    ("sm1-plum-dusk", "Plum Dusk", "smoothie", 1, 4, [
        ("rooibos_tea", 0.75, "cup"),
        ("plum", 3, "piece"),
        ("ice", 0.75, "cup"),
        ("ginger_ground", 0.25, "tsp"),
        ("coconut_sugar", 2, "tsp"),
    ], None),

    ("sm1-sour-cherry-marzipan", "Sour Cherry Marzipan", "smoothie", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("cherry_sour", 0.75, "cup"),
        ("ice", 0.5, "cup"),
        ("almond_extract", 0.25, "tsp"),
        ("honey", 2, "tsp"),
    ], "Almond extract is measured in drops for a reason — a quarter teaspoon reads as marzipan, a full one reads as soap."),

    ("sm1-peach-sweet-tea", "Peach Sweet Tea", "smoothie", 1, 3, [
        ("black_tea", 0.75, "cup"),
        ("peach_frozen", 1, "cup"),
        ("lemon_juice", 1, "tbsp"),
        ("brown_sugar", 2, "tsp"),
    ], None),

    ("sm1-peach-buttermilk-frost", "Peach Buttermilk Frost", "smoothie", 1, 3, [
        ("buttermilk", 0.75, "cup"),
        ("peach_frozen", 1, "cup"),
        ("maple_syrup", 2, "tsp"),
        ("nutmeg", 0.25, "tsp"),
    ], None),

    ("sm1-apricot-halva", "Apricot Halva", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("apricot_dried", 5, "piece"),
        ("tahini", 1, "tbsp"),
        ("ice", 0.75, "cup"),
        ("honey", 1, "tsp"),
    ], "Soak the dried apricots in hot water for ten minutes and drain — dry ones just bounce around the blade."),

    ("sm1-cherry-cacao-nib", "Cherry Cacao Nib", "smoothie", 1, 3, [
        ("macadamia_milk", 1, "cup"),
        ("cherry_frozen", 1, "cup"),
        ("cacao_nibs", 1, "tbsp"),
        ("salt", 0.125, "tsp"),
    ], "Add the nibs at the very end and pulse twice so they stay crunchy instead of turning to grit."),

    # ------------------------------------------------------------------ melon
    ("sm1-watermelon-salt-and-lime", "Watermelon Salt and Lime", "smoothie", 1, 3, [
        ("watermelon_juice", 0.75, "cup"),
        ("watermelon_frozen", 1.25, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("salt", 0.125, "tsp"),
    ], "The pinch of salt is not optional — it is what makes watermelon taste like more of itself."),

    ("sm1-melon-agua-fresca", "Melon Agua Fresca", "smoothie", 2, 4, [
        ("water", 0.75, "cup"),
        ("cantaloupe", 1.25, "cup"),
        ("ice", 0.75, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("sugar", 2, "tsp"),
    ], "A cantaloupe that smells like nothing at the stem end will taste like nothing blended — check before you cut."),

    ("sm1-honeydew-lime-frost", "Honeydew Lime Frost", "smoothie", 1, 3, [
        ("cactus_water", 0.5, "cup"),
        ("honeydew", 1.25, "cup"),
        ("ice", 0.75, "cup"),
        ("lime_zest", 0.5, "tsp"),
    ], "Freeze the honeydew cubes overnight and you can skip half the ice, which keeps the flavour from washing out."),

    ("sm1-watermelon-hibiscus", "Watermelon Hibiscus", "smoothie", 1, 3, [
        ("hibiscus_tea", 0.75, "cup"),
        ("watermelon_frozen", 1.5, "cup"),
        ("lime_juice", 2, "tsp"),
        ("agave", 1, "tsp"),
    ], None),

    ("sm1-melon-and-labneh", "Melon and Labneh", "smoothie", 1, 4, [
        ("water", 0.25, "cup"),
        ("labneh", 0.5, "cup"),
        ("cantaloupe", 0.75, "cup"),
        ("ice", 0.5, "cup"),
        ("mint", 1, "tbsp"),
        ("honey", 2, "tsp"),
    ], "Labneh is thicker than yogurt, so start the blend with the water on top of it to get things moving."),

    ("sm1-melon-con-horchata", "Melón con Horchata", "smoothie", 1, 4, [
        ("rice_milk", 0.75, "cup"),
        ("cantaloupe", 1, "cup"),
        ("ice", 0.5, "cup"),
        ("cinnamon", 0.5, "tsp"),
        ("condensed_milk", 1, "tbsp"),
    ], None),

    # ----------------------------------------------------------------- citrus
    ("sm1-blood-orange-frost", "Blood Orange Frost", "smoothie", 1, 5, [
        ("sparkling_water", 0.5, "cup"),
        ("blood_orange", 2, "piece"),
        ("ice", 1, "cup"),
        ("honey", 2, "tsp"),
    ], "Segment the blood oranges rather than juicing them — the membranes are what make the colour muddy."),

    ("sm1-tangerine-cream-cloud", "Tangerine Cream Cloud", "smoothie", 1, 4, [
        ("soy_milk_vanilla", 0.75, "cup"),
        ("tangerine", 3, "piece"),
        ("ice", 0.75, "cup"),
        ("vanilla_bean", 0.5, "tsp"),
    ], "Peel the white pith off each segment; it is the difference between creamy and bitter."),

    ("sm1-grapefruit-rosemary-chill", "Grapefruit Rosemary Chill", "smoothie", 1, 4, [
        ("green_tea", 0.5, "cup"),
        ("grapefruit", 1, "piece"),
        ("ice", 1, "cup"),
        ("rosemary", 1, "tsp"),
        ("agave", 2, "tsp"),
    ], "Use only the soft top leaves of the rosemary sprig — woody stem never breaks down and you will find it later."),

    ("sm1-clementine-and-date", "Clementine and Date", "smoothie", 1, 4, [
        ("flax_milk", 0.75, "cup"),
        ("clementine", 3, "piece"),
        ("date", 2, "piece"),
        ("ice", 0.5, "cup"),
    ], "Tear the dates open and check for pits even on bags marked pitted — one pit ends a blade assembly."),

    ("sm1-lemon-poppy-seed", "Lemon Poppy Seed", "smoothie", 1, 3, [
        ("greek_yogurt_nonfat", 0.5, "cup"),
        ("milk_skim", 0.5, "cup"),
        ("lemon_curd", 1.5, "tbsp"),
        ("lemon_zest", 1, "tsp"),
        ("poppy_seeds", 1, "tbsp"),
        ("ice", 0.75, "cup"),
    ], "Lemon curd does the work of juice and sugar together; add the zest last so it stays in flecks rather than dissolving."),

    ("sm1-marmalade-on-toast", "Marmalade on Toast", "smoothie", 1, 4, [
        ("oat_milk", 1, "cup"),
        ("oats", 0.25, "cup"),
        ("marmalade", 1.5, "tbsp"),
        ("ice", 0.75, "cup"),
        ("orange_zest", 0.5, "tsp"),
    ], "Let the oats sit in the oat milk for five minutes before blending — they thicken far better hydrated."),

    # ---------------------------------------------------- banana + nut butters
    ("sm1-elvis-in-a-cup", "Elvis in a Cup", "smoothie", 1, 3, [
        ("milk_2", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("peanut_butter", 2, "tbsp"),
        ("cacao_powder", 1, "tsp"),
        ("salt", 0.125, "tsp"),
    ], "Warm the peanut butter for ten seconds so it ribbons off the spoon instead of sitting in a lump on the blade."),

    ("sm1-fig-and-almond-butter", "Fig and Almond Butter", "smoothie", 1, 4, [
        ("almond_milk", 0.75, "cup"),
        ("fig", 3, "piece"),
        ("almond_butter", 1.5, "tbsp"),
        ("ice", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Fresh figs blend to a beautiful jammy purple; dried ones need a soak first and taste far sweeter, so cut back on nothing else."),

    ("sm1-banana-kulfi", "Banana Kulfi", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("cashew_butter", 1.5, "tbsp"),
        ("cardamom", 0.25, "tsp"),
        ("pistachios", 1, "tbsp"),
    ], "Blend the pistachios with the milk first so they break down, then add everything else — they are too hard to catch late."),

    ("sm1-sunflower-banana-cream", "Sunflower Banana Cream", "smoothie", 1, 3, [
        ("hemp_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("sunflower_butter", 2, "tbsp"),
        ("maple_syrup", 2, "tsp"),
    ], None),

    ("sm1-sesame-date-cream", "Sesame Date Cream", "smoothie", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("date", 3, "piece"),
        ("tahini", 1.5, "tbsp"),
        ("ice", 0.75, "cup"),
        ("salt", 0.125, "tsp"),
    ], "Use tahini from a fresh jar and stir it well — the separated oil at the top on its own makes the drink greasy."),

    ("sm1-pistachio-orange-blossom", "Pistachio Orange Blossom", "smoothie", 1, 4, [
        ("pistachio_milk", 0.75, "cup"),
        ("banana_frozen", 0.75, "cup"),
        ("pistachio_butter", 1.5, "tbsp"),
        ("orange_blossom", 0.5, "tsp"),
        ("honey", 2, "tsp"),
    ], "Orange blossom water and rose water are not interchangeable here — blossom is the one that suits pistachio."),

    ("sm1-hazelnut-banana-praline", "Hazelnut Banana Praline", "smoothie", 1, 3, [
        ("milk_lactose_free", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("hazelnut_butter", 1.5, "tbsp"),
        ("coconut_sugar", 2, "tsp"),
        ("salt", 0.125, "tsp"),
    ], None),

    ("sm1-coconut-butter-mango", "Coconut Butter Mango", "smoothie", 1, 3, [
        ("coconut_water", 0.75, "cup"),
        ("mango_frozen", 1, "cup"),
        ("coconut_butter", 1.5, "tbsp"),
        ("lime_juice", 2, "tsp"),
    ], "Coconut butter sets hard in the jar; stand it in warm water for a minute or it will never emulsify."),

    # ------------------------------------------------------------ yogurt/kefir
    ("sm1-minted-cucumber-kefir", "Minted Cucumber Kefir", "smoothie", 1, 4, [
        ("kefir", 0.75, "cup"),
        ("cucumber", 0.5, "piece"),
        ("mint", 2, "tbsp"),
        ("ice", 0.5, "cup"),
        ("salt", 0.125, "tsp"),
    ], "Scoop the watery seed core out of the cucumber; it dilutes the kefir and adds nothing."),

    ("sm1-quark-berry-whip", "Quark Berry Whip", "smoothie", 1, 3, [
        ("milk_2", 0.5, "cup"),
        ("quark", 0.5, "cup"),
        ("berries_mixed_frozen", 0.75, "cup"),
        ("vanilla_extract", 0.5, "tsp"),
        ("honey", 2, "tsp"),
    ], "Quark curdles if you hit it with acid before fat, so let the milk and quark blend smooth before the berries go in."),

    ("sm1-pineapple-cottage-whip", "Pineapple Cottage Whip", "smoothie", 1, 3, [
        ("pineapple_juice", 0.5, "cup"),
        ("cottage_cheese", 0.5, "cup"),
        ("pineapple_frozen", 0.75, "cup"),
        ("lime_zest", 0.5, "tsp"),
    ], "Run the cottage cheese with the juice alone for fifteen seconds first or the curds survive the whole blend."),

    ("sm1-ruby-kefir", "Ruby Kefir", "smoothie", 1, 4, [
        ("kefir", 0.75, "cup"),
        ("beet", 0.25, "cup"),
        ("raspberry_frozen", 0.75, "cup"),
        ("date", 1, "piece"),
    ], "Cooked beet, never raw — raw beet stays gritty and tastes like soil in a cold drink."),

    ("sm1-greek-honey-walnut", "Greek Honey Walnut", "smoothie", 1, 3, [
        ("milk_whole", 0.5, "cup"),
        ("greek_yogurt_whole", 0.5, "cup"),
        ("walnuts", 2, "tbsp"),
        ("ice", 0.75, "cup"),
        ("honey", 1, "tbsp"),
    ], "Walnut skins turn bitter when over-blended, so stop as soon as the drink looks smooth."),

    ("sm1-alphonso-coconut-cream", "Alphonso Coconut Cream", "smoothie", 1, 3, [
        ("coconut_milk_bev", 0.5, "cup"),
        ("coconut_yogurt", 0.5, "cup"),
        ("mango_frozen", 1, "cup"),
        ("cardamom", 0.25, "tsp"),
    ], None),

    ("sm1-strawberry-kefir-swirl", "Strawberry Kefir Swirl", "smoothie", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("strawberry_frozen", 1, "cup"),
        ("strawberry_jam", 1, "tbsp"),
        ("lemon_zest", 0.5, "tsp"),
    ], "Stir the jam in by hand after blending if you want an actual swirl rather than a uniform pink."),

    ("sm1-blueberry-skyr-spoon", "Blueberry Skyr Spoon", "smoothie", 1, 3, [
        ("oat_milk", 0.5, "cup"),
        ("skyr", 0.5, "cup"),
        ("blueberry_frozen", 0.75, "cup"),
        ("lemon_juice", 2, "tsp"),
        ("maple_syrup", 2, "tsp"),
    ], None),

    # --------------------------------------------------------- chocolate fruit
    ("sm1-chocolate-orange-freeze", "Chocolate Orange Freeze", "smoothie", 1, 4, [
        ("oat_milk_barista", 0.75, "cup"),
        ("orange", 1, "piece"),
        ("cacao_powder", 1, "tbsp"),
        ("ice", 0.75, "cup"),
        ("maple_syrup", 2, "tsp"),
    ], "Sift the cacao or shake it with the milk in a jar first — dry cocoa dumped on top clumps and floats."),

    ("sm1-raspberry-truffle-blend", "Raspberry Truffle Blend", "smoothie", 1, 3, [
        ("milk_whole", 0.75, "cup"),
        ("raspberry_frozen", 1, "cup"),
        ("dark_chocolate", 1.5, "tbsp"),
        ("ice", 0.5, "cup"),
        ("salt", 0.125, "tsp"),
    ], "Chop the chocolate fine before it goes in; a whole square just rattles and chips the ice instead."),

    ("sm1-pear-and-dark-chocolate", "Pear and Dark Chocolate", "smoothie", 1, 4, [
        ("soy_milk", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("cacao_powder", 1, "tbsp"),
        ("ice", 0.75, "cup"),
        ("date", 1, "piece"),
    ], None),

    ("sm1-mexican-chocolate-banana", "Mexican Chocolate Banana", "smoothie", 1, 3, [
        ("almond_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("cinnamon", 0.5, "tsp"),
        ("cayenne", 0.0625, "tsp"),
    ], "The cayenne should be a warmth you notice on the third sip, not the first — start with less than you think."),

    ("sm1-cacao-prune-velvet", "Cacao Prune Velvet", "smoothie", 1, 4, [
        ("cashew_milk", 0.75, "cup"),
        ("prune", 4, "piece"),
        ("dutch_cocoa", 1, "tbsp"),
        ("ice", 1, "cup"),
        ("salt", 0.125, "tsp"),
    ], None),

    ("sm1-cherry-chocolate-kefir", "Cherry Chocolate Kefir", "smoothie", 1, 3, [
        ("kefir", 0.75, "cup"),
        ("cherry_frozen", 1, "cup"),
        ("cacao_powder", 1, "tbsp"),
        ("honey", 2, "tsp"),
    ], None),

    ("sm1-white-chocolate-blackberry", "White Chocolate Blackberry", "smoothie", 1, 4, [
        ("milk_whole", 0.75, "cup"),
        ("blackberry_frozen", 0.75, "cup"),
        ("white_chocolate", 1.5, "tbsp"),
        ("ice", 0.5, "cup"),
        ("lemon_zest", 0.5, "tsp"),
    ], "White chocolate seizes in cold liquid, so shave it thin rather than dropping in chunks."),

    # ----------------------------------------------------------- orchard/autumn
    ("sm1-pear-and-fennel-frost", "Pear and Fennel Frost", "smoothie", 1, 5, [
        ("water", 0.75, "cup"),
        ("pear", 1, "piece"),
        ("fennel", 0.5, "cup"),
        ("ice", 0.75, "cup"),
        ("lemon_juice", 1, "tbsp"),
    ], "Use only the white bulb, not the fronds — fronds bring a licorice hit that swamps the pear."),

    ("sm1-persimmon-maple-cream", "Persimmon Maple Cream", "smoothie", 1, 4, [
        ("hemp_milk", 0.75, "cup"),
        ("persimmon", 1, "piece"),
        ("ice", 0.5, "cup"),
        ("maple_syrup", 2, "tsp"),
        ("pecans", 1, "tbsp"),
    ], "Only fully soft Hachiya persimmons work; an underripe one is astringent and will dry your mouth out."),

    ("sm1-green-apple-ginger-snap", "Green Apple Ginger Snap", "smoothie", 1, 4, [
        ("ginger_beer", 0.5, "cup"),
        ("apple_green", 1, "piece"),
        ("ice", 1, "cup"),
        ("ginger", 1, "tsp"),
        ("lemon_juice", 2, "tsp"),
    ], None),

    ("sm1-pumpkin-pear-spice", "Pumpkin Pear Spice", "smoothie", 1, 4, [
        ("oat_milk", 0.75, "cup"),
        ("pumpkin_puree", 0.5, "cup"),
        ("pear", 0.5, "piece"),
        ("ice", 0.5, "cup"),
        ("pumpkin_spice", 0.5, "tsp"),
    ], "Pure pumpkin puree, not pie filling — the filling is already sweetened and spiced and will double up on everything."),

    ("sm1-butternut-orchard", "Butternut Orchard", "smoothie", 1, 5, [
        ("apple_juice", 0.75, "cup"),
        ("butternut", 0.5, "cup"),
        ("apple", 0.5, "piece"),
        ("ice", 0.5, "cup"),
        ("apple_pie_spice", 0.5, "tsp"),
    ], "Roast and chill the squash rather than boiling it; boiled squash is watery and the drink goes thin."),

    ("sm1-concord-freeze", "Concord Freeze", "smoothie", 1, 3, [
        ("grape_juice", 0.75, "cup"),
        ("grape_frozen", 1, "cup"),
        ("lemon_juice", 2, "tsp"),
        ("ice", 0.25, "cup"),
    ], "Frozen grapes are the whole trick — they blend to a sorbet texture no amount of ice will match."),

    ("sm1-fig-walnut-autumn", "Black Mission Fig and Walnut", "smoothie", 1, 4, [
        ("milk_2", 1, "cup"),
        ("fig_dried", 4, "piece"),
        ("walnuts", 1.5, "tbsp"),
        ("ice", 0.75, "cup"),
        ("cinnamon", 0.25, "tsp"),
    ], "Snip the hard stem nub off each dried fig — it never softens and you will feel it in every sip."),

    # ------------------------------------------ freezer medleys, light, low sugar
    ("sm1-freezer-drawer-medley", "Freezer Drawer Medley", "smoothie", 1, 2, [
        ("coconut_water", 0.75, "cup"),
        ("berries_mixed_frozen", 0.5, "cup"),
        ("mango_frozen", 0.5, "cup"),
        ("banana_frozen", 0.25, "cup"),
        ("lime_juice", 2, "tsp"),
    ], "Whatever bags are nearly empty, roughly a cup and a quarter total — the lime is what stops random combinations tasting muddy."),

    ("sm1-cauliflower-vanilla-cloud", "Cauliflower Vanilla Cloud", "smoothie", 1, 3, [
        ("soy_milk", 0.75, "cup"),
        ("cauliflower_frozen", 1, "cup"),
        ("banana_frozen", 0.5, "cup"),
        ("vanilla_bean", 0.5, "tsp"),
        ("cinnamon", 0.25, "tsp"),
    ], None),

    ("sm1-carrot-orange-frost", "Carrot Orange Frost", "smoothie", 1, 4, [
        ("carrot_juice", 0.5, "cup"),
        ("orange", 1, "piece"),
        ("ice", 1, "cup"),
        ("ginger", 1, "tsp"),
        ("turmeric", 0.25, "tsp"),
    ], "Turmeric stains the gasket permanently — rinse the cup and the blade seal within a few minutes."),

    ("sm1-zucchini-lemon-cooler", "Zucchini Lemon Cooler", "smoothie", 1, 3, [
        ("water", 0.75, "cup"),
        ("zucchini_frozen", 0.75, "cup"),
        ("lemon_juice", 2, "tbsp"),
        ("ice", 0.5, "cup"),
        ("stevia", 0.125, "tsp"),
    ], None),

    ("sm1-jicama-lime-crush", "Jicama Lime Crush", "smoothie", 1, 5, [
        ("water", 0.75, "cup"),
        ("jicama", 0.75, "cup"),
        ("ice", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("tajin", 0.25, "tsp"),
    ], "Peel jicama with a knife, not a peeler — the skin is thicker and tougher than it looks."),

    ("sm1-tomato-strawberry-chill", "Tomato Strawberry Chill", "smoothie", 1, 4, [
        ("water", 0.5, "cup"),
        ("cherry_tomato", 8, "piece"),
        ("strawberry_frozen", 0.75, "cup"),
        ("basil", 1, "tbsp"),
        ("balsamic", 0.5, "tsp"),
    ], None),

    ("sm1-maple-water-berry", "Maple Water Berry", "smoothie", 1, 2, [
        ("maple_water", 1, "cup"),
        ("blueberry_frozen", 1, "cup"),
        ("chia", 1, "tbsp"),
    ], "Add the chia after everything else is blended and let it stand two minutes, or it clumps around the blade."),

    ("sm1-prickly-pear-cooler", "Prickly Pear Cooler", "smoothie", 1, 5, [
        ("cactus_water", 0.5, "cup"),
        ("prickly_pear", 2, "piece"),
        ("ice", 1, "cup"),
        ("lime_juice", 1, "tbsp"),
        ("agave", 1, "tsp"),
    ], "Wear a glove and scoop the flesh out with a spoon; the fine spines on the skin are the real hazard, not the seeds."),

    ("sm1-banana-oat-everyday", "Everyday Banana Oat", "smoothie", 1, 3, [
        ("oat_milk", 0.75, "cup"),
        ("banana_frozen", 1, "cup"),
        ("oats", 0.25, "cup"),
        ("cinnamon", 0.25, "tsp"),
        ("date_syrup", 2, "tsp"),
    ], "This is the plain Tuesday one — freeze peeled bananas in chunks on a tray so they do not fuse into a brick."),

    ("sm1-avocado-lime-silk", "Avocado Lime Silk", "smoothie", 1, 4, [
        ("coconut_milk_light", 0.75, "cup"),
        ("avocado", 0.5, "piece"),
        ("lime_juice", 1.5, "tbsp"),
        ("ice", 1, "cup"),
        ("agave", 2, "tsp"),
    ], "Avocado gives you silk without dairy, but it browns fast — blend it the minute you cut it open."),
]
