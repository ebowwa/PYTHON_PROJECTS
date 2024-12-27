from org.connect import setup_environment, create_video_from_images, loop_gif_to_match_audio, generate_videos


if __name__ == "__main__":
    # Define paths and values
    images_dir = "simulation_theory"
    output_path_images = "scripts/animated_images.mp4"
    duration = 34
    gif_path = "scripts/animated_images.mp4"
    audio_path = "audio_files/a_worldview_about_simulation_theory_about_hermeticsm_and_Solipsism_pitch.mp3"
    output_path_gif_audio = "animated_images_with_audio_final.mp4"

    # Generate videos
    generate_videos(images_dir, output_path_images, duration, gif_path, audio_path, output_path_gif_audio)
