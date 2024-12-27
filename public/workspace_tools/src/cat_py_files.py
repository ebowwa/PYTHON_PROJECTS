import os
import json
from rich import print

class FileConcatenator:
    def __init__(self):
        self.concatenated_content = []

    def concatenate_files_from_json_and_save(self, json_file, output_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                file_paths = data['files_to_cat']

            for file_path in file_paths:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as content_file:
                        file_content = content_file.read()
                        self.concatenated_content.append(f"Contents of {file_path}:\n{file_content}\n{'='*50}\n")
                else:
                    self.concatenated_content.append(f"File {file_path} doesn't exist!\n{'='*50}\n")

            with open(output_file, 'w') as out_f:
                out_f.writelines(self.concatenated_content)

            print(f"[bold green]Concatenated content saved to {output_file}[/bold green]")
        except Exception as e:
            print(f"[bold red]Something went wrong: {e}[/bold red]")

    def cat_directory(self, directory):
        try:
            output_dict = {}
            print("Starting directory traversal...")

            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(".py") or file.endswith(".json"):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r") as f:
                            content = f.read().replace('\n', '\\n').replace('\r', '\\r')
                        output_dict[file_path] = content

            print("Directory traversal completed.")
            return output_dict
        except Exception as e:
            print(f"[bold red]Error while catting directory: {e}[/bold red]")

# Usage example:
# file_concatenator = FileConcatenator()
# file_concatenator.concatenate_files_from_json_and_save('workspace/file_path.json', 'concatenated_output.txt')

