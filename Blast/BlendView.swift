import SwiftUI
import AudioToolbox

@MainActor
final class BlendTimer: ObservableObject {
    let duration: Double = 30
    @Published var remaining: Double = 30
    @Published var isRunning = false
    private var startedAt: Date?
    private var leftover: Double = 30
    private var ticker: Timer?

    var progress: Double {
        1 - (remaining / duration)
    }

    func toggle() {
        if isRunning {
            pause()
        } else {
            start()
        }
    }

    func start() {
        leftover = remaining
        startedAt = Date()
        isRunning = true
        ticker?.invalidate()
        ticker = Timer.scheduledTimer(withTimeInterval: 0.05, repeats: true) { [weak self] _ in
            Task { @MainActor in
                self?.tick()
            }
        }
        RunLoop.main.add(ticker!, forMode: .common)
    }

    func pause() {
        tick()
        leftover = remaining
        isRunning = false
        ticker?.invalidate()
        ticker = nil
        startedAt = nil
    }

    func reset() {
        ticker?.invalidate()
        ticker = nil
        isRunning = false
        startedAt = nil
        leftover = duration
        remaining = duration
    }

    private func tick() {
        guard let startedAt else { return }
        let elapsed = Date().timeIntervalSince(startedAt)
        remaining = max(0, leftover - elapsed)
        if remaining <= 0 {
            remaining = 0
            isRunning = false
            ticker?.invalidate()
            ticker = nil
            self.startedAt = nil
            leftover = duration
            UINotificationFeedbackGenerator().notificationOccurred(.success)
            AudioServicesPlaySystemSound(1005)
        }
    }
}

struct BlendView: View {
    @EnvironmentObject private var store: DeviceStore
    @StateObject private var timer = BlendTimer()

    private var guide: Guide { store.guide }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    timerCard
                    if !guide.programs.isEmpty {
                        programCard
                    }
                    layerCard
                    VStack(alignment: .leading, spacing: 10) {
                        SectionLabel(text: "How to blend")
                        ForEach(guide.blendSteps) { step in
                            StepCard(step: step)
                        }
                    }
                    ForEach(guide.blendWarnings, id: \.self) { text in
                        WarningBanner(text: text)
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Blend")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                DeviceMenuButton()
                ToolbarItem(placement: .topBarLeading) {
                    Button("Reset") { timer.reset() }
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
        }
    }

    private var timerCard: some View {
        Card {
            VStack(spacing: 18) {
                Text(guide.cycleLabel)
                    .font(.caption.weight(.semibold))
                    .tracking(1.1)
                    .foregroundStyle(BlastTheme.secondary)
                ZStack {
                    Circle()
                        .stroke(Color.white.opacity(0.08), lineWidth: 12)
                    Circle()
                        .trim(from: 0, to: timer.progress)
                        .stroke(BlastTheme.red, style: StrokeStyle(lineWidth: 12, lineCap: .round))
                        .rotationEffect(.degrees(-90))
                        .animation(.linear(duration: 0.05), value: timer.remaining)
                    VStack(spacing: 4) {
                        Text(timeLabel)
                            .font(.system(size: 56, weight: .bold, design: .rounded))
                            .monospacedDigit()
                            .foregroundStyle(.white)
                        Text(timer.remaining == 0 ? "Done" : "seconds")
                            .font(.subheadline)
                            .foregroundStyle(BlastTheme.secondary)
                    }
                }
                .frame(width: 220, height: 220)
                .frame(maxWidth: .infinity)

                PrimaryButton(
                    title: buttonTitle,
                    fill: timer.isRunning ? BlastTheme.cardLift : BlastTheme.red,
                    foreground: .white,
                    action: {
                        if timer.remaining == 0 {
                            timer.reset()
                            timer.start()
                        } else {
                            timer.toggle()
                        }
                    }
                )
                Text(guide.timerNote)
                    .font(.footnote)
                    .foregroundStyle(BlastTheme.secondary)
                    .multilineTextAlignment(.center)
                    .frame(maxWidth: .infinity)
            }
        }
    }

    private var programCard: some View {
        Card {
            VStack(alignment: .leading, spacing: 12) {
                SectionLabel(text: "Blend programs")
                ForEach(guide.programs) { program in
                    HStack(alignment: .top, spacing: 12) {
                        ZStack {
                            Circle()
                                .fill(program.tint.opacity(0.2))
                                .frame(width: 40, height: 40)
                            Image(systemName: program.icon)
                                .font(.system(size: 17, weight: .semibold))
                                .foregroundStyle(program.tint)
                        }
                        VStack(alignment: .leading, spacing: 3) {
                            Text(program.name)
                                .font(.subheadline.weight(.bold))
                                .foregroundStyle(.white)
                            Text(program.detail)
                                .font(.footnote)
                                .foregroundStyle(BlastTheme.secondary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                        Spacer(minLength: 0)
                    }
                }
            }
        }
    }

    private var layerCard: some View {
        Card {
            VStack(alignment: .leading, spacing: 12) {
                SectionLabel(text: "Load order")
                ForEach(guide.loadOrder) { layer in
                    loadRow(layer)
                }
                Text(guide.fillNote)
                    .font(.footnote)
                    .foregroundStyle(BlastTheme.secondary)
                    .padding(.top, 4)
            }
        }
    }

    private func loadRow(_ layer: LoadLayer) -> some View {
        HStack {
            RoundedRectangle(cornerRadius: 3, style: .continuous)
                .fill(layer.tint)
                .frame(width: 6, height: 36)
            VStack(alignment: .leading, spacing: 2) {
                Text(layer.title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text(layer.subtitle)
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer()
        }
        .padding(10)
        .background(layer.tint.opacity(0.12), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
    }

    private var timeLabel: String {
        String(format: "%.0f", ceil(timer.remaining))
    }

    private var buttonTitle: String {
        if timer.remaining == 0 { return "Run another 30s" }
        if timer.isRunning { return "Stop" }
        if timer.remaining < timer.duration { return "Resume" }
        return "Start 30s"
    }
}
