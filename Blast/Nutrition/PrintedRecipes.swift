import SwiftUI

/// The recipes printed on the box inserts, quoted as written. `display` keeps the
/// insert's exact wording; the food links exist so they carry nutrition like the
/// rest of the library.
extension RecipeBook {
    static let printed: [Recipe] = blastPrinted + maxPrinted

    private static let blastSteps = [
        "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
        "Turn the blender on, then press Start/Stop for a 30-second cycle.",
        "Run another 30-second cycle if you want it smoother.",
        "Press the power button to turn off.",
    ]

    private static let maxSteps: (String) -> [String] = { program in
        [
            "Install the vessel onto the motor base, twisting clockwise until the vessel clicks onto the motor base.",
            "Turn the unit ON using the power button and ensure the power symbol is GREEN, indicating the battery is full.",
            "Remove the lid and add ingredients to the blending vessel in the order listed. Secure the lid to the vessel.",
            "Select \(program).",
            "When blending is complete, power the motor base off, remove the vessel from the motor base, and enjoy through the sip lid.",
        ]
    }

    static let blastPrinted: [Recipe] = [
        Recipe(
            id: "beet-feta-dip",
            name: "Beet & Feta Dip",
            category: .savory,
            program: .blend,
            servings: 2,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("olive_oil", 30, .milliliter, display: "olive oil"),
                RecipeIngredient("lemon_juice", 1, .tbsp, display: "lemon juice"),
                RecipeIngredient("yogurt_plain", 2, .tbsp, display: "plain yogurt"),
                RecipeIngredient("honey", 1, .tsp, display: "honey"),
                RecipeIngredient("garlic", 0.5, .piece, display: "clove garlic, peeled"),
                RecipeIngredient("beet", 150, .gram, display: "pre-cooked drained beets, chopped"),
                RecipeIngredient("feta", 70, .gram, display: "feta cheese, cubed"),
                RecipeIngredient("cumin", 0.5, .tsp, display: "ground cumin"),
                RecipeIngredient("salt", 1, .tsp, display: "flaky sea salt"),
                RecipeIngredient("black_pepper", 0.5, .tsp, display: "ground black pepper", amountDisplay: "to taste"),
            ],
            tip: "Finish with fresh cilantro and pumpkin seeds on top.",
            printedSteps: [
                "Attach the cup to the motor base and turn the blender on with the power button.",
                "Remove the lid and add all ingredients in the order listed. Reseal the lid.",
                "Press Start/Stop for a 30-second blend cycle.",
                "If needed, run another 30-second cycle for a smoother texture.",
                "When done, press the power button to turn off.",
            ],
            printedFor: .blast
        ),
        Recipe(
            id: "avocado-salsa",
            name: "Creamy Avocado Salsa",
            category: .savory,
            program: .blend,
            servings: 4,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("lemon_juice", 2, .tbsp, display: "lemon juice"),
                RecipeIngredient("milk_whole", 59, .milliliter, display: "milk of your choice"),
                RecipeIngredient("salt", 1, .tsp, display: "kosher salt"),
                RecipeIngredient("black_pepper", 1, .tsp, display: "ground black pepper"),
                RecipeIngredient("jalapeno", 0.5, .piece, display: "jalapeño, seeded and chopped"),
                RecipeIngredient("cilantro", 4, .gram, display: "cilantro, leaves and stems"),
                RecipeIngredient("sour_cream", 59, .milliliter, display: "sour cream"),
                RecipeIngredient("mayonnaise", 59, .milliliter, display: "mayonnaise"),
                RecipeIngredient("avocado", 1, .piece, display: "avocado, pitted, peeled, and cubed"),
            ],
            tip: "Serve with tortillas.",
            printedSteps: blastSteps,
            printedFor: .blast
        ),
        Recipe(
            id: "cider-vinaigrette",
            name: "Apple Cider Vinaigrette",
            category: .savory,
            program: .blend,
            servings: 8,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("olive_oil", 118, .milliliter, display: "olive oil"),
                RecipeIngredient("cider_vinegar", 118, .milliliter, display: "apple cider vinegar"),
                RecipeIngredient("garlic", 6, .gram, display: "chopped garlic", amountDisplay: "2 tsp"),
                RecipeIngredient("agave", 1.5, .tbsp, display: "agave syrup"),
                RecipeIngredient("dijon", 0.5, .tsp, display: "Dijon mustard"),
                RecipeIngredient("salt", 1, .tsp, display: "kosher salt"),
                RecipeIngredient("black_pepper", 1, .tsp, display: "ground black pepper"),
            ],
            tip: nil,
            printedSteps: [
                "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
                "Turn the blender on, then press Start/Stop for a 30-second cycle.",
                "Turn off when done.",
            ],
            printedFor: .blast
        ),
        Recipe(
            id: "coffee-protein-shake",
            name: "Coffee Protein Shake",
            category: .protein,
            program: .blend,
            servings: 1,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("agave", 1, .tbsp, display: "agave syrup (optional)"),
                RecipeIngredient("coffee", 118, .milliliter, display: "cold coffee"),
                RecipeIngredient("almond_milk", 118, .milliliter, display: "almond milk"),
                RecipeIngredient("banana_frozen", 118, .gram, display: "frozen banana, cut into quarters", amountDisplay: "1"),
                RecipeIngredient("whey_chocolate", 29, .gram, display: "chocolate whey protein"),
                RecipeIngredient("ice", 59, .gram, display: "ice cubes"),
            ],
            tip: nil,
            printedSteps: blastSteps,
            printedFor: .blast
        ),
        Recipe(
            id: "mighty-green",
            name: "Mighty Green Smoothie",
            category: .green,
            program: .blend,
            servings: 1,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("orange_juice", 118, .milliliter, display: "orange juice"),
                RecipeIngredient("coconut_milk_bev", 118, .milliliter, display: "coconut milk"),
                RecipeIngredient("spinach", 15, .gram, display: "spinach"),
                RecipeIngredient("banana", 0.5, .piece, display: "banana, halved"),
                RecipeIngredient("mango_frozen", 70, .gram, display: "frozen mango chunks"),
            ],
            tip: nil,
            printedSteps: blastSteps,
            printedFor: .blast
        ),
    ]

    static let maxPrinted: [Recipe] = [
        Recipe(
            id: "carrot-apple-kale",
            name: "Carrot Apple Kale Wake-Up",
            category: .green,
            program: .blend,
            servings: 2,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("carrot_juice", 0.75, .cup, display: "carrot juice"),
                RecipeIngredient("kale", 0.5, .cup, display: "packed chopped kale, stems removed"),
                RecipeIngredient("apple_green", 0.25, .cup, display: "green apple peeled, cored, cut into 1/2-inch chunks"),
                RecipeIngredient("pineapple_frozen", 0.5, .cup, display: "frozen pineapple chunks"),
            ],
            tip: "After blending, if a smoother consistency is desired, press BLEND again.",
            printedSteps: [
                "Install the vessel onto the motor base, twisting clockwise until the vessel clicks onto the motor base.",
                "Turn the unit ON using the power button and ensure the power symbol is GREEN, indicating the battery is full.",
                "Remove the lid and add ingredients to the blending vessel in the order listed. Secure the lid to the vessel.",
                "Select BLEND.",
                "After blending, if a smoother consistency is desired, press BLEND again.",
                "When blending is complete, power the motor base off, remove the vessel from the motor base, and enjoy through the sip lid.",
            ],
            printedFor: .blastMax
        ),
        Recipe(
            id: "frozen-mocha-cold-brew",
            name: "Frozen Mocha Cold Brew",
            category: .coffee,
            program: .crush,
            servings: 2,
            prepMinutes: 3,
            totalMinutes: 4,
            ingredients: [
                RecipeIngredient("cold_brew", 0.75, .cup, display: "cold brew coffee concentrate"),
                RecipeIngredient("milk_whole", 0.5, .cup, display: "whole milk"),
                RecipeIngredient("chocolate_syrup", 0.25, .cup, display: "chocolate syrup"),
                RecipeIngredient("ice", 0.5, .cup, display: "ice"),
            ],
            tip: "Milk may expand during processing. If removing the lid before drinking, do so carefully to avoid spilling.",
            printedSteps: maxSteps("CRUSH"),
            printedFor: .blastMax
        ),
        Recipe(
            id: "mixed-berry-vanilla-protein",
            name: "Mixed Berry Vanilla Protein Smoothie",
            category: .protein,
            program: .blend,
            servings: 2,
            prepMinutes: 3,
            totalMinutes: 4,
            ingredients: [
                RecipeIngredient("oat_milk", 1, .cup, display: "oat milk"),
                RecipeIngredient("whey_vanilla", 1, .piece, display: "vanilla whey protein powder", amountDisplay: "1 scoop (1 oz)"),
                RecipeIngredient("berries_mixed_frozen", 0.75, .cup, display: "mixed frozen berries"),
            ],
            tip: nil,
            printedSteps: maxSteps("BLEND"),
            printedFor: .blastMax
        ),
        Recipe(
            id: "mango-margarita",
            name: "Mango Margarita",
            category: .cocktail,
            program: .crush,
            servings: 2,
            prepMinutes: 4,
            totalMinutes: 5,
            ingredients: [
                RecipeIngredient("tequila", 0.25, .cup, display: "tequila"),
                RecipeIngredient("triple_sec", 3, .tbsp, display: "triple sec"),
                RecipeIngredient("limeade_frozen", 0.5, .cup, display: "frozen lime cocktail mixer"),
                RecipeIngredient("mango_frozen", 0.75, .cup, display: "frozen mango chunks"),
                RecipeIngredient("ice", 0.333, .cup, display: "ice"),
            ],
            tip: "If a creamier output is desired, remove the vessel from the motor base after processing, shake, then reinstall the vessel and press BLEND. Process until complete.",
            printedSteps: maxSteps("CRUSH"),
            printedFor: .blastMax
        ),
        Recipe(
            id: "apple-cinnamon-oat",
            name: "Apple Cinnamon Oat Breakfast Smoothie",
            category: .breakfast,
            program: .blend,
            servings: 2,
            prepMinutes: 5,
            totalMinutes: 6,
            ingredients: [
                RecipeIngredient("milk_whole", 1, .cup, display: "whole milk"),
                RecipeIngredient("maple_syrup", 2, .tbsp, display: "maple syrup"),
                RecipeIngredient("apple_green", 0.5, .cup, display: "green apple, peeled, cored, cut into 1/2-inch chunks"),
                RecipeIngredient("banana_frozen", 0.5, .cup, display: "frozen banana slices"),
                RecipeIngredient("yogurt_vanilla", 0.5, .cup, display: "whole milk vanilla yogurt"),
                RecipeIngredient("cinnamon", 1, .tsp, display: "ground cinnamon"),
                RecipeIngredient("oats", 3, .tbsp, display: "quick oats"),
                RecipeIngredient("salt", 0.4, .gram, display: "kosher salt", amountDisplay: "pinch"),
            ],
            tip: nil,
            printedSteps: maxSteps("BLEND"),
            printedFor: .blastMax
        ),
    ]
}
