import SwiftUI

enum DietFilter: String, CaseIterable, Identifiable {
    case vegan, dairyFree, nutFree, glutenFree
    case highProtein, lowSugar, highFiber
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
        case .caffeineFree: return "Caffeine-free"
        case .noAlcohol: return "No alcohol"
        }
    }

    func matches(_ recipe: Recipe) -> Bool {
        switch self {
        case .vegan: return recipe.isVegan
        case .dairyFree: return recipe.isDairyFree
        case .nutFree: return recipe.isNutFree
        case .glutenFree: return recipe.isGlutenFree
        case .highProtein: return recipe.isHighProtein
        case .lowSugar: return recipe.isLowSugar
        case .highFiber: return recipe.isHighFiber
        case .caffeineFree: return !recipe.hasCaffeine
        case .noAlcohol: return !recipe.hasAlcohol
        }
    }
}

enum RecipeSort: String, CaseIterable, Identifiable {
    case standard, calorieLow, calorieHigh, proteinHigh, quickest

    var id: String { rawValue }

    var title: String {
        switch self {
        case .standard: return "Default"
        case .calorieLow: return "Fewest calories"
        case .calorieHigh: return "Most calories"
        case .proteinHigh: return "Most protein"
        case .quickest: return "Quickest"
        }
    }

    func sort(_ recipes: [Recipe]) -> [Recipe] {
        switch self {
        case .standard: return recipes
        case .calorieLow: return recipes.sorted { $0.perServing.kcal < $1.perServing.kcal }
        case .calorieHigh: return recipes.sorted { $0.perServing.kcal > $1.perServing.kcal }
        case .proteinHigh: return recipes.sorted { $0.perServing.protein > $1.perServing.protein }
        case .quickest: return recipes.sorted { $0.totalMinutes < $1.totalMinutes }
        }
    }
}

struct RecipeFilter {
    var query = ""
    var category: RecipeCategory?
    var diets: Set<DietFilter> = []
    var fitsVesselOnly = false
    var maxKcal: Double?
    var sort: RecipeSort = .standard

    var activeCount: Int {
        diets.count + (category == nil ? 0 : 1) + (fitsVesselOnly ? 1 : 0) + (maxKcal == nil ? 0 : 1) + (sort == .standard ? 0 : 1)
    }

    mutating func reset() {
        self = RecipeFilter()
    }

    func apply(to recipes: [Recipe], guide: Guide) -> [Recipe] {
        let filtered = recipes.filter { recipe in
            if let category, recipe.category != category { return false }
            if fitsVesselOnly, !recipe.fits(guide) { return false }
            if let maxKcal, recipe.perServing.kcal > maxKcal { return false }
            if !diets.allSatisfy({ $0.matches(recipe) }) { return false }
            return matchesQuery(recipe)
        }
        return sort.sort(filtered)
    }

    private func matchesQuery(_ recipe: Recipe) -> Bool {
        let q = query.folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current)
            .trimmingCharacters(in: .whitespaces)
        guard !q.isEmpty else { return true }
        var haystack = [recipe.name, recipe.category.title]
        haystack += recipe.ingredients.compactMap { $0.food?.name ?? $0.display }
        return haystack.contains {
            $0.folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current).contains(q)
        }
    }

    /// Short labels shown on a recipe's detail screen.
    static func badges(for recipe: Recipe) -> [String] {
        var badges: [String] = [recipe.category.title]
        if recipe.isHighProtein { badges.append("\(Int(recipe.perServing.protein.rounded()))g protein") }
        if recipe.isVegan { badges.append("Vegan") }
        else if recipe.isDairyFree { badges.append("Dairy-free") }
        if recipe.isLowSugar { badges.append("Low sugar") }
        if recipe.isHighFiber { badges.append("High fiber") }
        if recipe.hasCaffeine { badges.append("Caffeine") }
        if recipe.hasAlcohol { badges.append("Alcohol") }
        return badges
    }
}
