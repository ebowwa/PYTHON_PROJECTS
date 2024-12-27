//
//  DeviceView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/18/24.
//

import SwiftUI

struct DeviceView: View {
    var body: some View {
        ZStack {
            AdaptiveBackgroundView()
            DeviceContentContainerView()
        }
    }
}

struct DeviceView_Previews: PreviewProvider {
    static var previews: some View {
        DeviceView()
    }
}
