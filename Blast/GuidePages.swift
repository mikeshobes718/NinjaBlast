import SwiftUI

struct GuidePage: View {
    let id: GuideID
    let guide: Guide

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                content
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 28)
        }
        .background(BlastTheme.bg.ignoresSafeArea())
        .navigationTitle(guide.topic(id)?.title ?? "Guide")
        .navigationBarTitleDisplayMode(.inline)
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
        case .programs:
            programs
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
            ForEach(Array(guide.parts.enumerated()), id: \.offset) { index, part in
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
            WarningBanner(text: guide.partsNote)
        }
    }

    private var battery: some View {
        VStack(alignment: .leading, spacing: 14) {
            if let claim = guide.battery.claim, let real = guide.battery.real {
                HStack(spacing: 10) {
                    batteryStat(title: "Ninja claim", value: claim, caption: guide.battery.claimCaption)
                    batteryStat(title: "Real world", value: real, caption: guide.battery.realCaption)
                }
            }
            Card {
                VStack(alignment: .leading, spacing: 8) {
                    Text(guide.battery.headline)
                        .font(.headline)
                        .foregroundStyle(.white)
                    ForEach(guide.battery.body, id: \.self) { line in
                        Text(line)
                            .font(.body)
                            .foregroundStyle(BlastTheme.secondary)
                    }
                }
            }
            SectionLabel(text: "Make it last")
            ForEach(guide.battery.tips, id: \.self) { tip in
                bullet(tip)
            }
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
            ForEach(guide.setupSteps) { step in
                StepCard(step: step)
            }
        }
    }

    private var blendHow: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(guide.blendSteps) { step in
                StepCard(step: step)
            }
            ForEach(guide.blendWarnings, id: \.self) { text in
                WarningBanner(text: text)
            }
        }
    }

    private var programs: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("The dial has the program buttons above and below the power button.")
                .font(.subheadline)
                .foregroundStyle(BlastTheme.secondary)
            ProgramDial()
                .frame(maxWidth: .infinity)
                .padding(.vertical, 8)
            ForEach(guide.programs) { program in
                Card {
                    HStack(alignment: .top, spacing: 14) {
                        ZStack {
                            Circle()
                                .fill(program.tint.opacity(0.2))
                                .frame(width: 44, height: 44)
                            Image(systemName: program.icon)
                                .font(.title3.weight(.semibold))
                                .foregroundStyle(program.tint)
                        }
                        VStack(alignment: .leading, spacing: 4) {
                            Text(program.name)
                                .font(.headline)
                                .foregroundStyle(.white)
                            Text(program.detail)
                                .font(.subheadline)
                                .foregroundStyle(BlastTheme.secondary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                        Spacer(minLength: 0)
                    }
                }
            }
            WarningBanner(text: "Stop the blend mode at any time by pressing the program button again.")
        }
    }

    private var clean: some View {
        VStack(alignment: .leading, spacing: 14) {
            SectionLabel(text: "Quick clean")
            ForEach(guide.quickClean) { step in
                StepCard(step: step)
            }
            SectionLabel(text: "Hand washing")
            ForEach(guide.handWash, id: \.self) { line in
                bullet(line)
            }
            SectionLabel(text: "Dishwasher")
            ForEach(guide.dishwasher, id: \.self) { line in
                bullet(line)
            }
            WarningBanner(text: guide.cleanWarning)
        }
    }

    private var storage: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(guide.storage, id: \.self) { line in
                bullet(line)
            }
        }
    }

    private var trouble: some View {
        VStack(alignment: .leading, spacing: 14) {
            ForEach(guide.troubles) { block in
                troubleBlock(title: block.title, lines: block.lines)
            }
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
