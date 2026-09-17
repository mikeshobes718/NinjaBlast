import Foundation

/// Everything the Recipes tab needs to know about a recipe without touching the
/// recipe itself.
///
/// A recipe's nutrition, volume and dietary tags are all derived from its
/// ingredients, which means recomputing them on every keystroke of a search
/// across a thousand-recipe library. So they get computed once, here, and the
/// filtering and sorting work off these facts instead.
struct RecipeFacts {
    let id: String
    let perServing: Nutrients
    let volumeML: Double
    let totalMinutes: Int
    let ingredientCount: Int
    let foodIDs: Set<String>
    let tags: RecipeTags
    /// Folded and lowercased name + category + ingredient names and aliases,
    /// so a search is one `contains` against one string.
    let searchText: String
}

struct RecipeTags: OptionSet {
    let rawValue: Int

    static let vegan          = RecipeTags(rawValue: 1 << 0)
    static let dairyFree      = RecipeTags(rawValue: 1 << 1)
    static let nutFree        = RecipeTags(rawValue: 1 << 2)
    static let glutenFree     = RecipeTags(rawValue: 1 << 3)
    static let caffeine       = RecipeTags(rawValue: 1 << 4)
    static let alcohol        = RecipeTags(rawValue: 1 << 5)
    static let highProtein    = RecipeTags(rawValue: 1 << 6)
    static let lowSugar       = RecipeTags(rawValue: 1 << 7)
    static let highFiber      = RecipeTags(rawValue: 1 << 8)
    /// Nothing sweet was added — any sugar in it came with the fruit.
    static let noAddedSugar   = RecipeTags(rawValue: 1 << 9)
    static let fiveIngredients = RecipeTags(rawValue: 1 << 10)
    static let underTwoHundred = RecipeTags(rawValue: 1 << 11)
}

enum RecipeIndex {
    private static let table: [String: RecipeFacts] = build()

    static func facts(_ id: String) -> RecipeFacts? { table[id] }

    /// Non-optional accessor for the common case: a recipe that came out of
    /// RecipeBook always has facts.
    static func facts(for recipe: Recipe) -> RecipeFacts {
        table[recipe.id] ?? make(recipe)
    }

    private static func build() -> [String: RecipeFacts] {
        Dictionary(uniqueKeysWithValues: RecipeBook.all.map { ($0.id, make($0)) })
    }

    private static let addedSweetener: Set<FoodCategory> = [.sweetener]

    private static func make(_ recipe: Recipe) -> RecipeFacts {
        var tags: RecipeTags = []
        if recipe.isVegan { tags.insert(.vegan) }
        if recipe.isDairyFree { tags.insert(.dairyFree) }
        if recipe.isNutFree { tags.insert(.nutFree) }
        if recipe.isGlutenFree { tags.insert(.glutenFree) }
        if recipe.hasCaffeine { tags.insert(.caffeine) }
        if recipe.hasAlcohol { tags.insert(.alcohol) }
        if recipe.isHighProtein { tags.insert(.highProtein) }
        if recipe.isLowSugar { tags.insert(.lowSugar) }
        if recipe.isHighFiber { tags.insert(.highFiber) }
        if recipe.ingredients.count <= 5 { tags.insert(.fiveIngredients) }

        let perServing = recipe.perServing
        if perServing.kcal < 200 { tags.insert(.underTwoHundred) }

        let foods = recipe.ingredients.compactMap { $0.food }
        if !foods.contains(where: { addedSweetener.contains($0.category) }) {
            tags.insert(.noAddedSugar)
        }

        var terms: [String] = [recipe.name, recipe.category.title]
        for ingredient in recipe.ingredients {
            if let food = ingredient.food {
                terms.append(food.name)
                terms.append(contentsOf: food.aliases)
            } else if let display = ingredient.display {
                terms.append(display)
            }
        }

        return RecipeFacts(
            id: recipe.id,
            perServing: perServing,
            volumeML: recipe.volumeML,
            totalMinutes: recipe.totalMinutes,
            ingredientCount: recipe.ingredients.count,
            foodIDs: Set(recipe.ingredients.compactMap { $0.foodID }),
            tags: tags,
            searchText: terms.joined(separator: " ").searchFolded
        )
    }
}

extension String {
    /// Lowercased and stripped of accents, so "acai" finds "açaí".
    var searchFolded: String {
        folding(options: [.diacriticInsensitive, .caseInsensitive], locale: .current)
    }
}
