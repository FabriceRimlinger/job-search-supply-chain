#!/usr/bin/env python3
"""Serveur local JANUS — lecture + écriture des fichiers .md"""

import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765
BASE = os.path.dirname(os.path.abspath(__file__))

class JanusHandler(SimpleHTTPRequestHandler):

    def do_PUT(self):
        path = self.translate_path(self.path)
        # Sécurité : écriture autorisée uniquement dans le dossier du projet
        if not os.path.realpath(path).startswith(os.path.realpath(BASE)):
            self.send_error(403, "Forbidden")
            return
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(data)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, fmt, *args):
        line = str(args[0]) if args else ''
        if 'favicon' in line or 'favicon' in str(args):
            return
        parts = line.split()
        if len(parts) >= 2:
            if parts[0] == 'PUT':
                print(f"  ✎  {parts[1]}")
            else:
                print(f"  →  {parts[1]}")

if __name__ == '__main__':
    os.chdir(BASE)
    server = HTTPServer(('localhost', PORT), JanusHandler)
    print(f"JANUS server  →  http://localhost:{PORT}/janus.html")
    print("Ctrl+C pour arrêter\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
