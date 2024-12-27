//
//  TranscriptView.swift
//  Whispaw
//
//  Created by ebowwa-mac-13inch on 6/17/24.
//

import SwiftUI

struct TranscriptView: View {
    @State private var transcribedText: String = ""
    @State private var isTranscribing: Bool = false
    private var speechTranscriber = SpeechTranscriber()

    var body: some View {
        VStack {
            Text(transcribedText)
                .padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity)

            Button(action: {
                if isTranscribing {
                    speechTranscriber.stopTranscription()
                } else {
                    speechTranscriber.startTranscription()
                }
                isTranscribing.toggle()
            }) {
                Text(isTranscribing ? "Stop Transcription" : "Start Transcription")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
        }
        .onAppear {
            NotificationCenter.default.addObserver(forName: Notification.Name("TranscribedTextUpdated"), object: nil, queue: .main) { notification in
                if let text = notification.userInfo?["text"] as? String {
                    self.transcribedText = text
                }
            }
        }
        .onDisappear {
            NotificationCenter.default.removeObserver(self, name: Notification.Name("TranscribedTextUpdated"), object: nil)
        }
    }
}
