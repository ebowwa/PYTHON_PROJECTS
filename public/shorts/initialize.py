import os
import logging
from pulze.api import initialize_openai

def ensure_api_key(key_name, error_message):
    key_value = os.environ.get(key_name)
    if not key_value:
        logging.error(error_message)
        raise ValueError(error_message)
    return key_value

def initialize_api_keys():
    # Ensure API keys are in environment
    ELEVENLABS_API_KEY = ensure_api_key('ELEVENLABS_API_KEY', 'ELEVENLABS_API_KEY not found in environment variables.')
    default_voice_id = ensure_api_key('VOICE_ID', 'DEFAULT_VOICE_ID not found in environment variables.')
    PULZE_API_KEY = ensure_api_key('PULZE_API_KEY', 'PULZE_API_KEY not found in environment variables.')

    # Initialize OpenAI with the PULZE_API_KEY
    initialize_openai(PULZE_API_KEY)


    return ELEVENLABS_API_KEY, default_voice_id, PULZE_API_KEY
