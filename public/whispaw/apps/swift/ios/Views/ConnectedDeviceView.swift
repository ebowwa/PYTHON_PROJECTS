//
//  ConnectedDeviceView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/18/24.
//
import SwiftUI

struct ConnectedDeviceView: View {
    @EnvironmentObject var deviceModel: DeviceModel
    
    var body: some View {
        ZStack {
            BackgroundGradientView()
            VStack {
                DeviceCardView(batteryLevel: deviceModel.batteryLevel > 0 ? deviceModel.batteryLevel : nil)
            }
        }
    }
}

struct ConnectedDeviceView_Previews: PreviewProvider {
    static var previews: some View {
        ConnectedDeviceView()
            .environmentObject(DeviceModel.shared)
    }
}
