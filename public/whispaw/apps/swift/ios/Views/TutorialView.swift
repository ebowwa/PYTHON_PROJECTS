//
//  TutorialView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/16/24.
//
// lets get started, verify connected device, add context to connected device(s) and pet(s){general attitude, name, image, personality, pet type(s)}, how to use the app/service, invite friends
import SwiftUI

struct TutorialView: View {
    @State private var isActive = false

    var body: some View {
        NavigationStack {
            VStack {
                Text("Hey Pet Parent!")
                    .font(.largeTitle)
                    .padding()

                NavigationLink(value: "SignUp") {
                    EmptyView()
                }
                .hidden()
            }
            .onAppear {
                DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                    self.isActive = true
                }
            }
            .navigationDestination(isPresented: $isActive) {
                SignUpView()
            }
        }
    }
}

#Preview {
    TutorialView()
}
