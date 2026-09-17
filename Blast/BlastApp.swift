import SwiftUI

@main
struct BlastApp: App {
    @StateObject private var store = DeviceStore()
    @StateObject private var builder = BlendBuilder()
    @StateObject private var library = RecipeLibraryStore()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)
                .environmentObject(builder)
                .environmentObject(library)
                .preferredColorScheme(.dark)
        }
    }
}
