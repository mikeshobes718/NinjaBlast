import SwiftUI

struct CounterView: View {
    @EnvironmentObject private var store: DeviceStore
    @EnvironmentObject private var builder: BlendBuilder
    @State private var picking = false
    @State private var editing: BlendEntry?
    @State private var confirmClear = false

    private var shown: Nutrients {
        builder.servings > 1 ? builder.perServing : builder.total
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {
                    totalsCard
                    Card { VesselGauge(volumeML: builder.volumeML, guide: store.guide) }
                    ingredients
                    addButton
                    if !builder.isEmpty {
                        NavigationLink {
                            BreakdownView(
                                title: "This blend",
                                total: builder.total,
                                servings: builder.servings
                            )
                        } label: {
                            HStack {
                                Text("Full nutrition breakdown")
                                    .font(.headline)
                                Spacer()
                                Image(systemName: "chevron.right").font(.footnote.weight(.bold))
                            }
                            .foregroundStyle(.white)
                            .padding(16)
                            .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Counter")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                DeviceMenuButton()
                ToolbarItem(placement: .topBarLeading) {
                    Button("Clear") { confirmClear = true }
                        .foregroundStyle(builder.isEmpty ? BlastTheme.secondary.opacity(0.4) : BlastTheme.secondary)
                        .disabled(builder.isEmpty)
                }
            }
            .confirmationDialog("Clear this blend?", isPresented: $confirmClear, titleVisibility: .visible) {
                Button("Clear ingredients", role: .destructive) { builder.clear() }
            }
            .sheet(isPresented: $picking) {
                FoodPickerSheet { food, amount, unit in
                    builder.add(foodID: food.id, amount: amount, unit: unit)
                }
            }
            .sheet(item: $editing) { entry in
                if let food = entry.food {
                    AmountSheet(
                        food: food,
                        amount: entry.amount,
                        unit: entry.unit,
                        onCommit: { amount, unit in builder.update(entry, amount: amount, unit: unit) },
                        onRemove: { builder.remove(entry) }
                    )
                }
            }
        }
    }

    private var totalsCard: some View {
        Card {
            VStack(alignment: .leading, spacing: 16) {
                HStack(alignment: .firstTextBaseline, spacing: 8) {
                    Text("\(Int(shown.kcal.rounded()))")
                        .font(.system(size: 54, weight: .bold, design: .rounded))
                        .monospacedDigit()
                        .foregroundStyle(.white)
                        .contentTransition(.numericText())
                        .animation(.snappy, value: shown.kcal)
                    Text("kcal")
                        .font(.title3.weight(.semibold))
                        .foregroundStyle(BlastTheme.secondary)
                    Spacer(minLength: 0)
                    VStack(alignment: .trailing, spacing: 2) {
                        Text(builder.servings > 1 ? "PER SERVING" : "WHOLE BLEND")
                            .font(.caption2.weight(.bold))
                            .tracking(0.8)
                            .foregroundStyle(BlastTheme.secondary)
                        if builder.servings > 1 {
                            Text("\(Int(builder.total.kcal.rounded())) kcal total")
                                .font(.caption)
                                .foregroundStyle(BlastTheme.secondary)
                        }
                    }
                }
                MacroSplitBar(nutrients: shown)
                HStack(spacing: 10) {
                    miniStat("Fiber", shown.fiber)
                    miniStat("Sugar", shown.sugar)
                    Spacer(minLength: 0)
                    servingsStepper
                }
            }
        }
    }

    private func miniStat(_ title: String, _ grams: Double) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text(title.uppercased())
                .font(.caption2.weight(.bold))
                .tracking(0.6)
                .foregroundStyle(BlastTheme.secondary)
            Text("\(Int(grams.rounded())) g")
                .font(.subheadline.weight(.semibold))
                .monospacedDigit()
                .foregroundStyle(.white)
        }
        .frame(minWidth: 52, alignment: .leading)
    }

    private var servingsStepper: some View {
        HStack(spacing: 10) {
            Text("Servings")
                .font(.caption.weight(.semibold))
                .foregroundStyle(BlastTheme.secondary)
            Button {
                builder.servings = max(1, builder.servings - 1)
            } label: {
                Image(systemName: "minus")
            }
            .disabled(builder.servings <= 1)
            Text("\(builder.servings)")
                .font(.subheadline.weight(.bold))
                .monospacedDigit()
                .foregroundStyle(.white)
                .frame(minWidth: 14)
            Button {
                builder.servings = min(4, builder.servings + 1)
            } label: {
                Image(systemName: "plus")
            }
            .disabled(builder.servings >= 4)
        }
        .font(.caption.weight(.bold))
        .buttonStyle(.plain)
        .foregroundStyle(BlastTheme.red)
    }

    @ViewBuilder
    private var ingredients: some View {
        if builder.isEmpty {
            VStack(spacing: 10) {
                Image(systemName: "list.bullet.clipboard")
                    .font(.largeTitle)
                    .foregroundStyle(BlastTheme.secondary)
                Text("Nothing in the cup yet")
                    .font(.headline)
                    .foregroundStyle(.white)
                Text("Add what you pour in as you go. The totals update with every ingredient.")
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
                    .multilineTextAlignment(.center)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 28)
        } else {
            VStack(alignment: .leading, spacing: 8) {
                SectionLabel(text: "In the cup")
                VStack(spacing: 0) {
                    ForEach(Array(builder.entries.enumerated()), id: \.element.id) { index, entry in
                        Button { editing = entry } label: { row(entry) }
                            .buttonStyle(.plain)
                            .contextMenu {
                                Button("Remove", systemImage: "trash", role: .destructive) {
                                    builder.remove(entry)
                                }
                            }
                        if index < builder.entries.count - 1 {
                            Divider().overlay(BlastTheme.hairline).padding(.leading, 62)
                        }
                    }
                }
                .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: BlastTheme.radius, style: .continuous))
            }
        }
    }

    private func row(_ entry: BlendEntry) -> some View {
        HStack(spacing: 12) {
            if let food = entry.food {
                FoodBadge(category: food.category)
                VStack(alignment: .leading, spacing: 2) {
                    Text(food.name)
                        .font(.subheadline.weight(.semibold))
                        .foregroundStyle(.white)
                        .lineLimit(1)
                    Text(entry.amountLabel)
                        .font(.caption)
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
            Spacer(minLength: 8)
            Text("\(Int(entry.nutrients.kcal.rounded()))")
                .font(.subheadline.weight(.bold))
                .monospacedDigit()
                .foregroundStyle(.white)
            Text("kcal")
                .font(.caption2)
                .foregroundStyle(BlastTheme.secondary)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 12)
        .contentShape(Rectangle())
    }

    private var addButton: some View {
        Button { picking = true } label: {
            HStack {
                Image(systemName: "plus.circle.fill")
                Text("Add ingredient").fontWeight(.semibold)
            }
            .font(.headline)
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(BlastTheme.red, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
        }
        .buttonStyle(.plain)
    }
}

struct BreakdownView: View {
    let title: String
    let total: Nutrients
    let servings: Int

    @State private var perServing = true

    private var shown: Nutrients {
        perServing ? total.scaled(1 / Double(max(servings, 1))) : total
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                if servings > 1 {
                    Picker("Basis", selection: $perServing) {
                        Text("Per serving").tag(true)
                        Text("Whole blend").tag(false)
                    }
                    .pickerStyle(.segmented)
                }
                Card {
                    VStack(alignment: .leading, spacing: 0) {
                        HStack {
                            Text("Nutrient").font(.caption.weight(.semibold)).foregroundStyle(BlastTheme.secondary)
                            Spacer()
                            Text("% DV").font(.caption.weight(.semibold)).foregroundStyle(BlastTheme.secondary)
                        }
                        .padding(.bottom, 6)
                        Divider().overlay(BlastTheme.hairline)
                        NutrientRow(title: "Calories", value: shown.kcal, unit: "kcal", dailyValue: Nutrients.dailyValue.kcal, emphasized: true)
                        Divider().overlay(BlastTheme.hairline)
                        NutrientRow(title: "Protein", value: shown.protein, unit: "g", dailyValue: Nutrients.dailyValue.protein, emphasized: true)
                        Divider().overlay(BlastTheme.hairline)
                        NutrientRow(title: "Total fat", value: shown.fat, unit: "g", dailyValue: Nutrients.dailyValue.fat, emphasized: true)
                        Divider().overlay(BlastTheme.hairline)
                        NutrientRow(title: "Total carbs", value: shown.carbs, unit: "g", dailyValue: Nutrients.dailyValue.carbs, emphasized: true)
                        NutrientRow(title: "Fiber", value: shown.fiber, unit: "g", dailyValue: Nutrients.dailyValue.fiber, indented: true)
                        NutrientRow(title: "Sugars", value: shown.sugar, unit: "g", dailyValue: nil, indented: true)
                    }
                }
                Card { MacroSplitBar(nutrients: shown) }
                Text("Percent daily values are based on a 2,000 calorie diet. Values come from standard reference data for each ingredient and are an estimate, not a lab measurement.")
                    .font(.footnote)
                    .foregroundStyle(BlastTheme.secondary)
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 28)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle(title)
        .navigationBarTitleDisplayMode(.inline)
    }
}
