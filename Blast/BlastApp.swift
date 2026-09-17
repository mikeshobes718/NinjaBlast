import SwiftUI

@main
struct BlastApp: App {
    @StateObject private var store = DeviceStore()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)
                .preferredColorScheme(.dark)
        }
    }
}
