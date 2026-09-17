import SwiftUI

struct RecipesView: View {
    @EnvironmentObject private var store: DeviceStore
    private let columns = [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns: columns, spacing: 12) {
                    ForEach(RecipeBook.all(for: store.kind)) { recipe in
                        NavigationLink {
                            RecipeDetailView(recipe: recipe)
                        } label: {
                            RecipeCard(recipe: recipe)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Recipes")
            .navigationBarTitleDisplayMode(.large)
            .toolbar { DeviceMenuButton() }
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
                    .font(.system(size: 36, weight: .semibold))
                    .foregroundStyle(.white.opacity(0.92))
                VStack {
                    HStack {
                        Text("\(Int(recipe.perServing.kcal.rounded())) kcal")
                            .font(.caption2.weight(.bold))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 8)
                            .padding(.vertical, 4)
                            .background(.black.opacity(0.35), in: Capsule())
                        Spacer()
                        Text(recipe.program.label)
                            .font(.caption2.weight(.bold))
                            .foregroundStyle(.white)
                            .padding(.horizontal, 8)
                            .padding(.vertical, 4)
                            .background(.black.opacity(0.35), in: Capsule())
                    }
                    Spacer()
                }
                .padding(8)
            }
            .frame(height: 118)
            VStack(alignment: .leading, spacing: 6) {
                Text(recipe.name)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                Text("\(recipe.prepMinutes) min · \(recipe.yieldText)")
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
                    .lineLimit(1)
            }
            .padding(12)
            .frame(maxWidth: .infinity, minHeight: 80, alignment: .topLeading)
        }
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .clipShape(RoundedRectangle(cornerRadius: 18, style: .continuous))
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
                    WarningBanner(text: "This makes about \(Int(recipe.volumeML.rounded())) ml, over the MAX FILL line on the \(store.kind.shortName). Halve it or blend it in two batches.")
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
                                .frame(width: 92, alignment: .leading)
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
