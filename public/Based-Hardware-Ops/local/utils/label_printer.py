import os
import subprocess

def print_labels(label_dir, printer, media_size):
    try:
        for file in os.listdir(label_dir):
            if file.endswith(".pdf"):
                file_path = os.path.join(label_dir, file)
                print_command = f"lp -o media={media_size} -d {printer} '{file_path}'"
                subprocess.run(print_command, shell=True, check=True)
                os.remove(file_path)
        return f"Labels printed successfully from {label_dir} using {printer} with media size {media_size}."
    except Exception as e:
        return f"Error printing labels: {str(e)}"