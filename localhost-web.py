import http.server
import socketserver


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class CustomHandler(Handler):
    def log_message(self, format, *args):
        print("Custom your web!")  
        super().log_message(format, *args)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    httpd.serve_forever()
  
