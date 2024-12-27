# Swift Navigation

1. **Using NavigationView and NavigationLink**:
   - If you want to navigate to different views in a more structured way, you can use `NavigationView` and `NavigationLink`.

   ```swift
   import SwiftUI

   @main
   struct WhispawApp: App {
       @StateObject private var bluetoothService = BluetoothService()
       @State private var user: User? = User.load()

       var body: some Scene {
           WindowGroup {
               NavigationView {
                   if bluetoothService.isScanning {
                       SplashView()
                   } else {
                       if let user = user {
                           if user.isLoggedIn {
                               DashboardView()
                           } else {
                               TranscriptView()
                           }
                       } else {
                           TutorialView()
                       }
                   }
               }
           }
       }
   }
   ```

2. **Using TabView for Dashboard**:
   - If your `DashboardView` contains multiple tabs, you can use `TabView`.

   ```swift
   struct DashboardView: View {
       var body: some View {
           TabView {
               UserHomeView()
                   .tabItem {
                       Label("Home", systemImage: "house")
                   }
               SettingsView()
                   .tabItem {
                       Label("Settings", systemImage: "gear")
                   }
           }
       }
   }
   ```

3. **Using Sheets for Modal Views**:
   - If you want to present a view modally (like a sign-in view), you can use `.sheet`.

   ```swift
   struct TranscriptView: View {
       @State private var showingSignIn = false

       var body: some View {
           VStack {
               Text("Transcript View")
               Button(action: {
                   showingSignIn = true
               }) {
                   Text("Sign In")
               }
               .sheet(isPresented: $showingSignIn) {
                   SignInView()
               }
           }
       }
   }
   ```

4. **Using EnvironmentObject for Shared Data**:
   - If you need to share data across views, you can use `@EnvironmentObject`.

   ```swift
   class UserSettings: ObservableObject {
       @Published var isLoggedIn = false
   }

   @main
   struct WhispawApp: App {
       @StateObject private var bluetoothService = BluetoothService()
       @State private var user: User? = User.load()
       @StateObject private var userSettings = UserSettings()

       var body: some Scene {
           WindowGroup {
               NavigationView {
                   if bluetoothService.isScanning {
                       SplashView()
                   } else {
                       if let user = user {
                           if user.isLoggedIn {
                               DashboardView()
                           } else {
                               TranscriptView()
                           }
                       } else {
                           TutorialView()
                       }
                   }
               }
               .environmentObject(userSettings)
           }
       }
   }
   ```

5. **Using NavigationLinks for Deep Linking**:
   - If you want to navigate to specific views based on user actions, you can use `NavigationLink`.

   ```swift
   struct TutorialView: View {
       var body: some View {
           VStack {
               Text("Tutorial View")
               NavigationLink(destination: UserSignUpView()) {
                   Text("Finish Tutorial")
               }
           }
       }
   }
   ```

These modifications can help you structure your app's navigation more effectively and provide a better user experience.

# the concepts of `NavigationView`, `NavigationLink`, and `Sheet` in SwiftUI:

### NavigationView and NavigationLink

**NavigationView** is a container view that provides a navigation stack, allowing you to create hierarchical navigation in your app. It is used to manage the navigation between views and to display a navigation bar at the top of the screen.

**NavigationLink** is a view that controls the navigation presentation of a destination view. When a `NavigationLink` is activated (e.g., by tapping on it), it pushes the destination view onto the navigation stack.

Here's a simple example:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink(destination: DetailView()) {
                    Text("Go to Detail View")
                }
            }
            .navigationTitle("Home")
        }
    }
}

struct DetailView: View {
    var body: some View {
        Text("This is the Detail View")
            .navigationTitle("Detail")
    }
}
```

In this example:
- `NavigationView` wraps the `VStack` containing the `NavigationLink`.
- When the user taps the "Go to Detail View" text, the `DetailView` is pushed onto the navigation stack, and the user is taken to the detail view.

### Sheet

**Sheet** is a modal presentation style in SwiftUI that allows you to present a new view modally over the current view. Sheets are often used for temporary interactions that do not require full-screen navigation, such as displaying settings, sign-in forms, or alerts.

To present a sheet, you use the `.sheet` modifier on a view, and you typically use a `@State` variable to control the presentation.

Here's an example:

```swift
import SwiftUI

struct ContentView: View {
    @State private var showingSheet = false

    var body: some View {
        VStack {
            Button(action: {
                showingSheet = true
            }) {
                Text("Show Sheet")
            }
        }
        .sheet(isPresented: $showingSheet) {
            SheetView()
        }
    }
}

struct SheetView: View {
    var body: some View {
        Text("This is a sheet")
    }
}
```

In this example:
- The `@State` variable `showingSheet` is used to control the presentation of the sheet.
- When the user taps the "Show Sheet" button, the `showingSheet` state is set to `true`, which triggers the presentation of the `SheetView`.
- The `.sheet` modifier is used to present `SheetView` modally when `showingSheet` is `true`.

### Combining NavigationView, NavigationLink, and Sheet

You can combine these concepts to create more complex navigation flows. For example, you can use `NavigationLink` to navigate to a new view and then present a sheet from that view.

Here's an example:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink(destination: DetailView()) {
                    Text("Go to Detail View")
                }
            }
            .navigationTitle("Home")
        }
    }
}

struct DetailView: View {
    @State private var showingSheet = false

    var body: some View {
        VStack {
            Button(action: {
                showingSheet = true
            }) {
                Text("Show Sheet")
            }
        }
        .navigationTitle("Detail")
        .sheet(isPresented: $showingSheet) {
            SheetView()
        }
    }
}

struct SheetView: View {
    var body: some View {
        Text("This is a sheet")
    }
}
```

In this example:
- The `NavigationLink` in `ContentView` navigates to `DetailView`.
- From `DetailView`, the user can tap a button to present `SheetView` modally using the `.sheet` modifier.

These tools provide powerful ways to manage navigation and modal presentations in your SwiftUI app.
