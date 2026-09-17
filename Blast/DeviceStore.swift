import SwiftUI

enum DeviceKind: String, CaseIterable, Identifiable {
    case blast
    case blastMax

    var id: String { rawValue }

    var shortName: String {
        switch self {
        case .blast: return "Blast"
        case .blastMax: return "Blast MAX"
        }
    }

    var size: String {
        switch self {
        case .blast: return "16 oz"
        case .blastMax: return "20 oz"
        }
    }
}

@MainActor
final class DeviceStore: ObservableObject {
    private static let key = "blast.selectedDevice"

    @Published var kind: DeviceKind {
        didSet { UserDefaults.standard.set(kind.rawValue, forKey: Self.key) }
    }

    var guide: Guide { GuideBook.guide(for: kind) }

    init() {
        let saved = UserDefaults.standard.string(forKey: Self.key)
        kind = saved.flatMap(DeviceKind.init(rawValue:)) ?? .blast
    }
}

struct DeviceSegmentedPicker: View {
    @EnvironmentObject private var store: DeviceStore

    var body: some View {
        Picker("Device", selection: $store.kind) {
            ForEach(DeviceKind.allCases) { kind in
                Text("\(kind.shortName) · \(kind.size)").tag(kind)
            }
        }
        .pickerStyle(.segmented)
    }
}

struct DeviceMenuButton: ToolbarContent {
    @EnvironmentObject private var store: DeviceStore

    var body: some ToolbarContent {
        ToolbarItem(placement: .topBarTrailing) {
            Menu {
                Picker("Device", selection: $store.kind) {
                    ForEach(DeviceKind.allCases) { kind in
                        Label("\(kind.shortName) · \(kind.size)", systemImage: "cup.and.saucer.fill").tag(kind)
                    }
                }
            } label: {
                HStack(spacing: 4) {
                    Text(store.kind.shortName)
                        .font(.subheadline.weight(.semibold))
                    Image(systemName: "chevron.up.chevron.down")
                        .font(.caption2.weight(.bold))
                }
                .foregroundStyle(BlastTheme.secondary)
            }
        }
    }
}
