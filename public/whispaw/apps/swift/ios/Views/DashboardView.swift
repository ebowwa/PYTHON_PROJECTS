//
//  DashboardView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/18/24.
//

import SwiftUI

struct DashboardView: View {
    @EnvironmentObject var deviceModel: DeviceModel
    @StateObject private var bluetoothService = BluetoothService()

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            HeaderView()
            ScrollView {
                VStack(spacing: 16) {
                    PetInfoView(deviceModel: deviceModel)
                        .onAppear {
                            deviceModel.connect()
                        }
                        .onDisappear {
                            deviceModel.disconnect()
                        }
                    ActivityHistoryView()
                    SettingsView()
                }
                .padding()
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(UIColor.systemGray6))
    }
}

#Preview {
    DashboardView()
        .environmentObject(DeviceModel.shared)
}
