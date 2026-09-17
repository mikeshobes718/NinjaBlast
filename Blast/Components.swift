import SwiftUI

struct SectionLabel: View {
    let text: String

    var body: some View {
        Text(text.uppercased())
            .font(.caption.weight(.semibold))
            .tracking(1.1)
            .foregroundStyle(BlastTheme.secondary)
            .frame(maxWidth: .infinity, alignment: .leading)
    }
}

struct Card<Content: View>: View {
    var padding: CGFloat = 16
    @ViewBuilder var content: () -> Content

    var body: some View {
        content()
            .padding(padding)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: BlastTheme.radius, style: .continuous))
    }
}

struct PrimaryButton: View {
    let title: String
    var fill: Color = BlastTheme.red
    var foreground: Color = .white
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(.headline)
                .foregroundStyle(foreground)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 16)
                .background(fill, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
        }
        .buttonStyle(.plain)
    }
}

struct WarningBanner: View {
    let text: String

    var body: some View {
        HStack(alignment: .top, spacing: 12) {
            Image(systemName: "exclamationmark.circle.fill")
                .foregroundStyle(BlastTheme.red)
                .font(.title3)
            Text(text)
                .font(.subheadline)
                .foregroundStyle(.white)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(14)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(BlastTheme.red.opacity(0.16), in: RoundedRectangle(cornerRadius: 14, style: .continuous))
        .overlay(
            RoundedRectangle(cornerRadius: 14, style: .continuous)
                .stroke(BlastTheme.red.opacity(0.35), lineWidth: 1)
        )
    }
}

struct GuideRow: View {
    let topic: GuideTopic

    var body: some View {
        HStack(spacing: 14) {
            ZStack {
                RoundedRectangle(cornerRadius: 10, style: .continuous)
                    .fill(topic.tint.opacity(0.22))
                    .frame(width: 52, height: 52)
                Image(systemName: topic.icon)
                    .font(.title3.weight(.semibold))
                    .foregroundStyle(topic.tint)
            }
            VStack(alignment: .leading, spacing: 3) {
                Text(topic.title)
                    .font(.body.weight(.semibold))
                    .foregroundStyle(.white)
                Text(topic.subtitle)
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
                    .lineLimit(2)
            }
            Spacer(minLength: 8)
            Image(systemName: "chevron.right")
                .font(.footnote.weight(.semibold))
                .foregroundStyle(Color.white.opacity(0.28))
        }
        .padding(.vertical, 4)
        .contentShape(Rectangle())
    }
}

struct StepCard: View {
    let step: BlendStep

    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            Text("\(step.id)")
                .font(.subheadline.weight(.bold))
                .foregroundStyle(.white)
                .frame(width: 28, height: 28)
                .background(BlastTheme.red, in: Circle())
            Text(step.text)
                .font(.body)
                .foregroundStyle(.white.opacity(0.92))
                .fixedSize(horizontal: false, vertical: true)
            Spacer(minLength: 0)
        }
        .padding(16)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: BlastTheme.radius, style: .continuous))
    }
}

struct SpecTile: View {
    let item: SpecItem

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Image(systemName: item.icon)
                .font(.title3)
                .foregroundStyle(.white)
            Text(item.title)
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(.white)
            Text(item.value)
                .font(.footnote)
                .foregroundStyle(BlastTheme.secondary)
        }
        .padding(14)
        .frame(maxWidth: .infinity, minHeight: 108, alignment: .topLeading)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
    }
}

struct BlenderMark: View {
    var tall: Bool = false

    var body: some View {
        VStack(spacing: 0) {
            Capsule()
                .fill(Color.white.opacity(0.9))
                .frame(width: 36, height: 10)
                .offset(y: 6)
            RoundedRectangle(cornerRadius: 6, style: .continuous)
                .fill(
                    LinearGradient(
                        colors: [Color.white.opacity(0.22), Color.white.opacity(0.06)],
                        startPoint: .top,
                        endPoint: .bottom
                    )
                )
                .overlay(
                    RoundedRectangle(cornerRadius: 6, style: .continuous)
                        .stroke(Color.white.opacity(0.35), lineWidth: 1.5)
                )
                .frame(width: 54, height: tall ? 84 : 72)
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .fill(BlastTheme.red)
                .frame(width: 62, height: 28)
                .overlay(alignment: .top) {
                    Circle()
                        .fill(Color(red: 0.55, green: 0.3, blue: 0.95))
                        .frame(width: 8, height: 8)
                        .offset(y: 6)
                }
        }
        .frame(width: 72, height: 132, alignment: .bottom)
    }
}

struct ProgramDial: View {
    var body: some View {
        ZStack {
            Circle()
                .fill(BlastTheme.cardLift)
                .frame(width: 148, height: 148)
            Circle()
                .stroke(Color.white.opacity(0.12), lineWidth: 1)
                .frame(width: 148, height: 148)
            VStack(spacing: 10) {
                Text("Blend")
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(.white.opacity(0.9))
                Capsule()
                    .fill(Color.white.opacity(0.5))
                    .frame(width: 3, height: 14)
                Image(systemName: "power")
                    .font(.system(size: 22, weight: .semibold))
                    .foregroundStyle(Color(red: 0.2, green: 0.85, blue: 0.4))
                Capsule()
                    .fill(Color.white.opacity(0.5))
                    .frame(width: 3, height: 14)
                Text("Crush")
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(.white.opacity(0.9))
            }
        }
    }
}

struct SupportCallButton: View {
    var body: some View {
        if let url = URL(string: GuideBook.supportTel) {
            Link(destination: url) {
                HStack {
                    Image(systemName: "phone.fill")
                    Text("Call \(GuideBook.supportDisplay)")
                        .fontWeight(.semibold)
                }
                .font(.headline)
                .foregroundStyle(.white)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 16)
                .background(BlastTheme.red, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
            }
        }
    }
}
