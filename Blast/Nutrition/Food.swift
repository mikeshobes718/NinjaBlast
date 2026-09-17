import SwiftUI

struct Nutrients: Codable, Equatable {
    var kcal: Double = 0
    var protein: Double = 0
    var carbs: Double = 0
    var fiber: Double = 0
    var sugar: Double = 0
    var fat: Double = 0

    static func + (lhs: Nutrients, rhs: Nutrients) -> Nutrients {
        Nutrients(
            kcal: lhs.kcal + rhs.kcal,
            protein: lhs.protein + rhs.protein,
            carbs: lhs.carbs + rhs.carbs,
            fiber: lhs.fiber + rhs.fiber,
            sugar: lhs.sugar + rhs.sugar,
            fat: lhs.fat + rhs.fat
        )
    }

    func scaled(_ factor: Double) -> Nutrients {
        Nutrients(
            kcal: kcal * factor,
            protein: protein * factor,
            carbs: carbs * factor,
            fiber: fiber * factor,
            sugar: sugar * factor,
            fat: fat * factor
        )
    }

    /// FDA reference daily values, used for the %DV column.
    static let dailyValue = Nutrients(kcal: 2000, protein: 50, carbs: 275, fiber: 28, sugar: 50, fat: 78)
}

enum FoodCategory: String, Codable, CaseIterable, Identifiable {
    case fruit, frozen, greens, vegetable, liquid, dairy
    case protein, nutSeed, grain, flavor, sweetener, alcohol, other

    var id: String { rawValue }

    var title: String {
        switch self {
        case .fruit: return "Fruit"
        case .frozen: return "Frozen"
        case .greens: return "Greens"
        case .vegetable: return "Veg"
        case .liquid: return "Liquids"
        case .dairy: return "Dairy"
        case .protein: return "Protein"
        case .nutSeed: return "Nuts & seeds"
        case .grain: return "Grains"
        case .flavor: return "Flavor"
        case .sweetener: return "Sweet"
        case .alcohol: return "Alcohol"
        case .other: return "Other"
        }
    }

    var icon: String {
        switch self {
        case .fruit: return "basket.fill"
        case .frozen: return "snowflake"
        case .greens: return "leaf.fill"
        case .vegetable: return "carrot.fill"
        case .liquid: return "drop.fill"
        case .dairy: return "cup.and.saucer.fill"
        case .protein: return "bolt.fill"
        case .nutSeed: return "circle.grid.2x2.fill"
        case .grain: return "square.grid.3x3.fill"
        case .flavor: return "sparkles"
        case .sweetener: return "cube.fill"
        case .alcohol: return "wineglass.fill"
        case .other: return "ellipsis.circle.fill"
        }
    }

    var tint: Color {
        switch self {
        case .fruit: return Color(red: 0.95, green: 0.45, blue: 0.35)
        case .frozen: return Color(red: 0.42, green: 0.75, blue: 0.98)
        case .greens: return Color(red: 0.36, green: 0.8, blue: 0.45)
        case .vegetable: return Color(red: 0.95, green: 0.6, blue: 0.2)
        case .liquid: return Color(red: 0.35, green: 0.55, blue: 0.98)
        case .dairy: return Color(red: 0.85, green: 0.82, blue: 0.7)
        case .protein: return Color(red: 0.88, green: 0.3, blue: 0.4)
        case .nutSeed: return Color(red: 0.72, green: 0.55, blue: 0.32)
        case .grain: return Color(red: 0.8, green: 0.68, blue: 0.4)
        case .flavor: return Color(red: 0.65, green: 0.5, blue: 0.95)
        case .sweetener: return Color(red: 0.95, green: 0.72, blue: 0.3)
        case .alcohol: return Color(red: 0.6, green: 0.7, blue: 0.85)
        case .other: return Color(white: 0.6)
        }
    }
}

enum MeasureUnit: String, Codable, CaseIterable, Identifiable {
    case gram, milliliter, flOz, cup, tbsp, tsp, piece

    var id: String { rawValue }

    var short: String {
        switch self {
        case .gram: return "g"
        case .milliliter: return "ml"
        case .flOz: return "fl oz"
        case .cup: return "cup"
        case .tbsp: return "tbsp"
        case .tsp: return "tsp"
        case .piece: return "ea"
        }
    }

    /// Steps the amount stepper uses for this unit.
    var step: Double {
        switch self {
        case .gram, .milliliter: return 5
        case .flOz: return 0.5
        case .cup: return 0.25
        case .tbsp, .tsp: return 0.5
        case .piece: return 0.5
        }
    }

    var quickAmounts: [Double] {
        switch self {
        case .gram: return [15, 30, 50, 100, 150]
        case .milliliter: return [60, 120, 180, 240, 350]
        case .flOz: return [2, 4, 6, 8, 12]
        case .cup: return [0.25, 0.33, 0.5, 0.75, 1, 1.5]
        case .tbsp, .tsp: return [0.5, 1, 2, 3, 4]
        case .piece: return [0.5, 1, 2, 3]
        }
    }
}

