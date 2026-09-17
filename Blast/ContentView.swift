import SwiftUI

struct ContentView: View {
    @State private var tab = ContentView.launchTab()

    var body: some View {
        TabView(selection: $tab) {
            HomeView()
                .tabItem { Label("Guide", systemImage: "house.fill") }
                .tag(0)
            BlendView()
                .tabItem { Label("Blend", systemImage: "timer") }
                .tag(1)
            RecipesView()
                .tabItem { Label("Recipes", systemImage: "book.fill") }
                .tag(2)
            CounterView()
                .tabItem { Label("Counter", systemImage: "flame.fill") }
                .tag(3)
            LightsView()
                .tabItem { Label("Lights", systemImage: "light.max") }
                .tag(4)
        }
        .tint(BlastTheme.red)
        .background(BlastTheme.bg.ignoresSafeArea())
    }

    private static func launchTab() -> Int {
        UserDefaults.standard.integer(forKey: "blast.screenshotTab")
    }
}

#Preview {
    ContentView()
        .environmentObject(DeviceStore())
        .preferredColorScheme(.dark)
}
