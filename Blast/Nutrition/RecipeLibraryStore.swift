import SwiftUI

/// What the person has decided about the library: what they saved, what they
/// looked at, and what is in their kitchen right now.
@MainActor
final class RecipeLibraryStore: ObservableObject {
    private enum Key {
        static let favorites = "blast.favorites"
        static let recents = "blast.recents"
        static let pantry = "blast.pantry"
    }

    private static let recentLimit = 24

    @Published private(set) var favorites: Set<String> {
        didSet { defaults.set(Array(favorites), forKey: Key.favorites) }
    }

    /// Most recently opened first.
    @Published private(set) var recents: [String] {
        didSet { defaults.set(recents, forKey: Key.recents) }
    }

    /// Food ids the person says they have on hand, for "what can I make".
    @Published var pantry: Set<String> {
        didSet { defaults.set(Array(pantry), forKey: Key.pantry) }
    }

    private let defaults: UserDefaults

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        favorites = Set(defaults.stringArray(forKey: Key.favorites) ?? [])
        recents = defaults.stringArray(forKey: Key.recents) ?? []
        pantry = Set(defaults.stringArray(forKey: Key.pantry) ?? [])
    }

    func isFavorite(_ id: String) -> Bool { favorites.contains(id) }

    func toggleFavorite(_ id: String) {
        if favorites.contains(id) {
            favorites.remove(id)
        } else {
            favorites.insert(id)
        }
    }

    func markViewed(_ id: String) {
        var updated = recents.filter { $0 != id }
        updated.insert(id, at: 0)
        if updated.count > Self.recentLimit {
            updated.removeLast(updated.count - Self.recentLimit)
        }
        recents = updated
    }

    func clearRecents() { recents = [] }

    // MARK: - Pantry

    func togglePantry(_ foodID: String) {
        if pantry.contains(foodID) {
            pantry.remove(foodID)
        } else {
            pantry.insert(foodID)
        }
    }

    func clearPantry() { pantry = [] }

    /// Ingredients everyone is assumed to have, so a match isn't held up by
    /// water or a pinch of salt.
    static let assumedOnHand: Set<String> = ["water", "ice", "salt", "black_pepper"]

    /// Recipes ranked by how much of them the pantry already covers.
    ///
    /// A recipe you can make outright comes first; after that, the ones you are
    /// a single ingredient short of, because that is the genuinely useful
    /// answer — it tells you what to pick up.
    func matches(in recipes: [Recipe], maxMissing: Int = 2) -> [(recipe: Recipe, missing: [Food])] {
        guard !pantry.isEmpty else { return [] }
        let have = pantry.union(Self.assumedOnHand)
        var results: [(recipe: Recipe, missing: [Food])] = []
        for recipe in recipes {
            guard let facts = RecipeIndex.facts(recipe.id) else { continue }
            let missingIDs = facts.foodIDs.subtracting(have)
            guard missingIDs.count <= maxMissing else { continue }
            // A recipe that uses nothing you own isn't a match, it's a coincidence.
            guard facts.foodIDs.subtracting(Self.assumedOnHand).intersection(pantry).count >= 1 else { continue }
            let missing = missingIDs.compactMap(FoodBook.food).sorted {
                $0.name.localizedCaseInsensitiveCompare($1.name) == .orderedAscending
            }
            results.append((recipe, missing))
        }
        return results.sorted { lhs, rhs in
            if lhs.missing.count != rhs.missing.count { return lhs.missing.count < rhs.missing.count }
            return lhs.recipe.name.localizedCaseInsensitiveCompare(rhs.recipe.name) == .orderedAscending
        }
    }
}
