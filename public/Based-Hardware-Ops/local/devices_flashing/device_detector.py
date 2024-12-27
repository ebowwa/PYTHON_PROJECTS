import sys
import glob

class DeviceDetector:
    @staticmethod
    def get_connected_devices():
        """Detect connected devices in DFU mode for macOS."""
        if sys.platform.startswith('darwin'):
            return glob.glob('/Volumes/XIAO-SENSE')
        else:
            print(f"Unsupported platform: {sys.platform}")
            return []