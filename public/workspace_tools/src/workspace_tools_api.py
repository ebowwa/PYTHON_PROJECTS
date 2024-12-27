import os
import json
from cache_erase import PyCacheKiller
from cat_py_files import FileConcatenator

class WorkspaceToolsAPI:
    def __init__(self):
        self.cache_killer = PyCacheKiller()
        self.file_concatenator = FileConcatenator()

    def erase_cache(self, target_folder):
        self.cache_killer.target_folder = target_folder
        self.cache_killer.find_and_delete()

    def concatenate_files_from_json(self, json_file, output_file):
        self.file_concatenator.concatenate_files_from_json_and_save(json_file, output_file)

    def concatenate_files_in_directory(self, directory, output_file):
        self.file_concatenator.cat_directory(directory, output_file)

# Example usage
if __name__ == "__main__":
    api = WorkspaceToolsAPI()
    
    # Example usage to erase cache in a directory
    api.erase_cache('path/to/target/folder')

    # Example usage to concatenate files from a JSON list
    api.concatenate_files_from_json('path/to/json/file.json', 'output/concatenated.txt')

    # Example usage to concatenate all files in a directory
    api.concatenate_files_in_directory('path/to/directory', 'output/concatenated_dir.txt')
