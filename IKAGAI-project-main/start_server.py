#!/usr/bin/env python3
"""
Simple local server to run the Flask backend and serve the frontend.
"""
import os
import sys
import subprocess
import webbrowser
import time
from threading import Thread
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def start_flask():
    """Start Flask backend server"""
    os.chdir('backend')
    try:
        from app import app
        print("Starting Flask server on http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Error starting Flask: {e}")
        sys.exit(1)

def start_http_server():
    """Start HTTP server for frontend"""
    os.chdir('frontend')
    port = 8000
    handler = CORSRequestHandler
    httpd = HTTPServer(('localhost', port), handler)
    print(f"Starting HTTP server on http://localhost:{port}")
    print(f"Open http://localhost:{port}/demo.html in your browser")
    httpd.serve_forever()

if __name__ == '__main__':
    base_dir = Path(__file__).parent
    
    print("=" * 60)
    print("Mental Wellness Platform - Local Server")
    print("=" * 60)
    
    flask_thread = Thread(target=start_flask, daemon=True)
    flask_thread.start()
    
    time.sleep(2)
    
    http_thread = Thread(target=start_http_server, daemon=True)
    http_thread.start()
    
    time.sleep(1)
    
    print("\n" + "=" * 60)
    print("Servers are running!")
    print("=" * 60)
    print("\nFrontend: http://localhost:8000/demo.html")
    print("Backend API: http://localhost:5000")
    print("\nPress Ctrl+C to stop the servers")
    print("=" * 60 + "\n")
    
    try:
        webbrowser.open('http://localhost:8000/demo.html')
    except:
        pass
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down servers...")
        sys.exit(0)
