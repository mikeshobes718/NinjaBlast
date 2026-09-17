import SwiftUI

enum GuideID: String, Hashable, CaseIterable {
    case parts, battery, setup, blendHow, programs, clean, storage, trouble, warranty
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

struct Program: Identifiable {
    let id: String
    let name: String
    let detail: String
    let icon: String
    let tint: Color
}

struct LoadLayer: Identifiable {
    var id: String { title }
    let title: String
    let subtitle: String
    let tint: Color
}

struct TroubleBlock: Identifiable {
    var id: String { title }
    let title: String
    let lines: [String]
}

struct BatteryInfo {
    let claim: String?
    let real: String?
    let claimCaption: String
    let realCaption: String
    let headline: String
    let body: [String]
    let tips: [String]
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

struct Guide {
    let kind: DeviceKind
    let wordmark: String
    let tagline: String
    let model: String
    let volume: String
    let cycleLabel: String
    let timerNote: String
    let specs: [SpecItem]
    let topics: [GuideTopic]
    let parts: [String]
    let partsNote: String
    let setupSteps: [BlendStep]
    let blendSteps: [BlendStep]
    let blendWarnings: [String]
    let programs: [Program]
    let loadOrder: [LoadLayer]
    let fillNote: String
    let quickClean: [BlendStep]
    let handWash: [String]
    let dishwasher: [String]
    let cleanWarning: String
    let storage: [String]
    let battery: BatteryInfo
    let troubles: [TroubleBlock]
    let leds: [LEDStatus]
    let ledNote: String?
    let minLiquidML: Double
    let maxFillML: Double

    func topic(_ id: GuideID) -> GuideTopic? {
        topics.first { $0.id == id }
    }
}

enum GuideBook {
    static let supportDisplay = "11 3003-9030"
    static let supportTel = "tel:+551130039030"

