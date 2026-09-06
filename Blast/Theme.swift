import SwiftUI

enum BlastTheme {
    static let red = Color(red: 0.882, green: 0.024, blue: 0.0)
    static let bg = Color.black
    static let card = Color(white: 0.11)
    static let cardLift = Color(white: 0.16)
    static let hairline = Color.white.opacity(0.08)
    static let secondary = Color(white: 0.62)
    static let radius: CGFloat = 16
}

extension Color {
    static let blastRed = BlastTheme.red
}
