"""
Simple model serving script
Author: Golla Nikhil - 2022BCS0077
"""
import pickle
import json
import numpy as np
from http.server import HTTPServer, BaseHTTPRequestHandler

class ModelHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "healthy",
                "author": "Golla Nikhil",
                "roll": "2022BCS0077"
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[Golla Nikhil - 2022BCS0077] {format % args}")

def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    model = load_model()
    print("=" * 50)
    print("Model server started | Golla Nikhil | 2022BCS0077")
    print("Listening on port 8080")
    print("=" * 50)
    server = HTTPServer(("0.0.0.0", 8080), ModelHandler)
    server.serve_forever()
