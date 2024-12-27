from video_gemini import vision_model
from api._backend.text_to_speech import generate_speech 
from pydub import AudioSegment  # Ensure pydub is installed for audio handling.
from moviepy.editor import VideoFileClip  # Ensure moviepy is installed for video handling.

class VideoSpeechProcessor:
    def __init__(self, video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid):
        self.video_file_path = video_file_path
        self.target_frame_rate = target_frame_rate
        self.prompt_path = prompt_path
        self.project_uuid = project_uuid
        self.voice_uuid = voice_uuid
        self.total_text_length = 0  # Initialize total text length counter

    def get_video_duration(self):
        """Get the duration of the video in seconds."""
        with VideoFileClip(self.video_file_path) as video:
            return video.duration

    def process_video(self):
        """Process video to obtain text responses for TTS."""
        return vision_model(self.video_file_path, self.target_frame_rate, self.prompt_path)

    def generate_speech_for_responses(self, responses):
        audio_files = []
        for sequence_number, response_text in enumerate(responses, start=1):
            self.total_text_length += len(response_text)
            title = f"AudioResponse_{sequence_number}"
            audio_path = generate_speech(response_text, self.project_uuid, self.voice_uuid, title, sequence_number)
            if audio_path:  # Check if a path was returned and it's not None
                audio_files.append(audio_path)
            else:
                print(f"Warning: No audio file generated for {title}.")
        return audio_files

    def calculate_total_audio_duration(self, audio_files):
        """Calculate the total duration of all audio files."""
        total_duration = 0
        for audio_file in audio_files:
            try:
                audio = AudioSegment.from_file(audio_file)
                total_duration += len(audio)
            except Exception as e:
                print(f"Error processing file {audio_file}: {e}")
        return total_duration / 1000  # Convert milliseconds to seconds

    def process_video_and_generate_speech(self):
        """Main method to process video and generate speech."""
        video_duration = self.get_video_duration()
        responses = self.process_video()
        audio_files = self.generate_speech_for_responses(responses)
        total_audio_duration = self.calculate_total_audio_duration(audio_files)
        return audio_files, self.total_text_length, total_audio_duration, video_duration
    
    # Function to concatenate audio files into one file
    def concatenate_audio_files(audio_files, output_path):
        combined = AudioSegment.empty()
        for audio_file in audio_files:
            audio = AudioSegment.from_file(audio_file)
            combined += audio
        combined.export(output_path, format="wav")

    from moviepy.editor import VideoFileClip, AudioFileClip
    import os

    def overlay_audio(video_path, audio_path, output_path):
        # Validate input paths
        if not video_path or not os.path.exists(video_path):
            raise ValueError(f"Video path is invalid or does not exist: {video_path}")
        if not audio_path or not os.path.exists(audio_path):
            raise ValueError(f"Audio path is invalid or does not exist: {audio_path}")

        # Load the video clip
        video_clip = VideoFileClip(video_path)

        # Load the audio file
        audio_clip = AudioFileClip(audio_path)

        # Set the audio of the video clip as the audio clip
        final_clip = video_clip.set_audio(audio_clip)

        # Write the result to a file
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


# Assuming overlay_audio is defined as provided earlier

if __name__ == "__main__":
    video_file_path = 'public/wrestling.mp4'
    target_frame_rate = 30
    prompt_path = 'prompts/narrations/tik5.md'
    project_uuid = '0448305f'
    voice_uuid = 'd3e61caf'

    processor = VideoSpeechProcessor(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
    audio_files, total_text_length, total_audio_duration, video_duration = processor.process_video_and_generate_speech()

    # Print information about the processing
    print(f"Generated audio files: {audio_files}")
    print(f"Total text length sent to TTS API: {total_text_length} characters")
    print(f"Total audio duration: {total_audio_duration} seconds")
    print(f"Video duration: {video_duration} seconds")

    # Check if any audio files were generated
    if audio_files:
        concatenated_audio_path = "output/concatenated_audio.wav"
        # Concatenate the audio files
        concatenate_audio_files(audio_files, concatenated_audio_path)

        # Overlay the concatenated audio onto the video
        output_video_path = "output/final_video_with_audio.mp4"
        overlay_audio(video_file_path, concatenated_audio_path, output_video_path)

        print("Audio overlay completed successfully.")
    else:
        print("No audio files were generated, skipping audio overlay.")

# Example usage
if __name__ == "__main__":
    video_file_path = 'public/wrestling.mp4'
    target_frame_rate = 30
    prompt_path = 'prompts/narrations/tik5.md'
    project_uuid = '0448305f'
    voice_uuid = 'd3e61caf'

    processor = VideoSpeechProcessor(video_file_path, target_frame_rate, prompt_path, project_uuid, voice_uuid)
    audio_files, total_text_length, total_audio_duration, video_duration = processor.process_video_and_generate_speech()
    print(f"Generated audio files: {audio_files}")
    print(f"Total text length sent to TTS API: {total_text_length} characters")
    print(f"Total audio duration: {total_audio_duration} seconds")
    print(f"Video duration: {video_duration} seconds")

    # Comparison or further processing can be done here with video_duration and total_audio_duration
