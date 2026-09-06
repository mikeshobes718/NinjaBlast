import SwiftUI

enum GuideID: String, Hashable, CaseIterable {
    case parts, battery, setup, blendHow, clean, storage, trouble, warranty
}

struct SpecItem: Identifiable {
    let id: String
    let title: String
    let value: String
    let icon: String
}

struct GuideTopic: Identifiable {
    let id: GuideID
    let title: String
    let subtitle: String
    let icon: String
    let tint: Color
}

struct BlendStep: Identifiable {
    let id: Int
    let text: String
}

struct Ingredient: Identifiable {
    var id: String { amount + name }
    let amount: String
    let name: String
}

struct Recipe: Identifiable {
    let id: String
    let name: String
    let prep: String
    let yield: String
    let batteryNote: String?
    let tip: String?
    let accent: Color
    let symbol: String
    let ingredients: [Ingredient]
    let steps: [String]
}

struct LEDStatus: Identifiable {
    enum Pulse {
        case solid
        case flash
        case pair
        case chase
    }

    let id: String
    let title: String
    let meaning: String
    let action: String
    let colorA: Color
    let colorB: Color?
    let pulse: Pulse
}

enum GuideBook {
    static let model = "BC100BZ"
    static let supportDisplay = "11 3003-9030"
    static let supportTel = "tel:+551130039030"
    static let cycleSeconds: Double = 30

    static let specs: [SpecItem] = [
        SpecItem(id: "cap", title: "Capacity", value: "470 ml", icon: "cup.and.saucer.fill"),
        SpecItem(id: "fill", title: "Fill range", value: "177–400 ml", icon: "drop.fill"),
        SpecItem(id: "cycle", title: "Blend cycle", value: "30 seconds", icon: "timer"),
        SpecItem(id: "charge", title: "Charge", value: "USB-C 15W", icon: "cable.connector"),
        SpecItem(id: "time", title: "Full charge", value: "~2 hours", icon: "bolt.fill"),
        SpecItem(id: "wash", title: "Dishwasher", value: "Cup + lid", icon: "drop.fill"),
    ]

    static let topics: [GuideTopic] = [
        GuideTopic(id: .parts, title: "What's in the box", subtitle: "Six parts, blades stay on the base", icon: "shippingbox.fill", tint: Color(red: 0.45, green: 0.55, blue: 1)),
        GuideTopic(id: .setup, title: "First-time setup", subtitle: "Wash, charge, then blend", icon: "sparkles", tint: Color(red: 1, green: 0.72, blue: 0.2)),
        GuideTopic(id: .blendHow, title: "How to blend", subtitle: "Lock, layer, 30-second cycle", icon: "play.circle.fill", tint: BlastTheme.red),
        GuideTopic(id: .battery, title: "Battery life", subtitle: "Real-world 6–10 blends, not 20", icon: "battery.75", tint: Color(red: 0.35, green: 0.82, blue: 0.45)),
        GuideTopic(id: .clean, title: "Cleaning", subtitle: "Quick clean after every use", icon: "drop.circle.fill", tint: Color(red: 0.35, green: 0.72, blue: 0.95)),
        GuideTopic(id: .storage, title: "Storage", subtitle: "Upright, fully assembled", icon: "archivebox.fill", tint: Color(red: 0.72, green: 0.62, blue: 0.95)),
        GuideTopic(id: .trouble, title: "Troubleshooting", subtitle: "Stuck mix, jammed blades, lid", icon: "wrench.and.screwdriver.fill", tint: Color(red: 1, green: 0.55, blue: 0.2)),
        GuideTopic(id: .warranty, title: "Warranty", subtitle: "1 year, original purchaser", icon: "checkmark.seal.fill", tint: Color(white: 0.72)),
    ]

    static let parts: [String] = [
        "Sip lid (with release button)",
        "Carry handle",
        "Blending cup (470 ml / 16 oz)",
        "Blade cover",
        "Motor base with built-in BlastBlade (not removable)",
        "USB-C charging cable",
    ]

    static let blendSteps: [BlendStep] = [
        BlendStep(id: 1, text: "Align the arrow on the cup with the arrow on the back of the motor base, then twist to lock."),
        BlendStep(id: 2, text: "Press the power button (bottom, power symbol) until Start/Stop lights up."),
        BlendStep(id: 3, text: "Remove the lid. Add liquids first, then fresh/soft food, then frozen fruit or ice last. Stay between MIN LIQUID and MAX FILL."),
        BlendStep(id: 4, text: "Screw the lid on clockwise until it feels sealed."),
        BlendStep(id: 5, text: "Press Start/Stop (top, play/stop icon) for a 30-second cycle. Press again to stop early, or press again after it ends for another 30 seconds."),
        BlendStep(id: 6, text: "When the texture is right, press power to turn the unit OFF before opening the lid."),
        BlendStep(id: 7, text: "Always turn it off before drinking or removing the cup from the base."),
    ]

