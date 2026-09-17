import SwiftUI

enum DietFilter: String, CaseIterable, Identifiable {
    case vegan, dairyFree, nutFree, glutenFree
    case highProtein, lowSugar, highFiber, noAddedSugar
    case caffeineFree, noAlcohol

    var id: String { rawValue }

    var title: String {
        switch self {
        case .vegan: return "Vegan"
        case .dairyFree: return "Dairy-free"
        case .nutFree: return "Nut-free"
        case .glutenFree: return "Gluten-free"
        case .highProtein: return "20g+ protein"
        case .lowSugar: return "Low sugar"
        case .highFiber: return "High fiber"
        case .noAddedSugar: return "No added sugar"
        case .caffeineFree: return "Caffeine-free"
        case .noAlcohol: return "No alcohol"
        }
    }

    func matches(_ facts: RecipeFacts) -> Bool {
        switch self {
        case .vegan: return facts.tags.contains(.vegan)
        case .dairyFree: return facts.tags.contains(.dairyFree)
        case .nutFree: return facts.tags.contains(.nutFree)
        case .glutenFree: return facts.tags.contains(.glutenFree)
        case .highProtein: return facts.tags.contains(.highProtein)
        case .lowSugar: return facts.tags.contains(.lowSugar)
        case .highFiber: return facts.tags.contains(.highFiber)
        case .noAddedSugar: return facts.tags.contains(.noAddedSugar)
        case .caffeineFree: return !facts.tags.contains(.caffeine)
        case .noAlcohol: return !facts.tags.contains(.alcohol)
        }
    }
}

enum RecipeSort: String, CaseIterable, Identifiable {
    case standard, calorieLow, calorieHigh, proteinHigh, fiberHigh, sugarLow, quickest, fewestIngredients, alphabetical

    var id: String { rawValue }

    var title: String {
        switch self {
        case .standard: return "Default"
        case .calorieLow: return "Fewest calories"
        case .calorieHigh: return "Most calories"
        case .proteinHigh: return "Most protein"
        case .fiberHigh: return "Most fiber"
        case .sugarLow: return "Least sugar"
        case .quickest: return "Quickest"
        case .fewestIngredients: return "Fewest ingredients"
        case .alphabetical: return "A to Z"
        }
    }

    func sort(_ recipes: [Recipe]) -> [Recipe] {
        func by(_ value: @escaping (RecipeFacts) -> Double, ascending: Bool) -> [Recipe] {
            recipes.sorted { lhs, rhs in
                let l = RecipeIndex.facts(for: lhs), r = RecipeIndex.facts(for: rhs)
                let a = value(l), b = value(r)
                if a == b { return lhs.name.localizedCaseInsensitiveCompare(rhs.name) == .orderedAscending }
                return ascending ? a < b : a > b
            }
        }
        switch self {
        case .standard: return recipes
        case .calorieLow: return by({ $0.perServing.kcal }, ascending: true)
        case .calorieHigh: return by({ $0.perServing.kcal }, ascending: false)
        case .proteinHigh: return by({ $0.perServing.protein }, ascending: false)
        case .fiberHigh: return by({ $0.perServing.fiber }, ascending: false)
        case .sugarLow: return by({ $0.perServing.sugar }, ascending: true)
        case .quickest: return by({ Double($0.totalMinutes) }, ascending: true)
        case .fewestIngredients: return by({ Double($0.ingredientCount) }, ascending: true)
        case .alphabetical:
            return recipes.sorted { $0.name.localizedCaseInsensitiveCompare($1.name) == .orderedAscending }
        }
    }
}

struct RecipeFilter {
    var query = ""
    /// Empty means every category. A set rather than one value so a collection
    /// can gather related categories — frozen drinks are cocktails *and*
    /// mocktails — while the chip strip still toggles one at a time.
    var categories: Set<RecipeCategory> = []
    var diets: Set<DietFilter> = []
    var fitsVesselOnly = false
    var favoritesOnly = false
    var maxKcal: Double?
    var maxMinutes: Int?
    var maxIngredients: Int?
    var sort: RecipeSort = .standard

    /// Convenience for the single-select chip strip.
    var category: RecipeCategory? {
        get { categories.count == 1 ? categories.first : nil }
        set { categories = newValue.map { [$0] } ?? [] }
    }

    var activeCount: Int {
        diets.count
            + (categories.isEmpty ? 0 : 1)
            + (fitsVesselOnly ? 1 : 0)
            + (favoritesOnly ? 1 : 0)
            + (maxKcal == nil ? 0 : 1)
            + (maxMinutes == nil ? 0 : 1)
            + (maxIngredients == nil ? 0 : 1)
            + (sort == .standard ? 0 : 1)
    }

    /// True when the tab is showing the whole library untouched, which is when
    /// the browse shelves are worth showing instead of a wall of cards.
    var isPristine: Bool {
        query.trimmingCharacters(in: .whitespaces).isEmpty && activeCount == 0
    }

    mutating func reset() {
        self = RecipeFilter()
    }

