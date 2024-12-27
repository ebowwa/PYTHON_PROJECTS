import logging
import os

def generate_audio_and_save(tts_api, pitch_text, user_query):
    # Print the type and value of pitch_text for debugging
    print("Type of pitch_text: ", type(pitch_text))
    print("Value of pitch_text: ", pitch_text)

    # Use Elevenlabs to convert the pitch text into audio
    audio_content = tts_api.synthesize(pitch_text)
    if not audio_content:
        raise ValueError('Unable to synthesize audio content')
  

    # Save the generated audio into a file in a new folder
    max_filename_length = 255
    base_filename = user_query.replace(" ", "_") + "_pitch.mp3"

    # Create a new directory if it doesn't exist
    directory = 'audio_files'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Limit the length of filename to max_filename_length
    output_filename = (base_filename[:max_filename_length - 4] + ".mp3") if len(base_filename) > max_filename_length else base_filename
    output_filename = os.path.join(directory, output_filename) # adjust filename to include folder path

    with open(output_filename, 'wb') as output_file:
        output_file.write(audio_content)
  
    print("Audio content successfully written into file:", output_filename)
    logging.info(f'Successfully wrote audio content to file: {output_filename}')
    return output_filename

# With the file created and saved to the number then determine the content length of the video