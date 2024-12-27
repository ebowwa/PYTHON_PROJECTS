import logging
import os
def get_audio_duration(audio_path):
  cmd = ["./ffmpeg-6.0-amd64-static/ffmpeg", "-i", audio_path]
  result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
  lines = result.stderr.split('\n')
  for line in lines:
      if "Duration" in line:
          time = line.split(",")[0].split("Duration:")[1].strip()
          h, m, s = time.split(":")
          duration = int(h) * 3600 + int(m) * 60 + float(s)
          return duration
  return None

def adjust_video_duration(video_path, audio_duration, output_path):
  cmd = [
      "./ffmpeg-6.0-amd64-static/ffmpeg", 
      "-i", video_path, 
      "-t", str(audio_duration), 
      "-c", "copy", 
      output_path
  ]
  subprocess.run(cmd)
  
import subprocess
from initialize import initialize_api_keys
from query_processing import process_query
from audio_generation import generate_audio_and_save



def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Initialize API keys
    ELEVENLABS_API_KEY, default_voice_id, PULZE_API_KEY = initialize_api_keys()

    # Process user query
    tts_api, pitch_text, user_query = process_query()

    # Generate and save audio
    audio_path = generate_audio_and_save(tts_api, pitch_text, user_query)
    print(f"Generated audio path: {audio_path}")
    if not audio_path:
        raise ValueError("The audio path is not generated or returned by generate_audio_and_save function.")

    if condition_true: # replace 'condition_true' with your actual condition
        from org.connect import generate_videos
        # Generate videos
        # Define paths and values for the video generation
        images_dir = "simulation_theory"
        output_path_images = "scripts/animated_images.mp4"
        duration = 34
        gif_path = "scripts/animated_images.mp4"
        output_path_gif_audio = "animated_images_with_audio_final.mp4"

        generate_videos(images_dir, output_path_images, duration, gif_path, audio_path, output_path_gif_audio)

        # Adjust the video duration to match the audio duration
        audio_duration = get_audio_duration(audio_path)
        if audio_duration:
            adjust_video_duration(output_path_gif_audio, audio_duration, "adjusted_" + output_path_gif_audio)
        else:
            print("Error: Could not determine audio duration.")
    else:
        from replicate_client import run_replicate
        input_data = {
            "fps": 24,
            "seed": 17,
            "steps": 80,
            "width": 640,
            "height": 640,
            "scheduler": "euler_ancestral",
            "animations": "live | right | right | right | live",
            "max_frames": 72,
            "prompt_durations": "0.6 | 0.3 | 1 | 0.3 | 0.8",
            "animation_prompts": "winter forest, snowflakes, Van Gogh style | spring forest, flowers, sun rays, Van Gogh style | summer forest, lake, reflections on the water, summer sun, Van Gogh style | autumn forest, rain, Van Gogh style | winter forest, snowflakes, Van Gogh style"
        }

        result = run_replicate(input_data)
        print(result)

def get_content_length(audio_file):
    return os.path.getsize(audio_file)

if __name__ == "__main__":
    main()
