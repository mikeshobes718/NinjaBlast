import SwiftUI

struct FoodPickerSheet: View {
    let onPick: (Food, Double, MeasureUnit) -> Void

    @Environment(\.dismiss) private var dismiss
    @State private var query = ""
    @State private var category: FoodCategory?
    @State private var chosen: Food?

    private var results: [Food] {
        FoodBook.all.filter { food in
            (category == nil || food.category == category) && food.matches(query)
        }
    }

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 8) {
                        FilterChip(title: "All", isOn: category == nil) { category = nil }
                        ForEach(FoodCategory.allCases) { cat in
                            FilterChip(title: cat.title, isOn: category == cat, tint: cat.tint) {
                                category = category == cat ? nil : cat
                            }
                        }
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 10)
                }
                if results.isEmpty {
                    ContentUnavailableView(
                        "No match",
                        systemImage: "magnifyingglass",
                        description: Text("Try another name, or pick the closest ingredient.")
                    )
                    .frame(maxHeight: .infinity)
                } else {
                    List(results) { food in
                        Button { chosen = food } label: { row(food) }
                            .listRowBackground(BlastTheme.card)
                    }
                    .listStyle(.plain)
                    .scrollContentBackground(.hidden)
                }
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Add ingredient")
            .navigationBarTitleDisplayMode(.inline)
            .searchable(text: $query, placement: .navigationBarDrawer(displayMode: .always), prompt: "Search \(FoodBook.all.count) ingredients")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") { dismiss() }
                }
            }
            .navigationDestination(item: $chosen) { food in
                AmountEditor(
                    food: food,
                    amount: Self.defaultAmount(for: food),
                    unit: food.defaultUnit,
                    commitTitle: "Add to blend",
                    onCommit: { amount, unit in
                        onPick(food, amount, unit)
                        dismiss()
                    },
                    onRemove: nil
                )
            }
        }
    }

    private func row(_ food: Food) -> some View {
        HStack(spacing: 12) {
            FoodBadge(category: food.category, size: 34)
            VStack(alignment: .leading, spacing: 2) {
                Text(food.name)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text(summary(food))
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer(minLength: 0)
            Image(systemName: "plus.circle.fill")
                .foregroundStyle(BlastTheme.red)
        }
        .padding(.vertical, 4)
    }

    static func defaultAmount(for food: Food) -> Double {
        switch food.defaultUnit {
        case .cup: return food.isLiquid ? 1 : 0.5
        case .tbsp, .tsp: return 1
        case .piece: return 1
        case .gram: return 30
        case .milliliter: return 240
        case .flOz: return 8
        }
    }

    private func summary(_ food: Food) -> String {
        let amount = Self.defaultAmount(for: food)
        let kcal = Int(food.nutrients(amount: amount, unit: food.defaultUnit).kcal.rounded())
        return "\(Amount.format(amount)) \(food.unitLabel(food.defaultUnit, amount: amount)) · \(kcal) kcal"
    }
}

/// Sheet wrapper used when editing an ingredient already in the blend.
struct AmountSheet: View {
    let food: Food
    let amount: Double
    let unit: MeasureUnit
    let onCommit: (Double, MeasureUnit) -> Void
    let onRemove: () -> Void

    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            AmountEditor(
                food: food,
                amount: amount,
                unit: unit,
                commitTitle: "Save",
                onCommit: { amount, unit in
                    onCommit(amount, unit)
                    dismiss()
                },
                onRemove: {
                    onRemove()
                    dismiss()
                }
            )
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Cancel") { dismiss() }
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
        }
        .presentationDetents([.medium, .large])
    }
}

struct AmountEditor: View {
    let food: Food
    @State var amount: Double
    @State var unit: MeasureUnit
    let commitTitle: String
    let onCommit: (Double, MeasureUnit) -> Void
    let onRemove: (() -> Void)?