struct DietFlags: Codable {
    let isAnimal: Bool
    let isDairy: Bool
    let hasNuts: Bool
    let hasCaffeine: Bool
    let isAlcohol: Bool
    let hasGluten: Bool
}

struct Food: Identifiable, Codable, Hashable {
    static func == (lhs: Food, rhs: Food) -> Bool { lhs.id == rhs.id }
    func hash(into hasher: inout Hasher) { hasher.combine(id) }

    let id: String
    let name: String
    let category: FoodCategory
    let per100g: Nutrients
    let gramsPerCup: Double?
    let gramsPerPiece: Double?
    let pieceName: String?
    let isLiquid: Bool
    let mlPerGram: Double
    let defaultUnit: MeasureUnit
    let aliases: [String]
    let flags: DietFlags

    var availableUnits: [MeasureUnit] {
        var units: [MeasureUnit] = []
        if gramsPerPiece != nil { units.append(.piece) }
        if gramsPerCup != nil { units += [.cup, .tbsp, .tsp] }
        if isLiquid { units += [.milliliter, .flOz] }
        units.append(.gram)
        return units
    }

    func unitLabel(_ unit: MeasureUnit, amount: Double) -> String {
        guard unit == .piece else { return unit.short }
        let noun = pieceName ?? "piece"
        return amount > 1 ? noun + "s" : noun
    }

    /// True when the piece name already repeats the food name ("medium banana"),
    /// so a recipe line can show the count alone instead of "½ medium banana banana".
    var pieceNameEchoesFoodName: Bool {
        guard let pieceName else { return false }
        let key = name.lowercased().split(separator: " ").last.map(String.init) ?? name.lowercased()
        return pieceName.lowercased().contains(key)
    }

    func grams(amount: Double, unit: MeasureUnit) -> Double {
        switch unit {
        case .gram:
            return amount
        case .milliliter:
            return amount / mlPerGram
        case .flOz:
            return (amount * 29.5735) / mlPerGram
        case .cup:
            return amount * (gramsPerCup ?? (236.588 / mlPerGram))
        case .tbsp:
            return amount * (gramsPerCup ?? (236.588 / mlPerGram)) / 16
        case .tsp:
            return amount * (gramsPerCup ?? (236.588 / mlPerGram)) / 48
        case .piece:
            return amount * (gramsPerPiece ?? 100)
        }
    }

    func nutrients(amount: Double, unit: MeasureUnit) -> Nutrients {
        per100g.scaled(grams(amount: amount, unit: unit) / 100)
    }

    /// Rough volume the ingredient takes up in the vessel.
    func volumeML(amount: Double, unit: MeasureUnit) -> Double {
        grams(amount: amount, unit: unit) * mlPerGram
    }

    func matches(_ query: String) -> Bool {
        let q = query.folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current)
        guard !q.isEmpty else { return true }
        let haystack = ([name, category.title] + aliases)
            .map { $0.folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current) }
        return haystack.contains { $0.contains(q) }
    }
}

enum FoodBook {
    static let all: [Food] = load()
    static let byID: [String: Food] = Dictionary(uniqueKeysWithValues: all.map { ($0.id, $0) })

    static func food(_ id: String) -> Food? { byID[id] }

    private static func load() -> [Food] {
        guard let url = Bundle.main.url(forResource: "foods", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let foods = try? JSONDecoder().decode([Food].self, from: data) else {
            assertionFailure("foods.json missing or malformed")
            return []
        }
        return foods.sorted { $0.name.localizedCaseInsensitiveCompare($1.name) == .orderedAscending }
    }
}

enum Amount {
    private static let fractions: [(value: Double, glyph: String)] = [
        (0.125, "⅛"), (0.25, "¼"), (0.333, "⅓"), (0.5, "½"),
        (0.667, "⅔"), (0.75, "¾"),
    ]

    /// 0.75 -> "¾", 1.5 -> "1½", 240 -> "240"
    static func format(_ value: Double) -> String {
        if value >= 10 || value.truncatingRemainder(dividingBy: 1) == 0 {
            return String(format: "%g", (value * 10).rounded() / 10)
        }
        let whole = floor(value)
        let frac = value - whole
        if let match = fractions.first(where: { abs($0.value - frac) < 0.02 }) {
            return whole == 0 ? match.glyph : "\(Int(whole))\(match.glyph)"
        }
        return String(format: "%g", (value * 100).rounded() / 100)
    }

    static func grams(_ value: Double) -> String {
        value >= 100 ? "\(Int(value.rounded())) g" : String(format: "%.0f g", value)
    }
}
