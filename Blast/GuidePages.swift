import SwiftUI

struct GuidePage: View {
    let id: GuideID

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                content
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 28)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle(title)
        .navigationBarTitleDisplayMode(.inline)
    }

    private var title: String {
        GuideBook.topics.first(where: { $0.id == id })?.title ?? "Guide"
    }

    @ViewBuilder
    private var content: some View {
        switch id {
        case .parts:
            parts
        case .battery:
            battery
        case .setup:
            setup
        case .blendHow:
            blendHow
        case .clean:
            clean
        case .storage:
            storage
        case .trouble:
            trouble
        case .warranty:
            warranty
        }
    }

    private var parts: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("Check these before first use.")
                .font(.subheadline)
                .foregroundStyle(BlastTheme.secondary)
            ForEach(Array(GuideBook.parts.enumerated()), id: \.offset) { index, part in
                HStack(alignment: .top, spacing: 12) {
                    Text("\(index + 1)")
                        .font(.caption.weight(.bold))
                        .foregroundStyle(.white)
                        .frame(width: 24, height: 24)
                        .background(BlastTheme.cardLift, in: Circle())
                    Text(part)
                        .font(.body)
                        .foregroundStyle(.white)
                    Spacer(minLength: 0)
                }
                .padding(14)
                .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
            }
            WarningBanner(text: "The BlastBlade assembly is built into the motor base. It is not removable.")
        }
    }

    private var battery: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 10) {
                batteryStat(title: "Ninja claim", value: "15–20", caption: "light, mostly liquid")
                batteryStat(title: "Real world", value: "6–10", caption: "typical mixes")
            }
            Card {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Realistic expectation")
                        .font(.headline)
                        .foregroundStyle(.white)
                    Text("Treat 15–20 blends as a best-case number for thin mixes. Ice and frozen fruit cut that roughly in half. Top up every few uses instead of running it dead.")
                        .font(.body)
                        .foregroundStyle(BlastTheme.secondary)
                    Text("A full charge takes about 2 hours on USB-C at 5V/3A (15W). Yellow LED means charge soon.")
                        .font(.body)
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
            SectionLabel(text: "Make it last")
            bullet("Charge fully (solid green or purple) before first use and whenever it goes yellow.")
            bullet("Do not leave it sitting fully drained for long periods.")
            bullet("Use the included USB-C cable or a proper 5V/3A charger. A bad charger flashes red and blue.")
            bullet("Skip back-to-back cycles when the battery is already low. That shortens lifespan.")
        }
    }

    private func batteryStat(title: String, value: String, caption: String) -> some View {
        Card {
            VStack(alignment: .leading, spacing: 6) {
                Text(title.uppercased())
                    .font(.caption.weight(.semibold))
                    .tracking(0.8)
                    .foregroundStyle(BlastTheme.secondary)
                Text(value)
                    .font(.system(size: 32, weight: .bold, design: .rounded))
                    .foregroundStyle(.white)
                Text(caption)
                    .font(.caption)
                    .foregroundStyle(BlastTheme.secondary)
            }
        }
    }

    private var setup: some View {
        VStack(alignment: .leading, spacing: 10) {
            WarningBanner(text: "Blades are sharp and stay on the motor base. They can still be active with the lid off. Keep hands, hair, and loose clothing away.")
            ForEach(GuideBook.setupSteps) { step in
                StepCard(step: step)
            }
        }
    }

    private var blendHow: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(GuideBook.blendSteps) { step in
                StepCard(step: step)
            }
            WarningBanner(text: "Never run empty. Never blend hot, carbonated, or fizzy liquids.")
        }
    }

    private var clean: some View {
        VStack(alignment: .leading, spacing: 14) {
            SectionLabel(text: "After every use")
            ForEach(GuideBook.quickClean) { step in
                StepCard(step: step)
            }
            SectionLabel(text: "Hand washing")
            bullet("Wash the cup and lid with warm, soapy water.")
            bullet("Use a long-handled brush on the blades. Grip the motor base, never the blades.")
            bullet("Wipe the motor base with a clean, damp cloth only.")
            bullet("Rinse everything and air-dry.")
            SectionLabel(text: "Dishwasher")
            bullet("Cup and lid are top-rack dishwasher safe.")
            bullet("Do not use a heated drying cycle.")
            bullet("Take the cup and lid off the motor base first.")
            WarningBanner(text: "Never submerge the motor base or put it in the dishwasher. After cleaning near the USB-C port, air-dry 30 minutes before charging.")
        }
    }

    private var storage: some View {
        VStack(alignment: .leading, spacing: 10) {
            bullet("Store upright, fully assembled (lid + cup + base).")
            bullet("Don't leave blended or unblended ingredients sitting in the cup.")
            bullet("Don't stack anything on top of the unit.")
        }
    }

    private var trouble: some View {
        VStack(alignment: .leading, spacing: 14) {
            troubleBlock(
                title: "Ingredients keep getting stuck",
                lines: [
                    "Layer correctly: liquid up to MIN LIQUID, then fresh fruit or veg, then greens, then frozen or ice last.",
                    "If it keeps sticking, add a little more liquid.",
                    "Shake while it runs, flip it upside down mid-cycle, then start a new cycle right-side up.",
                ]
            )
            troubleBlock(
                title: "Blades locked / won't spin",
                lines: [
                    "Stay at or above MIN LIQUID and under MAX FILL.",
                    "Turn the unit off. Clear the blades with a long utensil, then restart.",
                ]
            )
            troubleBlock(
                title: "Lid or cup won't seat",
                lines: [
                    "Set the assembled base or cup on a flat surface.",
                    "Line up the threads evenly, then twist clockwise until it seals.",
                    "When seated, the LED glows solid purple or yellow depending on battery.",
                ]
            )
            troubleBlock(
                title: "Control panel won't turn off",
                lines: [
                    "Press the power button to toggle the unit on and off.",
                ]
            )
            Text("Still stuck?")
                .font(.headline)
                .foregroundStyle(.white)
            Text("Call SharkNinja at \(GuideBook.supportDisplay). Have your receipt ready.")
                .font(.subheadline)
                .foregroundStyle(BlastTheme.secondary)
            SupportCallButton()
        }
    }

    private var warranty: some View {
        VStack(alignment: .leading, spacing: 14) {
            Card {
                VStack(alignment: .leading, spacing: 8) {
                    Text("1-year limited warranty")
                        .font(.headline)
                        .foregroundStyle(.white)
                    Text("Valid only for the original purchaser and non-transferable. Covers manufacturing defects under normal home use.")
                        .font(.body)
                        .foregroundStyle(BlastTheme.secondary)
                }
            }
            SectionLabel(text: "Not covered")
            bullet("Normal wear on cups, blades, lids, or bases.")
            bullet("Units altered or used commercially.")
            bullet("Damage from misuse, negligence, or lack of maintenance.")
            bullet("Incidental or consequential damage.")
            bullet("Damage from unauthorized repairs.")
            SupportCallButton()
        }
    }

    private func troubleBlock(title: String, lines: [String]) -> some View {
        Card {
            VStack(alignment: .leading, spacing: 8) {
                Text(title)
                    .font(.headline)
                    .foregroundStyle(.white)
                ForEach(lines, id: \.self) { line in
                    HStack(alignment: .top, spacing: 8) {
                        Text("·")
                            .foregroundStyle(BlastTheme.red)
                        Text(line)
                            .font(.subheadline)
                            .foregroundStyle(BlastTheme.secondary)
                    }
                }
            }
        }
    }

    private func bullet(_ text: String) -> some View {
        HStack(alignment: .top, spacing: 10) {
            Circle()
                .fill(BlastTheme.red)
                .frame(width: 6, height: 6)
                .padding(.top, 8)
            Text(text)
                .font(.body)
                .foregroundStyle(.white)
            Spacer(minLength: 0)
        }
        .padding(14)
        .background(BlastTheme.card, in: RoundedRectangle(cornerRadius: 14, style: .continuous))
    }
}