    static func guide(for kind: DeviceKind) -> Guide {
        switch kind {
        case .blast: return blast
        case .blastMax: return blastMax
        }
    }
}

private let iceTint = Color(red: 0.35, green: 0.72, blue: 0.95)
private let freshTint = Color(red: 0.35, green: 0.78, blue: 0.48)
private let liquidTint = Color(red: 0.28, green: 0.48, blue: 0.95)
private let dryTint = Color(red: 0.95, green: 0.68, blue: 0.25)
private let greensTint = Color(red: 0.42, green: 0.8, blue: 0.4)
private let greenLED = Color(red: 0.2, green: 0.85, blue: 0.4)

extension GuideBook {
    static let blast = Guide(
        kind: .blast,
        wordmark: "NINJA BLAST",
        tagline: "Portable blender",
        model: "BC100BZ",
        volume: "470 ml · 16 oz",
        cycleLabel: "30-SECOND CYCLE",
        timerNote: "Matches one press of Start/Stop on the blender. Run another cycle if it is not smooth yet.",
        specs: [
            SpecItem(id: "cap", title: "Capacity", value: "470 ml", icon: "cup.and.saucer.fill"),
            SpecItem(id: "fill", title: "Fill range", value: "177–400 ml", icon: "drop.fill"),
            SpecItem(id: "cycle", title: "Blend cycle", value: "30 seconds", icon: "timer"),
            SpecItem(id: "charge", title: "Charge", value: "USB-C 15W", icon: "cable.connector"),
            SpecItem(id: "time", title: "Full charge", value: "~2 hours", icon: "bolt.fill"),
            SpecItem(id: "wash", title: "Dishwasher", value: "Cup + lid", icon: "drop.fill"),
        ],
        topics: [
            GuideTopic(id: .parts, title: "What's in the box", subtitle: "Six parts, blades stay on the base", icon: "shippingbox.fill", tint: Color(red: 0.45, green: 0.55, blue: 1)),
            GuideTopic(id: .setup, title: "First-time setup", subtitle: "Wash, charge, then blend", icon: "sparkles", tint: Color(red: 1, green: 0.72, blue: 0.2)),
            GuideTopic(id: .blendHow, title: "How to blend", subtitle: "Lock, layer, 30-second cycle", icon: "play.circle.fill", tint: BlastTheme.red),
            GuideTopic(id: .battery, title: "Battery life", subtitle: "Real-world 6–10 blends, not 20", icon: "battery.75", tint: Color(red: 0.35, green: 0.82, blue: 0.45)),
            GuideTopic(id: .clean, title: "Cleaning", subtitle: "Quick clean after every use", icon: "drop.circle.fill", tint: iceTint),
            GuideTopic(id: .storage, title: "Storage", subtitle: "Upright, fully assembled", icon: "archivebox.fill", tint: Color(red: 0.72, green: 0.62, blue: 0.95)),
            GuideTopic(id: .trouble, title: "Troubleshooting", subtitle: "Stuck mix, jammed blades, lid", icon: "wrench.and.screwdriver.fill", tint: Color(red: 1, green: 0.55, blue: 0.2)),
            GuideTopic(id: .warranty, title: "Warranty", subtitle: "1 year, original purchaser", icon: "checkmark.seal.fill", tint: Color(white: 0.72)),
        ],
        parts: [
            "Sip lid (with release button)",
            "Carry handle",
            "Blending cup (470 ml / 16 oz)",
            "Blade cover",
            "Motor base with built-in BlastBlade (not removable)",
            "USB-C charging cable",
        ],
        partsNote: "The BlastBlade assembly is built into the motor base. It is not removable.",
        setupSteps: [
            BlendStep(id: 1, text: "Unpack and check you have every part on the What's in the box list."),
            BlendStep(id: 2, text: "First wash: fill the cup with warm water to MIN LIQUID, add one small drop of dish soap, seal the lid, run 30 seconds. Empty and rinse."),
            BlendStep(id: 3, text: "Charge the motor base fully with the USB-C cable. Port is on the back of the base. Wait for solid green or steady purple."),
            BlendStep(id: 4, text: "You're ready to blend."),
        ],
        blendSteps: [
            BlendStep(id: 1, text: "Align the arrow on the cup with the arrow on the back of the motor base, then twist to lock."),
            BlendStep(id: 2, text: "Press the power button (bottom, power symbol) until Start/Stop lights up."),
            BlendStep(id: 3, text: "Remove the lid. Add liquids first, then fresh/soft food, then frozen fruit or ice last. Stay between MIN LIQUID and MAX FILL."),
            BlendStep(id: 4, text: "Screw the lid on clockwise until it feels sealed."),
            BlendStep(id: 5, text: "Press Start/Stop (top, play/stop icon) for a 30-second cycle. Press again to stop early, or press again after it ends for another 30 seconds."),
            BlendStep(id: 6, text: "When the texture is right, press power to turn the unit OFF before opening the lid."),
            BlendStep(id: 7, text: "Always turn it off before drinking or removing the cup from the base."),
        ],
        blendWarnings: [
            "Never run the blender empty. Never blend hot, carbonated, or fizzy liquids. Pressure can pop the lid off.",
            "Blades are sharp and stay on the motor base. Keep hands, hair, and loose clothing away from the cup.",
        ],
        programs: [],
        loadOrder: [
            LoadLayer(title: "Ice / frozen last", subtitle: "Fruit, ice cubes", tint: iceTint),
            LoadLayer(title: "Fresh / soft", subtitle: "Fruit, greens, yogurt", tint: freshTint),
            LoadLayer(title: "Liquids first", subtitle: "At least MIN LIQUID · ~177 ml", tint: liquidTint),
        ],
        fillNote: "Never go below MIN LIQUID or above MAX FILL (~400 ml).",
        quickClean: [
            BlendStep(id: 1, text: "Fill the cup with warm water up to the MIN LIQUID line."),
            BlendStep(id: 2, text: "Add one small drop of dish soap."),
            BlendStep(id: 3, text: "Seal the lid and run a 30-second blend cycle."),
            BlendStep(id: 4, text: "Empty the cup and rinse everything with warm water."),
        ],
        handWash: [
            "Wash the cup and lid with warm, soapy water.",
            "Use a long-handled brush on the blades. Grip the motor base, never the blades.",
            "Wipe the motor base with a clean, damp cloth only.",
            "Rinse everything and air-dry.",
        ],
        dishwasher: [
            "Cup and lid are top-rack dishwasher safe.",
            "Do not use a heated drying cycle.",
            "Take the cup and lid off the motor base first.",
        ],
        cleanWarning: "Never submerge the motor base or put it in the dishwasher. After cleaning near the USB-C port, air-dry 30 minutes before charging.",
        storage: [
            "Store upright, fully assembled (lid + cup + base).",
            "Don't leave blended or unblended ingredients sitting in the cup.",
            "Don't stack anything on top of the unit.",
        ],
        battery: BatteryInfo(
            claim: "15–20",
            real: "6–10",
            claimCaption: "light, mostly liquid",
            realCaption: "typical mixes",
            headline: "Realistic expectation",
            body: [
                "Treat 15–20 blends as a best-case number for thin mixes. Ice and frozen fruit cut that roughly in half. Top up every few uses instead of running it dead.",
                "A full charge takes about 2 hours on USB-C at 5V/3A (15W). Yellow LED means charge soon.",
            ],
            tips: [
                "Charge fully (solid green or purple) before first use and whenever it goes yellow.",
                "Do not leave it sitting fully drained for long periods.",
                "Use the included USB-C cable or a proper 5V/3A charger. A bad charger flashes red and blue.",
                "Skip back-to-back cycles when the battery is already low. That shortens lifespan.",
            ]
        ),
        troubles: [
            TroubleBlock(
                title: "Ingredients keep getting stuck",
                lines: [
                    "Layer correctly: liquid up to MIN LIQUID, then fresh fruit or veg, then greens, then frozen or ice last.",
                    "If it keeps sticking, add a little more liquid.",
                    "Shake while it runs, flip it upside down mid-cycle, then start a new cycle right-side up.",
                ]
            ),
            TroubleBlock(
                title: "Blades locked / won't spin",
                lines: [
                    "Stay at or above MIN LIQUID and under MAX FILL.",
                    "Turn the unit off. Clear the blades with a long utensil, then restart.",
                ]
            ),
            TroubleBlock(
                title: "Lid or cup won't seat",
                lines: [
                    "Set the assembled base or cup on a flat surface.",
                    "Line up the threads evenly, then twist clockwise until it seals.",
                    "When seated, the LED glows solid purple or yellow depending on battery.",
                ]
            ),
            TroubleBlock(
                title: "Control panel won't turn off",
                lines: [
                    "Press the power button to toggle the unit on and off.",
                ]
            ),
        ],
        leds: [
            LEDStatus(id: "white", title: "Flashing white", meaning: "Cup and base are not aligned.", action: "Realign the arrows on the cup and base, then reseat it.", colorA: .white, colorB: nil, pulse: .flash),
            LEDStatus(id: "orange", title: "Flashing orange", meaning: "Blades are jammed or blocked.", action: "Turn off, clear stuck ingredients, then restart the cycle.", colorA: Color(red: 1, green: 0.55, blue: 0.1), colorB: nil, pulse: .flash),
            LEDStatus(id: "red", title: "Solid red", meaning: "Battery needs charging.", action: "Plug in the USB-C cable and charge.", colorA: BlastTheme.red, colorB: nil, pulse: .solid),
            LEDStatus(id: "redblue", title: "Flashing red + blue", meaning: "Charger is faulty or incompatible.", action: "Use the correct 5V/3A (15W) charger.", colorA: BlastTheme.red, colorB: Color(red: 0.25, green: 0.45, blue: 1), pulse: .pair),
            LEDStatus(id: "chase", title: "Orange, moving clockwise", meaning: "Unit is overheated and cooling down.", action: "Let it rest at room temperature about 15 minutes.", colorA: Color(red: 1, green: 0.45, blue: 0.1), colorB: nil, pulse: .chase),
            LEDStatus(id: "ready", title: "Solid green or steady purple", meaning: "Fully charged / ready to blend.", action: "Good to go.", colorA: greenLED, colorB: Color(red: 0.62, green: 0.32, blue: 0.92), pulse: .solid),
            LEDStatus(id: "yellow", title: "Solid yellow", meaning: "Battery is getting low.", action: "Finish up soon and recharge.", colorA: Color(red: 1, green: 0.84, blue: 0.2), colorB: nil, pulse: .solid),
            LEDStatus(id: "fault", title: "Flashing white + red, or flashing red while blending", meaning: "Fault. Needs support.", action: "Call SharkNinja at 11 3003-9030.", colorA: .white, colorB: BlastTheme.red, pulse: .pair),
        ],
        ledNote: nil,
        minLiquidML: 177,
        maxFillML: 400
    )
}

extension GuideBook {
    static let blastMax = Guide(
        kind: .blastMax,
        wordmark: "NINJA BLAST MAX",
        tagline: "Portable blender",
        model: "BC200",
        volume: "590 ml · 20 oz",
        cycleLabel: "30-SECOND BLEND",
        timerNote: "Matches BLEND, the 30-second manual mode. Press the program button again at any time to stop early.",
        specs: [
            SpecItem(id: "cap", title: "Capacity", value: "20 oz · 590 ml", icon: "cup.and.saucer.fill"),
            SpecItem(id: "fill", title: "Fill range", value: "MIN 200 ml → MAX FILL", icon: "drop.fill"),
            SpecItem(id: "blend", title: "Blend", value: "30 seconds, manual", icon: "timer"),
            SpecItem(id: "crush", title: "Crush", value: "Frozen drinks", icon: "snowflake"),
            SpecItem(id: "autoiq", title: "Auto-iQ", value: "Pulses + pauses", icon: "wand.and.stars"),
            SpecItem(id: "time", title: "First charge", value: "Up to 3 hours", icon: "bolt.fill"),
        ],
        topics: [
            GuideTopic(id: .setup, title: "First-time setup", subtitle: "Charge up to 3 hours, then quick clean", icon: "sparkles", tint: Color(red: 1, green: 0.72, blue: 0.2)),
            GuideTopic(id: .blendHow, title: "How to blend", subtitle: "Twist on, load, pick a program", icon: "play.circle.fill", tint: BlastTheme.red),
            GuideTopic(id: .programs, title: "Blend programs", subtitle: "Blend, Auto-iQ, Crush", icon: "dial.medium.fill", tint: Color(red: 0.55, green: 0.5, blue: 0.95)),
            GuideTopic(id: .battery, title: "Charging", subtitle: "Green power light means full", icon: "battery.75", tint: Color(red: 0.35, green: 0.82, blue: 0.45)),
            GuideTopic(id: .clean, title: "3 ways to clean", subtitle: "Quick clean, hand-wash, dishwasher", icon: "drop.circle.fill", tint: iceTint),
            GuideTopic(id: .trouble, title: "Troubleshooting", subtitle: "Too thick, not blending", icon: "wrench.and.screwdriver.fill", tint: Color(red: 1, green: 0.55, blue: 0.2)),
            GuideTopic(id: .warranty, title: "Warranty", subtitle: "1 year, original purchaser", icon: "checkmark.seal.fill", tint: Color(white: 0.72)),
        ],
        parts: [
            "Sip lid",
            "Twist-and-go vessel (20 oz / 590 ml)",
            "Motor base with built-in blades",
            "Charging cable",
        ],
        partsNote: "The blade assembly is built into the motor base. It is not removable.",
        setupSteps: [
            BlendStep(id: 1, text: "Read the enclosed Ninja Owner's Guide before using the unit."),
            BlendStep(id: 2, text: "Fully charge the blender before first use. A full charge takes up to 3 hours."),
            BlendStep(id: 3, text: "Quick clean it: fill the vessel with 6 oz of water and a drop of dish soap, install the lid, install the vessel, and blend for a few seconds."),
            BlendStep(id: 4, text: "Empty, rinse, and you're ready to blend."),
        ],
        blendSteps: [
            BlendStep(id: 1, text: "Install the vessel onto the motor base, twisting clockwise until the vessel clicks onto the motor base."),
            BlendStep(id: 2, text: "Turn the unit ON using the power button and check that the power symbol is GREEN, meaning the battery is full."),
            BlendStep(id: 3, text: "Remove the lid and load in fill order: liquid to the MIN LIQUID line, fresh fruit, leafy greens, dry or sticky ingredients, then ice or frozen last."),
            BlendStep(id: 4, text: "Secure the lid to the vessel. Do not go past the MAX FILL line."),
            BlendStep(id: 5, text: "Select BLEND for shakes and smoothies, or CRUSH for frozen drinks."),
            BlendStep(id: 6, text: "If you want a smoother consistency, press BLEND again. Press the program button at any time to stop early."),
            BlendStep(id: 7, text: "When blending is complete, power the motor base off, remove the vessel, and enjoy through the sip lid."),
        ],
        blendWarnings: [
            "Do not blend without ingredients or without the lid. Do not go past the MAX FILL line when loading the vessel.",
            "Unintentional blending can occur when the lid is removed. Turn the motor base off with the power button when not in use.",
        ],
        programs: [
            Program(id: "blend", name: "BLEND", detail: "30-second manual mode for protein shakes and fruit smoothies.", icon: "timer", tint: BlastTheme.red),
            Program(id: "autoiq", name: "AUTO-iQ", detail: "Pre-programmed pulses and pauses to blend through tough ingredients.", icon: "wand.and.stars", tint: Color(red: 0.55, green: 0.5, blue: 0.95)),
            Program(id: "crush", name: "CRUSH", detail: "For frozen drinks.", icon: "snowflake", tint: iceTint),
        ],
        loadOrder: [
            LoadLayer(title: "5 · Ice / frozen last", subtitle: "Using more frozen? Add more liquid", tint: iceTint),
            LoadLayer(title: "4 · Dry or sticky", subtitle: "Seeds, protein powders, nut butters", tint: dryTint),
            LoadLayer(title: "3 · Leafy greens", subtitle: "Spinach, kale", tint: greensTint),
            LoadLayer(title: "2 · Fresh fruit", subtitle: "Cut in 1–2 inch pieces", tint: freshTint),
            LoadLayer(title: "1 · Liquid first", subtitle: "To or above the MIN LIQUID line", tint: liquidTint),
        ],
        fillNote: "Start at or above MIN LIQUID and never load past MAX FILL. For best results cut ingredients into 1–2 inch pieces.",
        quickClean: [
            BlendStep(id: 1, text: "Remove the vessel and fill it with 6 oz of water and a drop of dish soap."),
            BlendStep(id: 2, text: "Install the lid, then install the vessel on the motor base."),
            BlendStep(id: 3, text: "Blend for a few seconds."),
            BlendStep(id: 4, text: "Empty and rinse."),
        ],
        handWash: [
            "Remove the vessel from the motor base.",
            "Use a long-stemmed dish washing utensil to clean the blades.",
            "Wash the vessel and lid with warm, soapy water, then rinse and air-dry.",
        ],
        dishwasher: [
            "Remove the vessel from the motor base.",
            "Place the vessel and lid on the top rack of the dishwasher.",
        ],
        cleanWarning: "Do not expose the motor base to any liquid.",
        storage: [],
        battery: BatteryInfo(
            claim: nil,
            real: nil,
            claimCaption: "",
            realCaption: "",
            headline: "Charge before you blend",
            body: [
                "For best results, fully charge the blender before first use. A full charge takes up to 3 hours.",
                "Turn the unit on and check the power symbol: GREEN means the battery is full. Every recipe in the guide starts with that check.",
            ],
            tips: [
                "Charge fully before the first blend of the day if you are making anything frozen.",
                "Frozen and ice-heavy drinks use noticeably more charge than shakes.",
            ]
        ),
        troubles: [
            TroubleBlock(
                title: "Smoothie too thick and not blending",
                lines: [
                    "Stop the blend program.",
                    "Add 1 tbsp to 1/4 cup of liquid, then press BLEND until the smoothie comes together.",
                    "Or shake the vessel between blends to move ingredients.",
                    "You can stop the blend mode at any time by pressing the program button again.",
                ]
            ),
            TroubleBlock(
                title: "Output isn't creamy enough",
                lines: [
                    "Remove the vessel from the motor base after processing, shake it, then reinstall the vessel and press BLEND.",
                    "For smoothies, pressing BLEND a second time gives a smoother consistency.",
                ]
            ),
            TroubleBlock(
                title: "Milk drinks expanding",
                lines: [
                    "Milk may expand during processing. If you remove the lid before drinking, do so carefully to avoid spilling.",
                ]
            ),
            TroubleBlock(
                title: "It runs when you didn't mean it to",
                lines: [
                    "Unintentional blending can occur when the lid is removed.",
                    "Turn the motor base off with the power button whenever it is not in use.",
                ]
            ),
        ],
        leds: [
            LEDStatus(id: "green", title: "Green power symbol", meaning: "Battery is full and the unit is ready.", action: "Go ahead and pick BLEND or CRUSH.", colorA: greenLED, colorB: nil, pulse: .solid),
        ],
        ledNote: "The BC200 quick-start card only documents the green ready light. If your Blast MAX shows another color, check the full Ninja Owner's Guide or call support — the BC100 Blast codes do not necessarily apply.",
        minLiquidML: 200,
        maxFillML: 470
    )
}
