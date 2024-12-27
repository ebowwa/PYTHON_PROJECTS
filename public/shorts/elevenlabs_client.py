import os
from elevenlabs import generate, set_api_key

class TextToSpeechAPI:
  def __init__(self, default_voice_id=None):
      try:
          self.api_key = os.getenv('ELEVENLABS_API_KEY')
          if self.api_key is None:
              raise ValueError("Missing 'ELEVENLABS_API_KEY' environment variable")
          set_api_key(self.api_key)
      except Exception as e:
          print(f"An error occurred during API key initialization: {e}")
          return None
      self.default_voice_id = os.getenv('DEFAULT_VOICE_ID') or default_voice_id

  def synthesize(self, text, voice_id=None):
      try:
          voice_id = voice_id or self.default_voice_id
          audio = generate(
              text=text,
              voice=voice_id,
              model="eleven_monolingual_v1"
          )
          return audio
      except Exception as e:
          print(f"An error occurred during synthesis: {e}")
          return None


if __name__ == "__main__":
    try:
        api = TextToSpeechAPI()
        audio_content = api.synthesize("hello, world!")
        with open('output.mp3', 'wb') as f:
            f.write(audio_content)
    except Exception as e:
        print(f"An error occurred: {e}")