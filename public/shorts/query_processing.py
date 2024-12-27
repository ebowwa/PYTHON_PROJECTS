import logging
import os
from pulze.api import initialize, complete_text
from elevenlabs_client import TextToSpeechAPI
from initialize import initialize_api_keys


def process_query():
    # Get the API keys
    ELEVENLABS_API_KEY, default_voice_id, PULZE_API_KEY = initialize_api_keys()
    logging.info('API keys have been initialized.')
    print('API keys have been initialized.')

    # Ask the user for a query
    user_query = input("What video concept are you interested in? ")
    logging.info(f'User query received: {user_query}')
    print(f'User query received: {user_query}')

    # Initialize pulze API
    initialize(PULZE_API_KEY)
    logging.info('Pulze API has been initialized.')
    print('Pulze API has been initialized.')

    # Generate pitch text using Pulze API
    pitch_text = complete_text(f"Create a 30 second pitch for a video concept on {user_query}. Output the script: ")
    logging.info('Pitch text has been generated.')
    print('Pitch text has been generated.')

    # Get VOICE_ID from environment variables and initialize TextToSpeechAPI from elevenlabs
    VOICE_ID = os.environ.get('VOICE_ID')
    tts_api = TextToSpeechAPI(VOICE_ID)
    logging.info('TextToSpeechAPI has been initialized.')
    print('TextToSpeechAPI has been initialized.')
    print(pitch_text)  # before line 5 in audio_generation.py
    print(tts_api)  # before line 6 in audio_generation.py

    if tts_api is None or pitch_text is None:
        logging.error('Error in processing the query.')
        print('Error in processing the query.')
        return 

    # Return tts_api, pitch_text, and user_query for further usage
    return tts_api, pitch_text, user_query