    static let setupSteps: [BlendStep] = [
        BlendStep(id: 1, text: "Unpack and check you have every part on the What's in the box list."),
        BlendStep(id: 2, text: "First wash: fill the cup with warm water to MIN LIQUID, add one small drop of dish soap, seal the lid, run 30 seconds. Empty and rinse."),
        BlendStep(id: 3, text: "Charge the motor base fully with the USB-C cable. Port is on the back of the base. Wait for solid green or steady purple."),
        BlendStep(id: 4, text: "You're ready to blend."),
    ]

    static let quickClean: [BlendStep] = [
        BlendStep(id: 1, text: "Fill the cup with warm water up to the MIN LIQUID line."),
        BlendStep(id: 2, text: "Add one small drop of dish soap."),
        BlendStep(id: 3, text: "Seal the lid and run a 30-second blend cycle."),
        BlendStep(id: 4, text: "Empty the cup and rinse everything with warm water."),
    ]

    static let leds: [LEDStatus] = [
        LEDStatus(id: "white", title: "Flashing white", meaning: "Cup and base are not aligned.", action: "Realign the arrows on the cup and base, then reseat it.", colorA: .white, colorB: nil, pulse: .flash),
        LEDStatus(id: "orange", title: "Flashing orange", meaning: "Blades are jammed or blocked.", action: "Turn off, clear stuck ingredients, then restart the cycle.", colorA: Color(red: 1, green: 0.55, blue: 0.1), colorB: nil, pulse: .flash),
        LEDStatus(id: "red", title: "Solid red", meaning: "Battery needs charging.", action: "Plug in the USB-C cable and charge.", colorA: BlastTheme.red, colorB: nil, pulse: .solid),
        LEDStatus(id: "redblue", title: "Flashing red + blue", meaning: "Charger is faulty or incompatible.", action: "Use the correct 5V/3A (15W) charger.", colorA: BlastTheme.red, colorB: Color(red: 0.25, green: 0.45, blue: 1), pulse: .pair),
        LEDStatus(id: "chase", title: "Orange, moving clockwise", meaning: "Unit is overheated and cooling down.", action: "Let it rest at room temperature about 15 minutes.", colorA: Color(red: 1, green: 0.45, blue: 0.1), colorB: nil, pulse: .chase),
        LEDStatus(id: "ready", title: "Solid green or steady purple", meaning: "Fully charged / ready to blend.", action: "Good to go.", colorA: Color(red: 0.2, green: 0.85, blue: 0.4), colorB: Color(red: 0.62, green: 0.32, blue: 0.92), pulse: .solid),
        LEDStatus(id: "yellow", title: "Solid yellow", meaning: "Battery is getting low.", action: "Finish up soon and recharge.", colorA: Color(red: 1, green: 0.84, blue: 0.2), colorB: nil, pulse: .solid),
        LEDStatus(id: "fault", title: "Flashing white + red, or flashing red while blending", meaning: "Fault. Needs support.", action: "Call SharkNinja at 11 3003-9030.", colorA: .white, colorB: BlastTheme.red, pulse: .pair),
    ]

