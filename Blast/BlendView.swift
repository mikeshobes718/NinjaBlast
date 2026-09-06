import SwiftUI
import AudioToolbox

@MainActor
final class BlendTimer: ObservableObject {
    let duration: Double = GuideBook.cycleSeconds
    @Published var remaining: Double = GuideBook.cycleSeconds
    @Published var isRunning = false
    private var startedAt: Date?
    private var leftover: Double = GuideBook.cycleSeconds
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
    @StateObject private var timer = BlendTimer()

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    timerCard
                    layerCard
                    VStack(alignment: .leading, spacing: 10) {
                        SectionLabel(text: "How to blend")
                        ForEach(GuideBook.blendSteps) { step in
                            StepCard(step: step)
                        }
                    }
                    WarningBanner(text: "Never run the blender empty. Never blend hot, carbonated, or fizzy liquids. Pressure can pop the lid off.")
                    WarningBanner(text: "Blades are sharp and stay on the motor base. Keep hands, hair, and loose clothing away from the cup.")
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 28)
            }
            .background(BlastTheme.bg.ignoresSafeArea())
            .navigationTitle("Blend")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Reset") { timer.reset() }
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
        }
    }

    private var timerCard: some View {
        Card {
            VStack(spacing: 18) {
                Text("30-SECOND CYCLE")
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
                Text("Matches one press of Start/Stop on the blender. Run another cycle if it is not smooth yet.")
                    .font(.footnote)
                    .foregroundStyle(BlastTheme.secondary)
                    .multilineTextAlignment(.center)
                    .frame(maxWidth: .infinity)
            }
        }
    }

    private var layerCard: some View {
        Card {
            VStack(alignment: .leading, spacing: 12) {
                SectionLabel(text: "Load order")
                layer(title: "Ice / frozen last", subtitle: "Fruit, ice cubes", fill: Color(red: 0.35, green: 0.72, blue: 0.95))
                layer(title: "Fresh / soft", subtitle: "Fruit, greens, yogurt", fill: Color(red: 0.35, green: 0.78, blue: 0.48))
                layer(title: "Liquids first", subtitle: "At least MIN LIQUID · ~177 ml", fill: Color(red: 0.28, green: 0.48, blue: 0.95))
                Text("Never go below MIN LIQUID or above MAX FILL (~400 ml).")
                    .font(.footnote)
                    .foregroundStyle(BlastTheme.secondary)
                    .padding(.top, 4)
            }
        }
    }

    private func layer(title: String, subtitle: String, fill: Color) -> some View {
        HStack {
            RoundedRectangle(cornerRadius: 3, style: .continuous)
                .fill(fill)
                .frame(width: 6, height: 36)
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.white)
                Text(subtitle)
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
            Spacer()
        }
        .padding(10)
        .background(fill.opacity(0.12), in: RoundedRectangle(cornerRadius: 12, style: .continuous))
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
