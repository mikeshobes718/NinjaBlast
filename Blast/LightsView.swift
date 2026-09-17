import SwiftUI

struct LightsView: View {
    @EnvironmentObject private var store: DeviceStore

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    Text("Match the light on the motor base to a row. Colors tell you what to do next.")
                        .font(.subheadline)
                        .foregroundStyle(BlastTheme.secondary)
                    ForEach(store.guide.leds) { led in
                        LEDRow(status: led)
                    }
                    if let note = store.guide.ledNote {
                        Card {
                            HStack(alignment: .top, spacing: 10) {
                                Image(systemName: "info.circle.fill")
                                    .foregroundStyle(BlastTheme.secondary)
                                Text(note)
                                    .font(.footnote)
                                    .foregroundStyle(BlastTheme.secondary)
                                    .fixedSize(horizontal: false, vertical: true)
                            }
                        }
                    }
                    SupportCallButton()
                        .padding(.top, 8)
                    Text("Have your receipt ready if you need a warranty claim.")
                        .font(.footnote)
                        .foregroundStyle(BlastTheme.secondary)
                        .frame(maxWidth: .infinity, alignment: .center)
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Lights")
            .navigationBarTitleDisplayMode(.large)
            .toolbar { DeviceMenuButton() }
        }
    }
}

struct LEDRow: View {
    let status: LEDStatus

    var body: some View {
        HStack(alignment: .top, spacing: 14) {
            LEDSwatch(status: status)
            VStack(alignment: .leading, spacing: 6) {
                Text(status.title)
                    .font(.body.weight(.semibold))
                    .foregroundStyle(.white)
                Text(status.meaning)
                    .font(.subheadline)
                    .foregroundStyle(.white.opacity(0.9))
                Text(status.action)
                    .font(.subheadline)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer(minLength: 0)
        }
        .padding(14)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
    }
}

struct LEDSwatch: View {
    let status: LEDStatus

    var body: some View {
        TimelineView(.animation(minimumInterval: 0.35, paused: false)) { context in
            let t = context.date.timeIntervalSinceReferenceDate
            let on = Int(t * 2) % 2 == 0
            ZStack {
                Circle()
                    .fill(Color.white.opacity(0.06))
                    .frame(width: 44, height: 44)
                Circle()
                    .fill(swatchColor(on: on))
                    .frame(width: 22, height: 22)
                    .opacity(opacity(on: on))
                    .shadow(color: swatchColor(on: on).opacity(0.8), radius: 8)
            }
        }
    }

    private func swatchColor(on: Bool) -> Color {
        switch status.pulse {
        case .solid:
            return status.colorA
        case .flash:
            return status.colorA
        case .pair:
            return on ? status.colorA : (status.colorB ?? status.colorA)
        case .chase:
            return status.colorA
        }
    }

    private func opacity(on: Bool) -> Double {
        switch status.pulse {
        case .solid:
            return 1
        case .flash, .chase:
            return on ? 1 : 0.18
        case .pair:
            return 1
        }
    }
}
