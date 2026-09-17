import SwiftUI

struct RecipesView: View {
    @EnvironmentObject private var store: DeviceStore
    @State private var filter = RecipeFilter()
    @State private var showingFilters = false

    private let columns = [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]

    private var results: [Recipe] {
        filter.apply(to: RecipeBook.all(for: store.kind), guide: store.guide)
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVStack(spacing: 14, pinnedViews: []) {
                    categoryStrip
                    header
                    if results.isEmpty {
                        empty
                    } else {
                        LazyVGrid(columns: columns, spacing: 12) {
                            ForEach(results) { recipe in
                                NavigationLink {
                                    RecipeDetailView(recipe: recipe)
                                } label: {
                                    RecipeCard(recipe: recipe)
                                }
                                .buttonStyle(.plain)
                            }
                        }
                        .padding(.horizontal, 16)
                    }
                }
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Recipes")
            .navigationBarTitleDisplayMode(.large)
            .searchable(text: $filter.query, placement: .navigationBarDrawer(displayMode: .always), prompt: "Search recipes or ingredients")
            .toolbar {
                DeviceMenuButton()
                ToolbarItem(placement: .topBarLeading) {
                    Button { showingFilters = true } label: {
                        HStack(spacing: 4) {
                            Image(systemName: filter.activeCount > 0 ? "line.3.horizontal.decrease.circle.fill" : "line.3.horizontal.decrease.circle")
                            if filter.activeCount > 0 {
                                Text("\(filter.activeCount)")
                                    .font(.caption.weight(.bold))
                            }
                        }
                        .foregroundStyle(filter.activeCount > 0 ? BlastTheme.red : BlastTheme.secondary)
                    }
                }
            }
            .sheet(isPresented: $showingFilters) {
                RecipeFilterSheet(filter: $filter, guide: store.guide)
            }
        }
    }

    private var categoryStrip: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                FilterChip(title: "All", isOn: filter.category == nil) { filter.category = nil }
                ForEach(RecipeCategory.allCases) { category in
                    FilterChip(title: category.title, isOn: filter.category == category, tint: category.accent) {
                        filter.category = filter.category == category ? nil : category
                    }
                }
            }
            .padding(.horizontal, 16)
        }
    }

    private var header: some View {
        HStack {
            Text("\(results.count) recipe\(results.count == 1 ? "" : "s")")
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(BlastTheme.secondary)
            Spacer()
            Menu {
                Picker("Sort", selection: $filter.sort) {
                    ForEach(RecipeSort.allCases) { option in
                        Text(option.title).tag(option)
                    }
                }
            } label: {
                HStack(spacing: 4) {
                    Text(filter.sort.title)
                        .font(.subheadline.weight(.semibold))
                    Image(systemName: "arrow.up.arrow.down")
                        .font(.caption.weight(.bold))
                }
                .foregroundStyle(BlastTheme.red)
            }
        }
        .padding(.horizontal, 16)
    }

    private var empty: some View {
        VStack(spacing: 10) {
            Image(systemName: "magnifyingglass")
                .font(.largeTitle)
                .foregroundStyle(BlastTheme.secondary)
            Text("Nothing matches")
                .font(.headline)
                .foregroundStyle(.white)
            Text("Loosen a filter or search for an ingredient you have on hand.")
                .font(.subheadline)
                .foregroundStyle(BlastTheme.secondary)
                .multilineTextAlignment(.center)
            Button("Clear filters") { filter.reset() }
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(BlastTheme.red)
                .padding(.top, 4)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 50)
        .padding(.horizontal, 32)
    }
}

struct RecipeFilterSheet: View {
    @Binding var filter: RecipeFilter
    let guide: Guide

    @Environment(\.dismiss) private var dismiss

