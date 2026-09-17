import SwiftUI

@main
struct BlastApp: App {
    @StateObject private var store = DeviceStore()
    @StateObject private var builder = BlendBuilder()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)
                .environmentObject(builder)
                .preferredColorScheme(.dark)
        }
    }
}