    private var preview: Nutrients {
        food.nutrients(amount: amount, unit: unit)
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                header
                unitPicker
                amountControls
                previewCard
                Button {
                    onCommit(amount, unit)
                } label: {
                    Text(commitTitle)
                        .font(.headline)
                        .foregroundStyle(.white)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 16)
                        .background(BlastTheme.red, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                }
                .buttonStyle(.plain)
                .disabled(amount <= 0)

                if let onRemove {
                    Button(role: .destructive, action: onRemove) {
                        Text("Remove from blend")
                            .font(.headline)
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 14)
                            .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                    }
                    .buttonStyle(.plain)
                    .foregroundStyle(BlastTheme.red)
                }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 24)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle(food.name)
        .navigationBarTitleDisplayMode(.inline)
    }

    private var header: some View {
        HStack(spacing: 12) {
            FoodBadge(category: food.category, size: 44)
            VStack(alignment: .leading, spacing: 2) {
                Text(food.category.title)
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(BlastTheme.secondary)
                Text("\(Int(food.per100g.kcal.rounded())) kcal per 100 g")
                    .font(.subheadline)
                    .foregroundStyle(.white)
            }
            Spacer(minLength: 0)
        }
    }

    private var unitPicker: some View {
        VStack(alignment: .leading, spacing: 8) {
            SectionLabel(text: "Measure")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 8) {
                    ForEach(food.availableUnits) { option in
                        FilterChip(title: food.unitLabel(option, amount: 1), isOn: option == unit) {
                            guard option != unit else { return }
                            amount = convert(amount, from: unit, to: option)
                            unit = option
                        }
                    }
                }
                .padding(.vertical, 2)
            }
        }
    }

    private var amountControls: some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: "Amount")
            HStack(spacing: 16) {
                stepButton("minus") {
                    amount = max(unit.step, amount - unit.step)
                }
                Text("\(Amount.format(amount)) \(food.unitLabel(unit, amount: amount))")
                    .font(.title2.weight(.bold))
                    .monospacedDigit()
                    .foregroundStyle(.white)
                    .frame(maxWidth: .infinity)
                stepButton("plus") {
                    amount += unit.step
                }
            }
            .padding(.vertical, 6)
            .padding(.horizontal, 12)
            .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 8) {
                    ForEach(unit.quickAmounts, id: \.self) { value in
                        FilterChip(title: Amount.format(value), isOn: abs(amount - value) < 0.001) {
                            amount = value
                        }
                    }
                }
                .padding(.vertical, 2)
            }
        }
    }

    private var previewCard: some View {
        Card {
            VStack(alignment: .leading, spacing: 14) {
                HStack(alignment: .firstTextBaseline, spacing: 6) {
                    Text("\(Int(preview.kcal.rounded()))")
                        .font(.system(size: 36, weight: .bold, design: .rounded))
                        .monospacedDigit()
                        .foregroundStyle(.white)
                        .contentTransition(.numericText())
                        .animation(.snappy, value: preview.kcal)
                    Text("kcal")
                        .font(.headline)
                        .foregroundStyle(BlastTheme.secondary)
                    Spacer(minLength: 0)
                    Text(Amount.grams(food.grams(amount: amount, unit: unit)))
                        .font(.subheadline)
                        .foregroundStyle(BlastTheme.secondary)
                }
                MacroSplitBar(nutrients: preview)
            }
        }
    }

    private func stepButton(_ icon: String, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Image(systemName: icon)
                .font(.headline)
                .foregroundStyle(.white)
                .frame(width: 44, height: 44)
                .background(BlastTheme.cardLift, in: Circle())
        }
        .buttonStyle(.plain)
    }

    /// Keeps roughly the same quantity when the measure changes.
    private func convert(_ value: Double, from: MeasureUnit, to: MeasureUnit) -> Double {
        let grams = food.grams(amount: value, unit: from)
        let perUnit = food.grams(amount: 1, unit: to)
        guard perUnit > 0 else { return value }
        let raw = grams / perUnit
        switch to {
        case .gram, .milliliter: return max((raw / 5).rounded() * 5, 5)
        case .cup, .tbsp, .tsp, .piece: return max((raw * 4).rounded() / 4, 0.25)
        case .flOz: return max((raw * 2).rounded() / 2, 0.5)
        }
    }
}
