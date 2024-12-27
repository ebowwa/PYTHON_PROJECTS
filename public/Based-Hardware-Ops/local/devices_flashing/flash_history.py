import os
import json
import uuid
from datetime import datetime

class FlashHistory:
    FLASH_HISTORY_FILE = 'data/flash_history.json'

    def __init__(self):
        self.history = self._load_flash_history()

    def _load_flash_history(self):
        """Load the flash history from the JSON file or create a new one if it doesn't exist."""
        default_history = {"devices": [], "total_flashed": 0}
        
        if not os.path.exists(self.FLASH_HISTORY_FILE):
            print(f"Flash history file not found. Creating new file: {self.FLASH_HISTORY_FILE}")
            self._save_flash_history(default_history)
            return default_history

        try:
            with open(self.FLASH_HISTORY_FILE, 'r') as f:
                history = json.load(f)
            print(f"Loaded existing history: {history}")
            
            if not isinstance(history, dict) or 'devices' not in history or 'total_flashed' not in history:
                print("Invalid or incomplete history structure. Resetting to default.")
                self._save_flash_history(default_history)
                return default_history
            
            return history
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Resetting to default history.")
        except Exception as e:
            print(f"Unexpected error loading flash history: {e}. Resetting to default history.")
        
        self._save_flash_history(default_history)
        return default_history

    def _save_flash_history(self, history):
        """Save the flash history to the JSON file."""
        with open(self.FLASH_HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)

    def add_flashed_device(self, device_path):
        device_uuid = str(uuid.uuid4())
        self.history['devices'].append({
            "path": device_path,
            "uuid": device_uuid,
            "timestamp": datetime.now().isoformat()
        })
        self.history['total_flashed'] += 1
        self._save_flash_history(self.history)
        return device_uuid

    def get_history(self):
        return self.history

    def get_total_flashed(self):
        return self.history['total_flashed']

    def get_last_flashed_uuid(self):
        if self.history['devices']:
            return self.history['devices'][-1]['uuid']
        return None