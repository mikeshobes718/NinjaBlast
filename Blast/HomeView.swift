import SwiftUI

struct HomeView: View {
    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    deviceCard
                    specGrid
                    quickActions
                    guideList
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Blast")
            .navigationBarTitleDisplayMode(.large)
            .navigationDestination(for: GuideID.self) { id in
                GuidePage(id: id)
            }
        }
    }

    private var deviceCard: some View {
        HStack(alignment: .center, spacing: 16) {
            BlenderMark()
            VStack(alignment: .leading, spacing: 6) {
                Text("NINJA BLAST")
                    .font(.caption.weight(.semibold))
                    .tracking(1.2)
                    .foregroundStyle(BlastTheme.secondary)
                Text("Portable blender")
                    .font(.title2.weight(.bold))
                    .foregroundStyle(.white)
                Text("Series \(GuideBook.model) · 470 ml")
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
                Text("READY TO BLEND")
                    .font(.caption.weight(.semibold))
                    .tracking(0.6)
                    .foregroundStyle(Color(red: 0.45, green: 0.85, blue: 0.5))
                    .padding(.top, 4)
            }
            Spacer(minLength: 0)
        }
        .padding(18)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 20, style: .continuous))
    }

    private var specGrid: some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: "At a glance")
            LazyVGrid(columns: [GridItem(.flexible(), spacing: 10), GridItem(.flexible(), spacing: 10)], spacing: 10) {
                ForEach(GuideBook.specs) { item in
                    SpecTile(item: item)
                }
            }
        }
    }

    private var quickActions: some View {
        VStack(alignment: .leading, spacing: 10) {
            SectionLabel(text: "Quick actions")
            HStack(spacing: 10) {
                NavigationLink(value: GuideID.blendHow) {
                    quickTile(icon: "play.circle.fill", title: "How to blend")
                }
                NavigationLink(value: GuideID.clean) {
                    quickTile(icon: "drop.fill", title: "Quick clean")
                }
                NavigationLink(value: GuideID.battery) {
                    quickTile(icon: "battery.50", title: "Battery")
                }
            }
            .buttonStyle(.plain)
        }
    }

    private func quickTile(icon: String, title: String) -> some View {
        VStack(spacing: 10) {
            Image(systemName: icon)
                .font(.title2)
                .foregroundStyle(BlastTheme.red)
            Text(title)
                .font(.caption.weight(.semibold))
                .foregroundStyle(.white)
                .multilineTextAlignment(.center)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 16)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
    }

    private var guideList: some View {
        VStack(alignment: .leading, spacing: 4) {
            SectionLabel(text: "Owner's guide")
                .padding(.bottom, 8)
            ForEach(GuideBook.topics) { topic in
                NavigationLink(value: topic.id) {
                    GuideRow(topic: topic)
                }
                .buttonStyle(.plain)
                if topic.id != GuideBook.topics.last?.id {
                    Divider().overlay(BlastTheme.hairline)
                }
            }
        }
    }
}
