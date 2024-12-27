import os
from elevenlabs import generate, Voice, VoiceSettings

# Retrieve voice ID and API key from environment variables
voice_id = os.environ['VOICE_ID']  # Replace 'VOICE_ID' with the name of your environment variable for voice_id
api_key = os.environ['ELEVENLABS_API_KEY']

# Check if environment variables were found
if voice_id is None:
    raise ValueError("Environment variable 'VOICE_ID' is not set. Please check your environment variables.")
if api_key is None:
    raise ValueError("Environment variable 'ELEVENLABS_API_KEY' is not set. Please check your environment variables.")

# Initialize the VoiceSettings model
voice_settings = VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)

# Initialize the Voice model
voice = Voice(voice_id=voice_id, settings=voice_settings)

audio = generate(text="Hello there!", voice=voice)

# Print both variables along with the API Key
print("Voice ID:", voice_id)
print("API Key:", api_key)
print("Audio:", audio)