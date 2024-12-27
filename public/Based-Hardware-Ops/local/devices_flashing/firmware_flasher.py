import os
import sys
import time
from datetime import datetime
from devices_flashing.device_detector import DeviceDetector
from devices_flashing.flash_history import FlashHistory
from devices_flashing.firmware_uploader import FirmwareUploader

class FirmwareFlasher:
    def __init__(self, firmware_file):
        if not os.path.exists(firmware_file):
            print(f"Error: Firmware file {firmware_file} not found.")
            sys.exit(1)
        
        self.firmware_file = firmware_file
        self.device_detector = DeviceDetector()
        self.flash_history = FlashHistory()
        self.firmware_uploader = FirmwareUploader(firmware_file)
        self.flashed_devices = set(device['path'] for device in self.flash_history.get_history()['devices'])

    def start_flashing_process(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Starting continuous firmware flashing process...")
        print(f"Firmware file: {self.firmware_file}")
        print("Waiting for devices to be connected in DFU mode...")
        print("Press Ctrl+C to stop the script.")
        print(f"Total devices flashed so far: {self.flash_history.get_total_flashed()}")

        try:
            while True:
                self._process_devices()
                time.sleep(1)  # Wait for 1 second before checking again
        except KeyboardInterrupt:
            print("\nScript terminated by user.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
        finally:
            self._print_summary()

    def _process_devices(self):
        devices = self.device_detector.get_connected_devices()
        for device in devices:
            if device not in self.flashed_devices:
                self._flash_device(device)

        # Remove devices that are no longer connected from flashed_devices
        self.flashed_devices = {device for device in self.flashed_devices if device in devices}

    def _flash_device(self, device):
        print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - New device detected: {device}")
        print(f"Attempting to flash {device}...")
        
        try:
            success = self.firmware_uploader.flash_and_verify(device)

            if success:
                self.flash_history.add_flashed_device(device)
                self.flashed_devices.add(device)
                print(f"Device flashed successfully. UUID: {self.flash_history.get_last_flashed_uuid()}")
                print(f"Total devices flashed: {self.flash_history.get_total_flashed()}")
            else:
                print(f"Failed to flash {device}. Will retry on next detection.")
        except PermissionError:
            print(f"Error: Permission denied when trying to flash {device}.")
            print("Please ensure you have the necessary permissions to write to the device.")
            print("You may need to run the script with sudo or adjust your system permissions.")
        except Exception as e:
            print(f"An unexpected error occurred while flashing {device}: {e}")

    def _print_summary(self):
        print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Flashing process ended.")
        print(f"Total devices flashed in this session: {self.flash_history.get_total_flashed() - len(self.flashed_devices)}")
        print(f"Total devices flashed overall: {self.flash_history.get_total_flashed()}")