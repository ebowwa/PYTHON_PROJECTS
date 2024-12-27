
import moviepy.editor as mpy
from rich.progress import track

# ------------------------ PART 1: Creating Video from Images ------------------------

# Paths to the image files
image_files = ['IMG_9501.JPG', 'IMG_9271.JPG', 'IMG_9499.JPG', 'IMG_9505.WEBP', 'IMG_9218.PNG', 'IMG_9215.WEBP', 'IMG_9225.PNG', 'IMG_9506.WEBP', 'IMG_9462.JPG', 'IMG_9498.JPG', 'IMG_9497.WEBP', 'IMG_9489.JPG', 'IMG_9221.WEBP', 'IMG_9270.JPG', 'IMG_9463.JPG', 'IMG_9507.WEBP', 'IMG_9495.WEBP', 'IMG_9500.JPG', 'IMG_9461.JPG', 'IMG_9220.WEBP', 'IMG_9503.WEBP', 'IMG_9449.JPG', 'IMG_9493.WEBP', 'IMG_9496.JPG', 'IMG_9219.WEBP', 'IMG_9223.PNG', 'IMG_9216.PNG', 'IMG_9222 2.PNG', 'IMG_9217.PNG', 'IMG_9493 2.WEBP', 'IMG_9224.PNG', 'IMG_9222.PNG', 'IMG_9504.WEBP', 'IMG_9232.JPG', 'IMG_9502.WEBP']

# Calculate image duration to match the audio's 34 seconds
img_duration = 34 / len(image_files)

# Load the images and set their duration
img_clips = [mpy.ImageClip(img_file).set_duration(img_duration) for img_file in track(image_files, description="Loading images...")]

# Concatenate images to create a video
video = mpy.concatenate_videoclips(img_clips, method="compose")

# Save as MP4 video
video.write_videofile("animated_images.mp4", fps=24)

print("Video creation from images completed!")

# ------------------------ PART 2: Looping GIF to match Audio ------------------------

# Paths to the GIF and audio files
gif_file = "animated_images_with_audio.gif"
audio_file = "Simulating_Ancient_Civilizations__Unraveling_the_Mysteries_of_Lost_Worlds_with_Virtual_Reality_pitch.mp3"

# Load the GIF and audio
gif_clip = mpy.VideoFileClip(gif_file)
audio = mpy.AudioFileClip(audio_file)

# Loop the GIF to match the audio's duration
looped_gif_clip = gif_clip.fx(mpy.vfx.loop, duration=audio.duration)

# Set the audio to the looped GIF
video_with_audio = looped_gif_clip.set_audio(audio)

# Save as MP4 video with explicit audio codec and bitrate
video_with_audio.write_videofile("animated_images_with_audio_final.mp4", fps=24, audio_codec='aac', audio_bitrate="300k")

print("Video creation with looped GIF and audio completed!")
