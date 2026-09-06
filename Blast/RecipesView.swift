import SwiftUI

struct RecipesView: View {
    private let columns = [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns: columns, spacing: 12) {
                    ForEach(GuideBook.recipes) { recipe in
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
            }
            .frame(height: 118)
            VStack(alignment: .leading, spacing: 6) {
                Text(recipe.name)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                Text("\(recipe.prep) · \(recipe.yield)")
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
                    .lineLimit(2)
            }
            .padding(12)
            .frame(maxWidth: .infinity, minHeight: 88, alignment: .topLeading)
        }
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
        .clipShape(RoundedRectangle(cornerRadius: 18, style: .continuous))
    }
}

struct RecipeDetailView: View {
    let recipe: Recipe
    @State private var tab = 0

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                hero
                if let note = recipe.batteryNote {
                    HStack(alignment: .top, spacing: 10) {
                        Image(systemName: "battery.25")
                            .foregroundStyle(Color(red: 1, green: 0.84, blue: 0.2))
                        Text(note)
                            .font(.subheadline)
                            .foregroundStyle(.white)
                    }
                    .padding(14)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
                }
                Picker("Section", selection: $tab) {
                    Text("Ingredients").tag(0)
                    Text("Method").tag(1)
                }
                .pickerStyle(.segmented)

                if tab == 0 {
                    Card {
                        VStack(alignment: .leading, spacing: 0) {
                            ForEach(Array(recipe.ingredients.enumerated()), id: \.offset) { index, item in
                                IngredientRow(item: item)
                                if index < recipe.ingredients.count - 1 {
                                    Divider().overlay(BlastTheme.hairline)
                                }
                            }
                        }
                    }
                } else {
                    VStack(spacing: 10) {
                        ForEach(Array(recipe.steps.enumerated()), id: \.offset) { index, text in
                            StepCard(step: BlendStep(id: index + 1, text: text))
                        }
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
                Text(recipe.prep)
                    .font(.headline)
                    .foregroundStyle(.white)
                Text(recipe.yield)
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer()
        }
        .padding(16)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }
}
