import SwiftUI

@main
struct WhispawApp: App {
    @StateObject private var bluetoothService = BluetoothService()
    @StateObject private var deviceModel = DeviceModel.shared

    var body: some Scene {
        WindowGroup {
            if bluetoothService.isScanning {
                SplashScene()
                    .environmentObject(deviceModel)
            } else {
                if deviceModel.isConnected {
                    ConnectedDeviceView()
                        .environmentObject(deviceModel)
                }
            }
        }
    }
}

struct SplashScene: View {
    var body: some View {
        SplashView()
        // Splash view is an initial verification that device is connected.
        // If connected, it should transition to the main content scene.
        // If not connected, it should stay here and potentially redirect the user to buy a collar or troubleshoot the connection.
    }
}

struct OnboardingScene: View {
    var body: some View {
        TutorialView()
        // TutorialView should start a tutorial only if new user.
        // Tutorial ending in UserSignUpView().
    }
}