    static let recipes: [Recipe] = [
        Recipe(
            id: "beet",
            name: "Beet & Feta Dip",
            prep: "5 min",
            yield: "2 servings · 230 ml",
            batteryNote: nil,
            tip: "Finish with fresh cilantro and pumpkin seeds on top.",
            accent: Color(red: 0.55, green: 0.12, blue: 0.28),
            symbol: "leaf.fill",
            ingredients: [
                Ingredient(amount: "30 ml", name: "olive oil"),
                Ingredient(amount: "1 tbsp", name: "lemon juice"),
                Ingredient(amount: "2 tbsp", name: "plain yogurt"),
                Ingredient(amount: "1 tsp", name: "honey"),
                Ingredient(amount: "1/2", name: "clove garlic, peeled"),
                Ingredient(amount: "150 g", name: "pre-cooked drained beets, chopped"),
                Ingredient(amount: "70 g", name: "feta cheese, cubed"),
                Ingredient(amount: "1/2 tsp", name: "ground cumin"),
                Ingredient(amount: "1 tsp", name: "flaky sea salt"),
                Ingredient(amount: "to taste", name: "ground black pepper"),
            ],
            steps: [
                "Attach the cup to the motor base and turn the blender on with the power button.",
                "Remove the lid and add all ingredients in the order listed. Reseal the lid.",
                "Press Start/Stop for a 30-second blend cycle.",
                "If needed, run another 30-second cycle for a smoother texture.",
                "When done, press the power button to turn off.",
            ]
        ),
        Recipe(
            id: "salsa",
            name: "Creamy Avocado Salsa",
            prep: "5 min",
            yield: "1.5 cups",
            batteryNote: nil,
            tip: "Serve with tortillas.",
            accent: Color(red: 0.22, green: 0.48, blue: 0.28),
            symbol: "carrot.fill",
            ingredients: [
                Ingredient(amount: "2 tbsp", name: "lemon juice"),
                Ingredient(amount: "59 ml", name: "milk of your choice"),
                Ingredient(amount: "1 tsp", name: "kosher salt"),
                Ingredient(amount: "1 tsp", name: "ground black pepper"),
                Ingredient(amount: "1/2", name: "jalapeño, seeded and chopped"),
                Ingredient(amount: "4 g", name: "cilantro, leaves and stems"),
                Ingredient(amount: "59 ml", name: "sour cream"),
                Ingredient(amount: "59 ml", name: "mayonnaise"),
                Ingredient(amount: "1", name: "avocado, pitted, peeled, and cubed"),
            ],
            steps: [
                "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
                "Turn the blender on, then press Start/Stop for a 30-second cycle.",
                "Run another 30-second cycle if you want it smoother.",
                "Turn off and serve with tortillas.",
            ]
        ),
        Recipe(
            id: "vinaigrette",
            name: "Apple Cider Vinaigrette",
            prep: "5 min",
            yield: "1 cup",
            batteryNote: "Light mix. Easy on the battery.",
            tip: nil,
            accent: Color(red: 0.72, green: 0.48, blue: 0.14),
            symbol: "drop.fill",
            ingredients: [
                Ingredient(amount: "118 ml", name: "olive oil"),
                Ingredient(amount: "118 ml", name: "apple cider vinegar"),
                Ingredient(amount: "2 tsp", name: "chopped garlic"),
                Ingredient(amount: "1.5 tbsp", name: "agave syrup"),
                Ingredient(amount: "1/2 tsp", name: "Dijon mustard"),
                Ingredient(amount: "1 tsp", name: "kosher salt"),
                Ingredient(amount: "1 tsp", name: "ground black pepper"),
            ],
            steps: [
                "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
                "Turn the blender on, then press Start/Stop for a 30-second cycle.",
                "Turn off when done.",
            ]
        ),
        Recipe(
            id: "coffee",
            name: "Coffee Protein Shake",
            prep: "5 min",
            yield: "1 serving · 470 ml",
            batteryNote: "Ice-heavy. Plan on fewer blends per charge.",
            tip: nil,
            accent: Color(red: 0.32, green: 0.2, blue: 0.12),
            symbol: "cup.and.saucer.fill",
            ingredients: [
                Ingredient(amount: "1 tbsp", name: "agave syrup (optional)"),
                Ingredient(amount: "118 ml", name: "cold coffee"),
                Ingredient(amount: "118 ml", name: "almond milk"),
                Ingredient(amount: "1", name: "frozen banana, cut into quarters"),
                Ingredient(amount: "29 g", name: "chocolate whey protein"),
                Ingredient(amount: "59 g", name: "ice cubes"),
            ],
            steps: [
                "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
                "Turn the blender on, then press Start/Stop for a 30-second cycle.",
                "Turn off when the shake is smooth.",
            ]
        ),
        Recipe(
            id: "green",
            name: "Mighty Green Smoothie",
            prep: "5 min",
            yield: "1 serving · 470 ml",
            batteryNote: "Frozen fruit. Top up the charge every few uses.",
            tip: nil,
            accent: Color(red: 0.14, green: 0.42, blue: 0.28),
            symbol: "leaf.circle.fill",
            ingredients: [
                Ingredient(amount: "118 ml", name: "orange juice"),
                Ingredient(amount: "118 ml", name: "coconut milk"),
                Ingredient(amount: "15 g", name: "spinach"),
                Ingredient(amount: "1/2", name: "banana, halved"),
                Ingredient(amount: "70 g", name: "frozen mango chunks"),
            ],
            steps: [
                "With the cup attached to the base, add ingredients in the order listed. Seal the lid.",
                "Turn the blender on, then press Start/Stop for a 30-second cycle.",
                "Turn off when the smoothie is smooth.",
            ]
        ),
    ]
}
