import SwiftUI

struct RecipesView: View {
    @EnvironmentObject private var store: DeviceStore
    @EnvironmentObject private var library: RecipeLibraryStore
    @State private var filter = RecipeFilter()
    @State private var showingFilters = false
    @State private var showingPantry = false
    @State private var surprise: Recipe?

    private let columns = [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]

    private var all: [Recipe] { RecipeBook.all(for: store.kind) }

    var body: some View {
        NavigationStack {
            let results = filter.apply(to: all, guide: store.guide, favorites: library.favorites)

            ScrollView {
                LazyVStack(spacing: 14) {
                    categoryStrip
                    if filter.isPristine {
                        browse
                    } else {
                        header(count: results.count)
                        if results.isEmpty {
                            empty
                        } else {
                            grid(results)
                        }
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
            .sheet(isPresented: $showingPantry) {
                PantryView(recipes: all)
            }
            .navigationDestination(item: $surprise) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }

    // MARK: - Browse

    @ViewBuilder
    private var browse: some View {
        pantryCard

        if !library.favorites.isEmpty {
            shelf(
                title: "Saved",
                recipes: all.filter { library.favorites.contains($0.id) }
            )
        }

        if !library.recents.isEmpty {
            shelf(
                title: "Recently opened",
                recipes: library.recents.compactMap { id in all.first { $0.id == id } }
            )
        }

        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: "Collections")
            VStack(spacing: 8) {
                ForEach(RecipeCollection.all) { collection in
                    Button {
                        var next = collection.filter
                        next.query = ""
                        filter = next
                    } label: {
                        collectionRow(collection)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
        .padding(.horizontal, 16)

        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: "Every category")
            LazyVGrid(columns: columns, spacing: 10) {
                ForEach(RecipeCategory.allCases) { category in
                    let count = all.filter { $0.category == category }.count
                    Button { filter.category = category } label: {
                        categoryTile(category, count: count)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
        .padding(.horizontal, 16)

        Button {
            surprise = all.randomElement()
        } label: {
            HStack(spacing: 8) {
                Image(systemName: "dice.fill")
                Text("Surprise me").fontWeight(.semibold)
            }
            .font(.headline)
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 15)
            .background(BlastTheme.cardLift, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
        }
        .buttonStyle(.plain)
        .padding(.horizontal, 16)
        .padding(.top, 4)

        Text("\(all.count) recipes for the \(store.kind.shortName)")
            .font(.footnote)
            .foregroundStyle(BlastTheme.secondary)
            .frame(maxWidth: .infinity)
            .padding(.top, 6)
    }

    private var pantryCard: some View {
        Button { showingPantry = true } label: {
            HStack(spacing: 14) {
                ZStack {
                    Circle().fill(BlastTheme.red)
                    Image(systemName: "refrigerator.fill")
                        .font(.title3)
                        .foregroundStyle(.white)
                }
                .frame(width: 46, height: 46)
                VStack(alignment: .leading, spacing: 3) {
                    Text("What can I make?")
                        .font(.headline)
                        .foregroundStyle(.white)
                    Text(library.pantry.isEmpty
                         ? "Tell it what's in the kitchen"
                         : "\(library.pantry.count) ingredient\(library.pantry.count == 1 ? "" : "s") on hand")
                        .font(.subheadline)
                        .foregroundStyle(BlastTheme.secondary)
                }
                Spacer(minLength: 0)
                Image(systemName: "chevron.right")
                    .font(.footnote.weight(.bold))
                    .foregroundStyle(BlastTheme.secondary)
            }
            .padding(16)
            .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
        }
        .buttonStyle(.plain)
        .padding(.horizontal, 16)
    }

    private func shelf(title: String, recipes: [Recipe]) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: title)
                .padding(.horizontal, 16)
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 10) {
                    ForEach(recipes) { recipe in
                        NavigationLink {
                            RecipeDetailView(recipe: recipe)
                        } label: {
                            RecipeMiniCard(recipe: recipe)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.horizontal, 16)
            }
        }
    }

    private func collectionRow(_ collection: RecipeCollection) -> some View {
        HStack(spacing: 12) {
            ZStack {
                RoundedRectangle(cornerRadius: 10, style: .continuous).fill(collection.tint)
                Image(systemName: collection.symbol)
                    .font(.footnote.weight(.bold))
                    .foregroundStyle(.white)
            }
            .frame(width: 34, height: 34)
            VStack(alignment: .leading, spacing: 2) {
                Text(collection.title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text(collection.subtitle)
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer(minLength: 0)
            Image(systemName: "chevron.right")
                .font(.caption.weight(.bold))
                .foregroundStyle(BlastTheme.secondary)
        }
        .padding(12)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
    }

    private func categoryTile(_ category: RecipeCategory, count: Int) -> some View {
        HStack(spacing: 10) {
            Image(systemName: category.symbol)
                .font(.subheadline.weight(.bold))
                .foregroundStyle(.white)
                .frame(width: 26, height: 26)
                .background(category.accent, in: RoundedRectangle(cornerRadius: 8, style: .continuous))
            VStack(alignment: .leading, spacing: 1) {
                Text(category.title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text("\(count)")
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer(minLength: 0)
        }
        .padding(10)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
    }

    // MARK: - Results

    private func grid(_ results: [Recipe]) -> some View {
        LazyVGrid(columns: columns, spacing: 12) {
            ForEach(results) { recipe in
                NavigationLink {
                    RecipeDetailView(recipe: recipe)
                } label: {
                    RecipeCard(recipe: recipe, isFavorite: library.isFavorite(recipe.id))
                }
                .buttonStyle(.plain)
                .contextMenu {
                    Button {
                        library.toggleFavorite(recipe.id)
                    } label: {
                        Label(library.isFavorite(recipe.id) ? "Remove from saved" : "Save",
                              systemImage: library.isFavorite(recipe.id) ? "heart.slash" : "heart")
                    }
                }
            }
        }
        .padding(.horizontal, 16)
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

    private func header(count: Int) -> some View {
        HStack {
            Text("\(count) recipe\(count == 1 ? "" : "s")")
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(BlastTheme.secondary)
            Spacer()
            Button("Clear") { filter.reset() }
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(BlastTheme.secondary)
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

// MARK: - What can I make

struct PantryView: View {
    let recipes: [Recipe]

    @EnvironmentObject private var library: RecipeLibraryStore
    @Environment(\.dismiss) private var dismiss
    @State private var query = ""
    @State private var category: FoodCategory?

    private var foods: [Food] {
        FoodBook.all.filter { food in
            (category == nil || food.category == category) && food.matches(query)
        }
    }

    private var matches: [(recipe: Recipe, missing: [Food])] {
        library.matches(in: recipes)
    }

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                if !library.pantry.isEmpty {
                    selectedStrip
                }
                categoryStrip
                    .padding(.vertical, 10)
                List {
                    ForEach(foods) { food in
                        Button {
                            library.togglePantry(food.id)
                        } label: {
                            HStack(spacing: 12) {
                                FoodBadge(category: food.category, size: 30)
                                Text(food.name)
                                    .foregroundStyle(.white)
                                Spacer(minLength: 0)
                                if library.pantry.contains(food.id) {
                                    Image(systemName: "checkmark.circle.fill")
                                        .foregroundStyle(BlastTheme.red)
                                }
                            }
                        }
                        .listRowBackground(BlastTheme.card)
                    }
                }
                .listStyle(.plain)
                .scrollContentBackground(.hidden)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .searchable(text: $query, prompt: "Search ingredients")
            .navigationTitle("In my kitchen")
            .navigationBarTitleDisplayMode(.inline)
            .safeAreaInset(edge: .bottom) {
                if !library.pantry.isEmpty {
                    NavigationLink {
                        PantryMatchesView(matches: matches)
                    } label: {
                        Text(matches.isEmpty
                             ? "No matches yet — add a few more"
                             : "See \(matches.count) recipe\(matches.count == 1 ? "" : "s")")
                            .font(.headline)
                            .foregroundStyle(.white)
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 16)
                            .background(matches.isEmpty ? BlastTheme.cardLift : BlastTheme.red,
                                        in: RoundedRectangle(cornerRadius: 12, style: .continuous))
                    }
                    .buttonStyle(.plain)
                    .disabled(matches.isEmpty)
                    .padding(16)
                    .background(.ultraThinMaterial)
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("Clear") { library.clearPantry() }
                        .foregroundStyle(BlastTheme.secondary)
                        .disabled(library.pantry.isEmpty)
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") { dismiss() }.fontWeight(.semibold)
                }
            }
        }
    }

    private var selectedStrip: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                ForEach(library.pantry.compactMap(FoodBook.food).sorted { $0.name < $1.name }) { food in
                    Button {
                        library.togglePantry(food.id)
                    } label: {
                        HStack(spacing: 5) {
                            Text(food.name).font(.footnote.weight(.semibold))
                            Image(systemName: "xmark").font(.caption2.weight(.bold))
                        }
                        .foregroundStyle(.white)
                        .padding(.horizontal, 10)
                        .padding(.vertical, 7)
                        .background(BlastTheme.red, in: Capsule())
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(.horizontal, 16)
            .padding(.top, 12)
        }
    }

    private var categoryStrip: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                FilterChip(title: "All", isOn: category == nil) { category = nil }
                ForEach(FoodCategory.allCases) { option in
                    FilterChip(title: option.title, isOn: category == option, tint: option.tint) {
                        category = category == option ? nil : option
                    }
                }
            }
            .padding(.horizontal, 16)
        }
    }
}

struct PantryMatchesView: View {
    let matches: [(recipe: Recipe, missing: [Food])]

    private var ready: [(recipe: Recipe, missing: [Food])] { matches.filter { $0.missing.isEmpty } }
    private var nearly: [(recipe: Recipe, missing: [Food])] { matches.filter { !$0.missing.isEmpty } }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                if !ready.isEmpty {
                    section("You can make these now", items: ready)
                }
                if !nearly.isEmpty {
                    section("One or two short", items: nearly)
                }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 28)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle("Matches")
        .navigationBarTitleDisplayMode(.inline)
    }

    private func section(_ title: String, items: [(recipe: Recipe, missing: [Food])]) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: title)
            VStack(spacing: 8) {
                ForEach(items, id: \.recipe.id) { item in
                    NavigationLink {
                        RecipeDetailView(recipe: item.recipe)
                    } label: {
                        HStack(spacing: 12) {
                            Image(systemName: item.recipe.symbol)
                                .font(.subheadline.weight(.bold))
                                .foregroundStyle(.white)
                                .frame(width: 30, height: 30)
                                .background(item.recipe.accent, in: RoundedRectangle(cornerRadius: 8, style: .continuous))
                            VStack(alignment: .leading, spacing: 2) {
                                Text(item.recipe.name)
                                    .font(.subheadline.weight(.semibold))
                                    .foregroundStyle(.white)
                                Text(item.missing.isEmpty
                                     ? "\(item.recipe.totalMinutes) min · everything on hand"
                                     : "need \(item.missing.map { $0.name.lowercased() }.joined(separator: ", "))")
                                    .font(.caption)
                                    .foregroundStyle(BlastTheme.secondary)
                                    .lineLimit(1)
                            }
                            Spacer(minLength: 0)
                            Image(systemName: "chevron.right")
                                .font(.caption.weight(.bold))
                                .foregroundStyle(BlastTheme.secondary)
                        }
                        .padding(12)
                        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }
}

// MARK: - Filters

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
                        chipGrid([.vegan, .dairyFree, .nutFree, .glutenFree])
                    }
                    group("Nutrition") {
                        chipGrid([.highProtein, .lowSugar, .highFiber, .noAddedSugar])
                    }
                    group("Avoid") {
                        chipGrid([.caffeineFree, .noAlcohol])
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
                    group("Show only") {
                        FlowLayout(spacing: 8) {
                            FilterChip(
                                title: "Fits my \(guide.kind.shortName) in one blend",
                                isOn: filter.fitsVesselOnly
                            ) {
                                filter.fitsVesselOnly.toggle()
                            }
                            FilterChip(title: "Saved", isOn: filter.favoritesOnly) {
                                filter.favoritesOnly.toggle()
                            }
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

// MARK: - Cards

struct RecipeCard: View {
    let recipe: Recipe
    var isFavorite = false

    private var facts: RecipeFacts { RecipeIndex.facts(for: recipe) }

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
                        pill("\(Int(facts.perServing.kcal.rounded())) kcal")
                        Spacer(minLength: 4)
                        pill(recipe.program.label)
                    }
                    Spacer()
                    HStack(spacing: 4) {
                        if recipe.printedFor != nil {
                            pill("From the box")
                        }
                        Spacer(minLength: 0)
                        if isFavorite {
                            Image(systemName: "heart.fill")
                                .font(.caption2.weight(.bold))
                                .foregroundStyle(.white)
                                .padding(5)
                                .background(.black.opacity(0.35), in: Circle())
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
        let protein = Int(facts.perServing.protein.rounded())
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

/// The compact card the horizontal shelves use.
struct RecipeMiniCard: View {
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
                    .font(.system(size: 24, weight: .semibold))
                    .foregroundStyle(.white.opacity(0.92))
            }
            .frame(height: 68)
            Text(recipe.name)
                .font(.caption.weight(.semibold))
                .foregroundStyle(.white)
                .lineLimit(2)
                .multilineTextAlignment(.leading)
                .padding(9)
                .frame(maxWidth: .infinity, minHeight: 50, alignment: .topLeading)
        }
        .frame(width: 128)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
        .clipShape(RoundedRectangle(cornerRadius: 14, style: .continuous))
    }
}

// MARK: - Detail

struct RecipeDetailView: View {
    let recipe: Recipe

    @EnvironmentObject private var store: DeviceStore
    @EnvironmentObject private var builder: BlendBuilder
    @EnvironmentObject private var library: RecipeLibraryStore
    @State private var tab = 0
    @State private var loaded = false

    private var facts: RecipeFacts { RecipeIndex.facts(for: recipe) }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                hero
                if facts.volumeML > store.guide.maxFillML + 1 {
                    WarningBanner(text: "This loads about \(Int(facts.volumeML.rounded())) ml, past the MAX FILL line on the \(store.kind.shortName). Halve it or blend it in two batches.")
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
        .onAppear { library.markViewed(recipe.id) }
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                Button {
                    library.toggleFavorite(recipe.id)
                } label: {
                    Image(systemName: library.isFavorite(recipe.id) ? "heart.fill" : "heart")
                        .foregroundStyle(library.isFavorite(recipe.id) ? BlastTheme.red : BlastTheme.secondary)
                }
                .accessibilityLabel(library.isFavorite(recipe.id) ? "Remove from saved" : "Save recipe")
            }
        }
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
                Text("\(recipe.yieldText) · \(Int(facts.perServing.kcal.rounded())) kcal each")
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
                        Text("\(Int(facts.perServing.kcal.rounded()))")
                            .font(.system(size: 40, weight: .bold, design: .rounded))
                            .foregroundStyle(.white)
                        Text("kcal per serving")
                            .font(.subheadline)
                            .foregroundStyle(BlastTheme.secondary)
                        Spacer(minLength: 0)
                    }
                    MacroSplitBar(nutrients: facts.perServing)
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