    func apply(to recipes: [Recipe], guide: Guide, favorites: Set<String> = []) -> [Recipe] {
        let q = query.searchFolded.trimmingCharacters(in: .whitespaces)
        let terms = q.split(separator: " ").map(String.init)
        let maxFill = guide.maxFillML + 1

        let filtered = recipes.filter { recipe in
            if !categories.isEmpty, !categories.contains(recipe.category) { return false }
            if favoritesOnly, !favorites.contains(recipe.id) { return false }
            guard let facts = RecipeIndex.facts(recipe.id) else { return false }
            if fitsVesselOnly, facts.volumeML > maxFill { return false }
            if let maxKcal, facts.perServing.kcal > maxKcal { return false }
            if let maxMinutes, facts.totalMinutes > maxMinutes { return false }
            if let maxIngredients, facts.ingredientCount > maxIngredients { return false }
            for diet in diets where !diet.matches(facts) { return false }
            // Every word has to land somewhere, so "frozen mango" narrows
            // rather than returning everything frozen plus everything mango.
            for term in terms where !facts.searchText.contains(term) { return false }
            return true
        }
        return sort.sort(filtered)
    }

    /// Short labels shown on a recipe's detail screen.
    static func badges(for recipe: Recipe) -> [String] {
        let facts = RecipeIndex.facts(for: recipe)
        var badges: [String] = [recipe.category.title]
        if facts.tags.contains(.highProtein) { badges.append("\(Int(facts.perServing.protein.rounded()))g protein") }
        if facts.tags.contains(.vegan) { badges.append("Vegan") }
        else if facts.tags.contains(.dairyFree) { badges.append("Dairy-free") }
        if facts.tags.contains(.lowSugar) { badges.append("Low sugar") }
        if facts.tags.contains(.highFiber) { badges.append("High fiber") }
        if facts.tags.contains(.caffeine) { badges.append("Caffeine") }
        if facts.tags.contains(.alcohol) { badges.append("Alcohol") }
        return badges
    }
}

/// A named shelf on the Recipes tab. Each one is just a filter with a face on
/// it, so a collection can never show something the filters would disagree with.
struct RecipeCollection: Identifiable {
    let id: String
    let title: String
    let subtitle: String
    let symbol: String
    let tint: Color
    let filter: RecipeFilter

    static let all: [RecipeCollection] = [
        RecipeCollection(
            id: "quick", title: "Four minutes or less", subtitle: "Out the door fast",
            symbol: "bolt.fill", tint: Color(red: 0.95, green: 0.65, blue: 0.15),
            filter: { var f = RecipeFilter(); f.maxMinutes = 4; f.sort = .quickest; return f }()
        ),
        RecipeCollection(
            id: "protein", title: "20g protein and up", subtitle: "After the gym",
            symbol: "figure.strengthtraining.traditional", tint: Color(red: 0.55, green: 0.18, blue: 0.5),
            filter: { var f = RecipeFilter(); f.diets = [.highProtein]; f.sort = .proteinHigh; return f }()
        ),
        RecipeCollection(
            id: "light", title: "Under 200 calories", subtitle: "Light but not thin",
            symbol: "leaf.fill", tint: Color(red: 0.2, green: 0.6, blue: 0.45),
            filter: { var f = RecipeFilter(); f.maxKcal = 200; f.sort = .calorieLow; return f }()
        ),
        RecipeCollection(
            id: "vegan", title: "Fully plant-based", subtitle: "No animal products",
            symbol: "carrot.fill", tint: Color(red: 0.25, green: 0.55, blue: 0.3),
            filter: { var f = RecipeFilter(); f.diets = [.vegan]; return f }()
        ),
        RecipeCollection(
            id: "nosugar", title: "Nothing added", subtitle: "Sweetness from the fruit only",
            symbol: "drop.degreesign", tint: Color(red: 0.35, green: 0.55, blue: 0.9),
            filter: { var f = RecipeFilter(); f.diets = [.noAddedSugar]; return f }()
        ),
        RecipeCollection(
            id: "fiber", title: "High fiber", subtitle: "Oats, chia, flax and berries",
            symbol: "circle.grid.2x2.fill", tint: Color(red: 0.72, green: 0.48, blue: 0.16),
            filter: { var f = RecipeFilter(); f.diets = [.highFiber]; f.sort = .fiberHigh; return f }()
        ),
        RecipeCollection(
            id: "frozen", title: "Frozen and blended", subtitle: "Cocktails and mocktails",
            symbol: "snowflake", tint: Color(red: 0.42, green: 0.75, blue: 0.98),
            filter: { var f = RecipeFilter(); f.categories = [.cocktail, .mocktail]; return f }()
        ),
        RecipeCollection(
            id: "five", title: "Five ingredients or fewer", subtitle: "Short shopping list",
            symbol: "list.bullet", tint: Color(red: 0.6, green: 0.45, blue: 0.85),
            filter: { var f = RecipeFilter(); f.maxIngredients = 5; f.sort = .fewestIngredients; return f }()
        ),
    ]
}
