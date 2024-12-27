//
//  SignUpView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/17/24.
//
import SwiftUI

struct SignUpView: View {
    @State private var username: String = ""
    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        VStack {
            SignUpForm(username: $username, email: $email, password: $password)

            Button(action: {
                // Create a new user and save it
                var newUser = User(username: username, email: email)
                newUser.login()
            }) {
                Text("Sign Up")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
            .padding()
        }
        .padding()
    }
}

#Preview {
    SignUpView()
}
