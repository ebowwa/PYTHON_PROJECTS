import shutil
import time
from datetime import datetime
from devices_flashing.device_detector import DeviceDetector

class FirmwareUploader:
    def __init__(self, firmware_file):
        self.firmware_file = firmware_file
        self.device_detector = DeviceDetector()

    def flash_and_verify(self, device):
        """Flash the firmware to the device and verify the process."""
        flash_result = self._flash_firmware(device)
        
        if flash_result == "LIKELY_SUCCESS" or flash_result is True:
            print("Verifying if device was actually flashed...")
            if self._verify_flashing(device):
                print("Device successfully flashed and rebooted!")
                return True
            else:
                print("Device might not have been flashed successfully. It's still in DFU mode.")
        return False

    def _flash_firmware(self, device):
        """Flash the firmware to the device by copying the UF2 file."""
        try:
            shutil.copy(self.firmware_file, device)
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Successfully copied firmware to {device}")
            return True
        except IOError as e:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - I/O error occurred, which likely indicates a successful flash: {e}")
            return "LIKELY_SUCCESS"
        except Exception as e:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: Failed to flash firmware to {device}. {e}")
            return False

    def _verify_flashing(self, device):
        """Verify if the device was actually flashed by checking if it's no longer in DFU mode."""
        for _ in range(10):  # Check for up to 10 seconds
            time.sleep(1)
            if device not in self.device_detector.get_connected_devices():
                return True
        return False