    private let calorieOptions: [Double?] = [nil, 150, 250, 350]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    group("Diet") {
                        chipGrid(DietFilter.allCases.filter { [.vegan, .dairyFree, .nutFree, .glutenFree].contains($0) })
                    }
                    group("Nutrition") {
                        chipGrid(DietFilter.allCases.filter { [.highProtein, .lowSugar, .highFiber].contains($0) })
                    }
                    group("Avoid") {
                        chipGrid(DietFilter.allCases.filter { [.caffeineFree, .noAlcohol].contains($0) })
                    }
                    group("Calories per serving") {
                        HStack(spacing: 8) {
                            ForEach(calorieOptions.indices, id: \.self) { index in
                                let value = calorieOptions[index]
                                FilterChip(
                                    title: value.map { "Under \(Int($0))" } ?? "Any",
                                    isOn: filter.maxKcal == value
                                ) {
                                    filter.maxKcal = value
                                }
                            }
                        }
                    }
                    group("Vessel") {
                        FilterChip(
                            title: "Fits my \(guide.kind.shortName) in one blend",
                            isOn: filter.fitsVesselOnly
                        ) {
                            filter.fitsVesselOnly.toggle()
                        }
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Filters")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Reset") {
                        let query = filter.query
                        filter.reset()
                        filter.query = query
                    }
                    .foregroundStyle(BlastTheme.secondary)
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") { dismiss() }.fontWeight(.semibold)
                }
            }
        }
        .presentationDetents([.medium, .large])
    }

    private func group<Content: View>(_ title: String, @ViewBuilder content: () -> Content) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: title)
            content()
        }
    }

    private func chipGrid(_ options: [DietFilter]) -> some View {
        FlowLayout(spacing: 8) {
            ForEach(options) { option in
                FilterChip(title: option.title, isOn: filter.diets.contains(option)) {
                    if filter.diets.contains(option) {
                        filter.diets.remove(option)
                    } else {
                        filter.diets.insert(option)
                    }
                }
            }
        }
    }
}

/// Wraps chips onto as many lines as they need.
struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let width = proposal.width ?? .infinity
        var x: CGFloat = 0, y: CGFloat = 0, rowHeight: CGFloat = 0
        for view in subviews {
            let size = view.sizeThatFits(.unspecified)
            if x + size.width > width, x > 0 {
                x = 0
                y += rowHeight + spacing
                rowHeight = 0
            }
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
        return CGSize(width: width == .infinity ? x : width, height: y + rowHeight)
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        var x = bounds.minX, y = bounds.minY, rowHeight: CGFloat = 0
        for view in subviews {
            let size = view.sizeThatFits(.unspecified)
            if x + size.width > bounds.maxX, x > bounds.minX {
                x = bounds.minX
                y += rowHeight + spacing
                rowHeight = 0
            }
            view.place(at: CGPoint(x: x, y: y), proposal: ProposedViewSize(size))
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
    }
}

struct RecipeCard: View {
    let recipe: Recipe

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ZStack {
                LinearGradient(
                    colors: [recipe.accent, recipe.accent.opacity(0.55)],
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                Image(systemName: recipe.symbol)
                    .font(.system(size: 34, weight: .semibold))
                    .foregroundStyle(.white.opacity(0.92))
                VStack {
                    HStack(alignment: .top) {
                        pill("\(Int(recipe.perServing.kcal.rounded())) kcal")
                        Spacer(minLength: 4)
                        pill(recipe.program.label)
                    }
                    Spacer()
                    if recipe.printedFor != nil {
                        HStack {
                            pill("From the box")
                            Spacer(minLength: 0)
                        }
                    }
                }
                .padding(8)
            }
            .frame(height: 110)
            VStack(alignment: .leading, spacing: 5) {
                Text(recipe.name)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                Text(subtitle)
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
                    .lineLimit(1)
            }
            .padding(12)
            .frame(maxWidth: .infinity, minHeight: 78, alignment: .topLeading)
        }
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .clipShape(RoundedRectangle(cornerRadius: 18, style: .continuous))
    }

    private var subtitle: String {
        let protein = Int(recipe.perServing.protein.rounded())
        if protein >= 15 {
            return "\(recipe.totalMinutes) min · \(protein)g protein"
        }
        return "\(recipe.totalMinutes) min · \(recipe.yieldText)"
    }

    private func pill(_ text: String) -> some View {
        Text(text)
            .font(.caption2.weight(.bold))
            .foregroundStyle(.white)
            .padding(.horizontal, 7)
            .padding(.vertical, 3)
            .background(.black.opacity(0.35), in: Capsule())
    }
}

struct RecipeDetailView: View {
    let recipe: Recipe

    @EnvironmentObject private var store: DeviceStore
    @EnvironmentObject private var builder: BlendBuilder
    @State private var tab = 0
    @State private var loaded = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                hero
                if !recipe.fits(store.guide) {
                    WarningBanner(text: "This loads about \(Int(recipe.volumeML.rounded())) ml, past the MAX FILL line on the \(store.kind.shortName). Halve it or blend it in two batches.")
                }
                tagRow
                Picker("Section", selection: $tab) {
                    Text("Ingredients").tag(0)
                    Text("Method").tag(1)
                    Text("Nutrition").tag(2)
                }
                .pickerStyle(.segmented)

