import SwiftUI

enum RecipeCategory: String, Codable, CaseIterable, Identifiable {
    case smoothie, green, protein, coffee, breakfast, dessert
    case cocktail, mocktail, kids, wellness, savory

    var id: String { rawValue }

    var title: String {
        switch self {
        case .smoothie: return "Smoothies"
        case .green: return "Greens"
        case .protein: return "Protein"
        case .coffee: return "Coffee"
        case .breakfast: return "Breakfast"
        case .dessert: return "Dessert"
        case .cocktail: return "Cocktails"
        case .mocktail: return "Mocktails"
        case .kids: return "Kids"
        case .wellness: return "Wellness"
        case .savory: return "Savory"
        }
    }

    var symbol: String {
        switch self {
        case .smoothie: return "drop.fill"
        case .green: return "leaf.fill"
        case .protein: return "bolt.fill"
        case .coffee: return "cup.and.saucer.fill"
        case .breakfast: return "sunrise.fill"
        case .dessert: return "birthday.cake.fill"
        case .cocktail: return "wineglass.fill"
        case .mocktail: return "sparkles"
        case .kids: return "face.smiling.fill"
        case .wellness: return "heart.fill"
        case .savory: return "carrot.fill"
        }
    }

    var accent: Color {
        switch self {
        case .smoothie: return Color(red: 0.85, green: 0.25, blue: 0.45)
        case .green: return Color(red: 0.18, green: 0.5, blue: 0.3)
        case .protein: return Color(red: 0.55, green: 0.18, blue: 0.5)
        case .coffee: return Color(red: 0.32, green: 0.2, blue: 0.12)
        case .breakfast: return Color(red: 0.72, green: 0.48, blue: 0.16)
        case .dessert: return Color(red: 0.45, green: 0.2, blue: 0.6)
        case .cocktail: return Color(red: 0.86, green: 0.55, blue: 0.1)
        case .mocktail: return Color(red: 0.15, green: 0.52, blue: 0.62)
        case .kids: return Color(red: 0.9, green: 0.35, blue: 0.25)
        case .wellness: return Color(red: 0.2, green: 0.58, blue: 0.5)
        case .savory: return Color(red: 0.5, green: 0.35, blue: 0.14)
        }
    }
}

enum BlendProgram: String, Codable, CaseIterable, Identifiable {
    case blend, crush

    var id: String { rawValue }
    var label: String { self == .blend ? "BLEND" : "CRUSH" }
}

struct RecipeIngredient: Codable, Identifiable {
    let foodID: String?
    let amount: Double
    let unit: MeasureUnit
    /// Exact wording from a printed insert, when the app must quote it verbatim.
    let display: String?
    /// Prep detail, e.g. "peeled, cored, cut into 1/2-inch chunks".
    let note: String?
    /// Used where a measure has no number, e.g. "pinch" or "to taste".
    let amountDisplay: String?

    var id: String { (foodID ?? display ?? "?") + "\(amount)\(unit.rawValue)" }

    var food: Food? { foodID.flatMap(FoodBook.food) }

    var amountText: String {
        if let amountDisplay { return amountDisplay }
        guard let food else { return Amount.format(amount) }
        return "\(Amount.format(amount)) \(food.unitLabel(unit, amount: amount))"
    }

    var nameText: String {
        if let display { return display }
        guard let food else { return "—" }
        return note.map { "\(food.name.lowercased()), \($0)" } ?? food.name.lowercased()
    }

    var nutrients: Nutrients {
        food?.nutrients(amount: amount, unit: unit) ?? Nutrients()
    }

    var volumeML: Double {
        food?.volumeML(amount: amount, unit: unit) ?? 0
    }

    init(_ foodID: String?, _ amount: Double, _ unit: MeasureUnit, display: String? = nil, note: String? = nil, amountDisplay: String? = nil) {
        self.foodID = foodID
        self.amount = amount
        self.unit = unit
        self.display = display
        self.note = note
        self.amountDisplay = amountDisplay
    }
}

struct Recipe: Identifiable, Codable {
    let id: String
    let name: String
    let category: RecipeCategory
    let program: BlendProgram
    let servings: Int
    let prepMinutes: Int
    let totalMinutes: Int
    let ingredients: [RecipeIngredient]
    let tip: String?
    /// Set only for recipes transcribed from a printed insert, whose wording is quoted.
    let printedSteps: [String]?
    /// Recipes from the box insert are pinned to that device; the library works on both.
    let printedFor: DeviceKind?

    var accent: Color { category.accent }
    var symbol: String { category.symbol }

    var total: Nutrients {
        ingredients.reduce(Nutrients()) { $0 + $1.nutrients }
    }

    var perServing: Nutrients {
        total.scaled(1 / Double(max(servings, 1)))
    }

    var volumeML: Double {
        ingredients.reduce(0) { $0 + $1.volumeML }
    }

    var yieldText: String {
        servings == 1 ? "1 serving" : "serves \(servings)"
    }

    var timeText: String {
        "\(prepMinutes) min prep · \(totalMinutes) min total"
    }

    // Derived from ingredient flags so a filter can never disagree with the recipe.
    var isVegan: Bool { ingredients.allSatisfy { $0.food.map { !$0.flags.isAnimal } ?? true } }
    var isDairyFree: Bool { ingredients.allSatisfy { $0.food.map { !$0.flags.isDairy } ?? true } }
    var isNutFree: Bool { ingredients.allSatisfy { $0.food.map { !$0.flags.hasNuts } ?? true } }
    var isGlutenFree: Bool { ingredients.allSatisfy { $0.food.map { !$0.flags.hasGluten } ?? true } }
    var hasCaffeine: Bool { ingredients.contains { $0.food?.flags.hasCaffeine == true } }
    var hasAlcohol: Bool { ingredients.contains { $0.food?.flags.isAlcohol == true } }

    var isHighProtein: Bool { perServing.protein >= 20 }
    var isLowSugar: Bool { perServing.sugar < 10 }
    var isHighFiber: Bool { perServing.fiber >= 5 }

    func fits(_ guide: Guide) -> Bool {
        volumeML <= guide.maxFillML + 1
    }

    func steps(for guide: Guide) -> [String] {
        if let printedSteps { return printedSteps }
        var steps = [
            "Install the vessel onto the motor base and twist clockwise until it clicks into place.",
            "Turn the unit on and load in fill order: liquid first, then fresh fruit, greens, dry or sticky ingredients, and ice or frozen last.",
            "Secure the lid. Stay between the MIN LIQUID and MAX FILL lines.",
        ]
        if guide.programs.isEmpty {
            steps.append("Press Start/Stop for a 30-second cycle. Run a second cycle if it is not smooth yet.")
        } else {
            steps.append("Select \(program.label). Press it again for a smoother consistency.")
        }
        steps.append("Power the motor base off, remove the vessel, and drink through the sip lid.")
        return steps
    }
}

enum RecipeBook {
    /// The printed insert recipes, plus the full library loaded from JSON.
    static let library: [Recipe] = loadLibrary()

    static func all(for kind: DeviceKind) -> [Recipe] {
        printed.filter { $0.printedFor == kind } + library
    }

    static func recipe(_ id: String) -> Recipe? {
        all.first { $0.id == id }
    }

    static let all: [Recipe] = printed + library

    private static func loadLibrary() -> [Recipe] {
        guard let url = Bundle.main.url(forResource: "recipes", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let recipes = try? JSONDecoder().decode([Recipe].self, from: data) else {
            return []
        }
        return recipes
    }
}
