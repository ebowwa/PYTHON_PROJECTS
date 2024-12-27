import sys
import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from devices_flashing import FirmwareFlasher
from urllib.parse import parse_qs
from utils.label_printer import print_labels

class LabelPrintingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/views/printing.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/print':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)

            label_dir = params.get('labelDir', ['/Users/ebowwa/Based-Hardware/shipping/2'])[0]
            printer = params.get('printer', ['MUNBYN_ITPP941AP'])[0]
            media_size = params.get('mediaSize', ['4x6'])[0]

            response = print_labels(label_dir, printer, media_size)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_error(404)

def run_web_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LabelPrintingHandler)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()

def run_firmware_flasher(firmware_file):
    print("Starting firmware flashing process...")
    flasher = FirmwareFlasher(firmware_file)
    flasher.start_flashing_process()
    print("Firmware flashing process is running in the background.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python index.py <firmware_file.uf2>")
        sys.exit(1)

    firmware_file = sys.argv[1]
    
    if not os.path.exists('views/printing.html'):
        print("Error: views/printing.html not found.")
        sys.exit(1)
    
    firmware_thread = threading.Thread(target=run_firmware_flasher, args=(firmware_file,))
    firmware_thread.start()

    run_web_server()

    firmware_thread.join()

if __name__ == "__main__":
    main()