                switch tab {
                case 0: ingredientList
                case 1: method
                default: nutrition
                }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 28)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle(recipe.name)
        .navigationBarTitleDisplayMode(.inline)
    }

    private var hero: some View {
        HStack(spacing: 14) {
            ZStack {
                Circle().fill(recipe.accent)
                Image(systemName: recipe.symbol)
                    .font(.title2)
                    .foregroundStyle(.white)
            }
            .frame(width: 52, height: 52)
            VStack(alignment: .leading, spacing: 4) {
                Text(recipe.timeText)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text("\(recipe.yieldText) · \(Int(recipe.perServing.kcal.rounded())) kcal each")
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
                Text("Program · \(recipe.program.label)")
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(Color(red: 0.45, green: 0.72, blue: 1))
            }
            Spacer(minLength: 0)
        }
        .padding(16)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }

    private var tagRow: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                ForEach(RecipeFilter.badges(for: recipe), id: \.self) { badge in
                    Text(badge)
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(BlastTheme.secondary)
                        .padding(.horizontal, 10)
                        .padding(.vertical, 6)
                        .background(BlastTheme.cardLift, in: Capsule())
                }
            }
        }
    }

    private var ingredientList: some View {
        VStack(spacing: 14) {
            Card {
                VStack(alignment: .leading, spacing: 0) {
                    ForEach(Array(recipe.ingredients.enumerated()), id: \.offset) { index, item in
                        HStack(alignment: .firstTextBaseline, spacing: 12) {
                            Text(item.amountText)
                                .font(.body.weight(.semibold))
                                .foregroundStyle(Color(red: 0.45, green: 0.72, blue: 1))
                                .frame(width: 96, alignment: .leading)
                            Text(item.nameText)
                                .font(.body)
                                .foregroundStyle(.white)
                            Spacer(minLength: 0)
                        }
                        .padding(.vertical, 8)
                        if index < recipe.ingredients.count - 1 {
                            Divider().overlay(BlastTheme.hairline)
                        }
                    }
                }
            }
            loadButton
        }
    }

    private var loadButton: some View {
        Button {
            builder.load(recipe)
            loaded = true
        } label: {
            HStack {
                Image(systemName: loaded ? "checkmark.circle.fill" : "flame.fill")
                Text(loaded ? "Loaded into Counter" : "Send to Counter")
                    .fontWeight(.semibold)
            }
            .font(.headline)
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(loaded ? Color(red: 0.2, green: 0.6, blue: 0.35) : BlastTheme.red,
                        in: RoundedRectangle(cornerRadius: 12, style: .continuous))
        }
        .buttonStyle(.plain)
        .animation(.snappy, value: loaded)
    }

    private var method: some View {
        VStack(spacing: 10) {
            ForEach(Array(recipe.steps(for: store.guide).enumerated()), id: \.offset) { index, text in
                StepCard(step: BlendStep(id: index + 1, text: text))
            }
            if let tip = recipe.tip {
                Card {
                    VStack(alignment: .leading, spacing: 6) {
                        Text("TIP")
                            .font(.caption.weight(.semibold))
                            .tracking(1)
                            .foregroundStyle(BlastTheme.red)
                        Text(tip)
                            .font(.body)
                            .foregroundStyle(.white)
                    }
                }
            }
        }
    }

    private var nutrition: some View {
        VStack(spacing: 14) {
            Card {
                VStack(alignment: .leading, spacing: 14) {
                    HStack(alignment: .firstTextBaseline, spacing: 6) {
                        Text("\(Int(recipe.perServing.kcal.rounded()))")
                            .font(.system(size: 40, weight: .bold, design: .rounded))
                            .foregroundStyle(.white)
                        Text("kcal per serving")
                            .font(.subheadline)
                            .foregroundStyle(BlastTheme.secondary)
                        Spacer(minLength: 0)
                    }
                    MacroSplitBar(nutrients: recipe.perServing)
                }
            }
            NavigationLink {
                BreakdownView(title: recipe.name, total: recipe.total, servings: recipe.servings)
            } label: {
                HStack {
                    Text("Full breakdown").font(.headline)
                    Spacer()
                    Image(systemName: "chevron.right").font(.footnote.weight(.bold))
                }
                .foregroundStyle(.white)
                .padding(16)
                .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
            }
            .buttonStyle(.plain)
            loadButton
        }
    }
}
