import SwiftUI

struct BlendEntry: Identifiable, Codable, Equatable {
    var id = UUID()
    var foodID: String
    var amount: Double
    var unit: MeasureUnit

    var food: Food? { FoodBook.food(foodID) }

    var nutrients: Nutrients {
        food?.nutrients(amount: amount, unit: unit) ?? Nutrients()
    }

    var volumeML: Double {
        food?.volumeML(amount: amount, unit: unit) ?? 0
    }

    var amountLabel: String {
        guard let food else { return "" }
        return "\(Amount.format(amount)) \(food.unitLabel(unit, amount: amount))"
    }
}

@MainActor
final class BlendBuilder: ObservableObject {
    private static let key = "blast.currentBlend"

    @Published var entries: [BlendEntry] = [] { didSet { save() } }
    @Published var servings: Int = 1 { didSet { save() } }

    var total: Nutrients {
        entries.reduce(Nutrients()) { $0 + $1.nutrients }
    }

    var perServing: Nutrients {
        total.scaled(1 / Double(max(servings, 1)))
    }

    var volumeML: Double {
        entries.reduce(0) { $0 + $1.volumeML }
    }

    var isEmpty: Bool { entries.isEmpty }

    func add(foodID: String, amount: Double, unit: MeasureUnit) {
        entries.append(BlendEntry(foodID: foodID, amount: amount, unit: unit))
    }

    func update(_ entry: BlendEntry, amount: Double, unit: MeasureUnit) {
        guard let index = entries.firstIndex(where: { $0.id == entry.id }) else { return }
        entries[index].amount = amount
        entries[index].unit = unit
    }

    func remove(_ entry: BlendEntry) {
        entries.removeAll { $0.id == entry.id }
    }

    func remove(atOffsets offsets: IndexSet) {
        entries.remove(atOffsets: offsets)
    }

    func clear() {
        entries = []
        servings = 1
    }

    func load(_ recipe: Recipe) {
        entries = recipe.ingredients.compactMap { item in
            guard let foodID = item.foodID else { return nil }
            return BlendEntry(foodID: foodID, amount: item.amount, unit: item.unit)
        }
        servings = recipe.servings
    }

    // MARK: - Persistence

    private struct Snapshot: Codable {
        var entries: [BlendEntry]
        var servings: Int
    }

    init() {
        guard let data = UserDefaults.standard.data(forKey: Self.key),
              let snapshot = try? JSONDecoder().decode(Snapshot.self, from: data) else { return }
        entries = snapshot.entries.filter { FoodBook.food($0.foodID) != nil }
        servings = max(snapshot.servings, 1)
    }

    private func save() {
        let snapshot = Snapshot(entries: entries, servings: servings)
        guard let data = try? JSONEncoder().encode(snapshot) else { return }
        UserDefaults.standard.set(data, forKey: Self.key)
    }
}
