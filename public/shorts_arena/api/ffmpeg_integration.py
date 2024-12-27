
import subprocess

def stitch_video_audio(video_file: str, audio_file: str, output_file: str):
    command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_file
    ]
    subprocess.run(command, check=True)

# Example usage
if __name__ == '__main__':
    stitch_video_audio('path/to/video.mp4', 'path/to/audio.mp3', 'path/to/output.mp4')
