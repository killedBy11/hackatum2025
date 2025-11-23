# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from urllib.parse import parse_qs
import requests

# Configuration
OLLAMA_URL = "http://localhost:11434"  # Ollama endpoint
MODEL_NAME = "llama3.1"


class ProxyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body.decode())

        try:
            response = requests.post(
                OLLAMA_URL + self.path,
                json=data,
            )
            response.raise_for_status()
        except requests.RequestException as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
            return

        lines = response.text.strip().split("\n")

        # Parse each line individually
        token_objects = [json.loads(line) for line in lines]

        result = ""
        # Example: inspect tokens
        for token in token_objects:
            try:
                result += token['message']['content']
            except:
                result += token['response']

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'response': result}).encode())


def run_proxy():
    with HTTPServer(('0.0.0.0', 5000), ProxyRequestHandler) as httpd:
        print("Proxy running on port 5000")
        httpd.serve_forever()


if __name__ == "__main__":
    run_proxy()