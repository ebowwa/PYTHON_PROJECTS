'use client';

import { useState, useEffect } from 'react';
import TTS from '@/components/utility/audio/TTS';
import RecordingControls from '@/components/utility/audio/RecordingControls';
import '@/styles/Speaker.css';
import { translateAudio, generateResponse } from '../(actions)/speech/action';

const SILENCE_THRESHOLD = 50; // Adjust this value to set the silence threshold
const SILENCE_DURATION = 3000; // 3 seconds of silence

export default function Speaker() {
  const [isListening, setIsListening] = useState(false);
  const [status, setStatus] = useState('Waiting for audio...');
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [silenceTimer, setSilenceTimer] = useState<ReturnType<typeof setTimeout> | null>(null);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const [audioChunks, setAudioChunks] = useState<Blob[]>([]);
  const [messages, setMessages] = useState<{ role: 'user' | 'assistant'; content: string }[]>([]);

  useEffect(() => {
    updateButtonText();
  }, [isListening]);

  function updateButtonText() {
    return isListening ? '🔇 Disable Microphone' : '🎤 Enable Microphone';
  }

  function startVisualization() {
    // Add code to start the visualization
  }

  function stopVisualization() {
    // Add code to stop the visualization
  }

  async function startListening() {
    setStatus('Listening...');
    startVisualization();

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const newMediaRecorder = new MediaRecorder(stream);
      setMediaRecorder(newMediaRecorder);

      newMediaRecorder.addEventListener('dataavailable', (event) => {
        setAudioChunks((prevChunks) => [...prevChunks, event.data]);
        handleAudioData(event.data);
      });

      newMediaRecorder.addEventListener('stop', async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const { text } = await translateAudio(audioBlob, 'whisper-large-v3');
        setMessages((prevMessages) => [
        ...prevMessages,
        { role: 'user', content: text },
        ]);
        const response = await generateResponse(text, 'llama3-8b-8192');
        setMessages((prevMessages) => [
          ...prevMessages,
          { role: 'assistant', content: response.content },
        ]);
        setAudioChunks([]);
      });

      newMediaRecorder.start();
    } catch (error) {
      console.error('Error starting audio recording:', error);
      setStatus('Error starting audio recording');
    }
  }

  function stopListening() {
    setStatus('Waiting for audio...');
    stopVisualization();
    clearSilenceTimer();
    mediaRecorder?.stop();
    setIsListening(false);
  }

  const handleMicButtonClick = () => {
    setIsListening((prevState) => !prevState);

    if (isListening) {
      stopListening();
    } else {
      startListening();
    }
  };

  const handleAudioData = async (data: Blob) => {
    const audioLevel = await getAudioLevel(data);
    if (audioLevel < SILENCE_THRESHOLD) {
      if (!silenceTimer) {
        setSilenceTimer(
          setTimeout(() => {
            // Do not stop listening, just reset the silence timer
            setSilenceTimer(null);
          }, SILENCE_DURATION)
        );
      }
    } else {
      clearSilenceTimer();
    }
  };

  const clearSilenceTimer = () => {
    if (silenceTimer) {
      clearTimeout(silenceTimer);
      setSilenceTimer(null);
    }
  };

  const getAudioLevel = async (data: Blob): Promise<number> => {
    const audioContext = new AudioContext();
    const arrayBuffer = await data.arrayBuffer();
    const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
    const channelData = audioBuffer.getChannelData(0);
    const rms = Math.sqrt(
      channelData.reduce((sum, value) => sum + value * value, 0) / channelData.length
    );
    return rms * 100;
  };

  return (
    <div className="container">
      <h1>Voice-to-Voice Conversation</h1>
      <div className="messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.role}`}>
            {message.role === 'user' ? 'User: ' : 'Assistant: '}
            {message.content}
          </div>
        ))}
      </div>
      <button id="mic-button" onClick={handleMicButtonClick}>
        <span>{updateButtonText()}</span>
      </button>
      <div id="visualization">
        <div className="pulse"></div>
        <div className="mic-icon">🎤</div>
      </div>
      <div id="status">{status}</div>
    </div>
  );
}