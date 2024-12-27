from flask import Flask, jsonify, request
from _backend.metaphor.contentQuery import exa_api_search
from _backend.inference.client import OpenAIClient
from _backend.resemble.speech import create_audio_clip
from ffmpeg_integration import stitch_video_audio
import os
import uuid
import requests

app = Flask(__name__)

client = OpenAIClient(api_key="null", base_url="https://dev-hub.agentartificial.com")

@app.route('/get_chat_response', methods=['POST'])
def get_chat_response():
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.get_chat_response(message)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
@app.route('/process_content', methods=['POST'])
def process_content():
    # Extract user inquiry from the request
    data = request.json
    user_inquiry = data.get('inquiry')

    # Step 1: Content Retrieval
    video_content = exa_api_search(user_inquiry)
    if not video_content:
        return jsonify({'error': 'No content found'}), 404

    # Extracting video URL and text for narration
    video_url = video_content.get('video_url')
    narration_text = video_content.get('narration_text')

    # Step 2: Narration
    # Instantiate OpenAIClient with necessary credentials (assumed to be set as environment variables)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_client = OpenAIClient(api_key=openai_api_key)
    narration_result = openai_client.narrate(narration_text)
    if not narration_result:
        return jsonify({'error': 'Narration failed'}), 500

    # Step 3: Audio Generation
    # Dynamically generate audio clip with required parameters
    audio_clip = create_audio_clip(
        project_uuid=str(uuid.uuid4()),
        title='Generated Audio',
        body=narration_result,
        voice_uuid=os.getenv('RESEMBLE_VOICE_UUID')
    )
    if not audio_clip:
        return jsonify({'error': 'Audio generation failed'}), 500

    # Step 4: Download video content
    video_file_path = f'/tmp/{uuid.uuid4()}.mp4'
    with requests.get(video_url, stream=True) as r:
        r.raise_for_status()
        with open(video_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

    # Step 5: FFmpeg Integration
    # Assuming audio_clip contains path to generated audio
    audio_file_path = audio_clip.get('audio_file_path')
    output_file_path = f'/output/{uuid.uuid4()}.mp4'
    stitch_video_audio(video_file_path, audio_file_path, output_file_path)

    # Step 6: Provide download link
    download_link = f'http://{request.host}/download/{output_file_path}'
    return jsonify({'download_link': download_link})

if __name__ == '__main__':
    app.run(debug=True)