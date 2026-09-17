import SwiftUI

enum Macro: String, CaseIterable, Identifiable {
    case protein, carbs, fat

    var id: String { rawValue }

    var title: String {
        switch self {
        case .protein: return "Protein"
        case .carbs: return "Carbs"
        case .fat: return "Fat"
        }
    }

    var tint: Color {
        switch self {
        case .protein: return Color(red: 0.4, green: 0.72, blue: 1)
        case .carbs: return Color(red: 1, green: 0.72, blue: 0.25)
        case .fat: return Color(red: 0.95, green: 0.45, blue: 0.4)
        }
    }

    /// Calories contributed per gram, used for the macro split bar.
    var kcalPerGram: Double {
        self == .fat ? 9 : 4
    }

    func grams(_ n: Nutrients) -> Double {
        switch self {
        case .protein: return n.protein
        case .carbs: return n.carbs
        case .fat: return n.fat
        }
    }
}

/// Single stacked bar showing where the calories come from.
struct MacroSplitBar: View {
    let nutrients: Nutrients

    private var slices: [(macro: Macro, kcal: Double)] {
        Macro.allCases.map { ($0, $0.grams(nutrients) * $0.kcalPerGram) }
    }

    private var totalKcal: Double {
        max(slices.reduce(0) { $0 + $1.kcal }, 0.0001)
    }

    var body: some View {
        VStack(spacing: 10) {
            GeometryReader { geo in
                HStack(spacing: 2) {
                    ForEach(slices, id: \.macro.id) { slice in
                        Capsule()
                            .fill(slice.macro.tint)
                            .frame(width: max(geo.size.width * (slice.kcal / totalKcal) - 2, 0))
                    }
                }
            }
            .frame(height: 10)
            HStack(spacing: 14) {
                ForEach(Macro.allCases) { macro in
                    HStack(spacing: 5) {
                        Circle().fill(macro.tint).frame(width: 7, height: 7)
                        Text(macro.title)
                            .font(.caption)
                            .foregroundStyle(BlastTheme.secondary)
                        Text("\(Int(macro.grams(nutrients).rounded())) g")
                            .font(.caption.weight(.semibold))
                            .foregroundStyle(.white)
                    }
                }
                Spacer(minLength: 0)
            }
        }
    }
}

/// Estimated load vs the vessel's MIN LIQUID and MAX FILL lines.
struct VesselGauge: View {
    let volumeML: Double
    let guide: Guide

    private var fraction: Double {
        min(volumeML / guide.maxFillML, 1.25)
    }

    private var isOver: Bool { volumeML > guide.maxFillML }
    private var isUnderMin: Bool { volumeML > 0 && volumeML < guide.minLiquidML }

    private var tint: Color {
        if isOver { return BlastTheme.red }
        if isUnderMin { return Color(red: 1, green: 0.78, blue: 0.25) }
        return Color(red: 0.3, green: 0.8, blue: 0.5)
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                SectionLabel(text: "Vessel load")
                Spacer()
                Text("\(Int(volumeML.rounded())) / \(Int(guide.maxFillML)) ml")
                    .font(.caption.weight(.semibold))
                    .monospacedDigit()
                    .foregroundStyle(tint)
            }
            GeometryReader { geo in
                ZStack(alignment: .leading) {
                    Capsule()
                        .fill(Color.white.opacity(0.08))
                    Capsule()
                        .fill(tint)
                        .frame(width: min(geo.size.width * fraction, geo.size.width))
                    Rectangle()
                        .fill(Color.white.opacity(0.45))
                        .frame(width: 2)
                        .offset(x: geo.size.width * (guide.minLiquidML / guide.maxFillML))
                }
            }
            .frame(height: 14)
            Text(statusText)
                .font(.footnote)
                .foregroundStyle(isOver ? BlastTheme.red : BlastTheme.secondary)
                .fixedSize(horizontal: false, vertical: true)
        }
    }

    private var statusText: String {
        if isOver {
            return "Over the MAX FILL line for the \(guide.kind.shortName). Split it into two blends."
        }
        if isUnderMin {
            return "Below MIN LIQUID (\(Int(guide.minLiquidML)) ml). Add more liquid or the blades will cavitate."
        }
        if volumeML == 0 {
            return "Add ingredients to see how full the vessel gets. The marker is the MIN LIQUID line."
        }
        return "Fits the \(guide.kind.shortName). Loaded volume is an estimate, so leave a little headroom."
    }
}

struct NutrientRow: View {
    let title: String
    let value: Double
    let unit: String
    let dailyValue: Double?
    var emphasized = false
    var indented = false

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text(title)
                .font(emphasized ? .body.weight(.semibold) : .body)
                .foregroundStyle(emphasized ? .white : Color(white: 0.85))
                .padding(.leading, indented ? 16 : 0)
            Spacer(minLength: 8)
            Text("\(formatted) \(unit)")
                .font(.body.weight(emphasized ? .bold : .regular))
                .monospacedDigit()
                .foregroundStyle(.white)
            if let dailyValue, dailyValue > 0 {
                Text("\(Int((value / dailyValue * 100).rounded()))%")
                    .font(.caption.weight(.semibold))
                    .monospacedDigit()
                    .foregroundStyle(BlastTheme.secondary)
                    .frame(width: 46, alignment: .trailing)
            } else {
                Spacer().frame(width: 46)
            }
        }
        .padding(.vertical, 7)
    }

    private var formatted: String {
        value >= 10 ? "\(Int(value.rounded()))" : String(format: "%.1f", value)
    }
}

struct FoodBadge: View {
    let category: FoodCategory
    var size: CGFloat = 38

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: size / 3.2, style: .continuous)
                .fill(category.tint.opacity(0.2))
            Image(systemName: category.icon)
                .font(.system(size: size * 0.42, weight: .semibold))
                .foregroundStyle(category.tint)
        }
        .frame(width: size, height: size)
    }
}

struct FilterChip: View {
    let title: String
    let isOn: Bool
    var tint: Color = BlastTheme.red
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(isOn ? .white : BlastTheme.secondary)
                .padding(.horizontal, 14)
                .padding(.vertical, 8)
                .background(isOn ? tint : BlastTheme.cardLift, in: Capsule())
        }
        .buttonStyle(.plain)
    }
}
