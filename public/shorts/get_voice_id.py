import requests
import os
import json

def get_voice_id():
    url = "https://api.elevenlabs.io/v1/voices"

    headers = {
        "Accept": "application/json",
        "xi-api-key": os.environ.get("ELEVEN_LABS_API_KEY")  # Retrieve API key from environment variable
    }

    response = requests.get(url, headers=headers)

    # Parse the JSON response
    data = response.json()

    # List to store the voice ids
    voice_ids = [] 

    # Checking if Voices is in data
    if 'voices' in data:
        voices = data['voices']
        for voice in voices:
            # Only process voices that have a category of "cloned"
            if voice['category'] == 'cloned':
                try:
                    print("Voice ID: ", voice['voice_id'])
                    print("Name: ", voice['name'])
                    print("Category: ", voice['category'])
                    voice_ids.append(voice['voice_id'])  # Append voice id to list
                    # Check if settings are not None
                    if voice['settings']:
                        print("Settings: ", voice['settings'])
                    else:
                        print("No settings for this voice.")
                except Exception as e:
                    print(f"An error occurred while processing voice properties: {e}")
    else:
        print("Voices not found in data.")

    return voice_ids # Returns a list of voice ids

if __name__ == "__main__":
    voice_ids = get_voice_id()
    print(voice_ids)  # print returned voice_ids when running this file