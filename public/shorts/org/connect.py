import os
def setup_environment():
  os.environ['IMAGEIO_FFMPEG_EXE'] = 'ffmpeg-6.0-amd64-static/ffmpeg'
  os.environ['FFMPEG_BINARY'] = 'ffmpeg-6.0-amd64-static/ffmpeg'
  os.environ['FFPROBE_BINARY'] = 'ffmpeg-6.0-amd64-static/ffprobe'
import moviepy.editor as mpy
from rich.progress import track

def create_video_from_images(dir_path: str, output_path: str, duration: float):
    """Create a video from images in a directory with a specified duration."""

    # Get a list of all files in the directory
    all_files = os.listdir(dir_path)

    # Filter out only image files based on extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    image_files = [os.path.join(dir_path, f) for f in all_files if any(f.lower().endswith(ext) for ext in image_extensions)]

    # Calculate image duration
    img_duration = duration / len(image_files)

    # Load the images and set their duration
    img_clips = [mpy.ImageClip(img_file).set_duration(img_duration) for img_file in track(image_files, description="Loading images...")]

    # Concatenate images to create a video
    video = mpy.concatenate_videoclips(img_clips, method="compose")

    # Save as MP4 video
    video.write_videofile(output_path, fps=24)
    print("Video creation from images completed!")

def loop_gif_to_match_audio(gif_path: str, audio_path: str, output_path: str):
    """Loop a GIF to match an audio's duration and save as an MP4 video."""

    # Load the GIF and audio
    gif_clip = mpy.VideoFileClip(gif_path)
    audio = mpy.AudioFileClip(audio_path)

    # Loop the GIF to match the audio's duration
    looped_gif_clip = gif_clip.fx(mpy.vfx.loop, duration=audio.duration)

    # Set the audio to the looped GIF
    video_with_audio = looped_gif_clip.set_audio(audio)

    # Save as MP4 video with explicit audio codec and bitrate
    video_with_audio.write_videofile(output_path, fps=24, audio_codec='aac', audio_bitrate="300k")
    print("Video creation with looped GIF and audio completed!")

def generate_videos(images_dir, output_path_images, duration, gif_path, audio_path, output_path_gif_audio):
    setup_environment()
    create_video_from_images(images_dir, output_path_images, duration)
    loop_gif_to_match_audio(gif_path, audio_path, output_path_gif_audio)
