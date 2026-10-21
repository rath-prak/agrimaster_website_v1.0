#!/usr/bin/env python3
"""
Development server with live reload support.
Serves the docs/ folder with auto-reload on file changes.
"""
import http.server
import os
import socketserver
from pathlib import Path

# Configurable root - defaults to docs/ relative to repository root
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
ROOT = os.environ.get('AGRIMASTER_ROOT', str(REPO_ROOT / 'docs'))

class ReloadHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)
    
    def end_headers(self):
        """Disable caching for development"""
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests with live reload injection"""
        # Version endpoint for live reload polling
        if self.path.startswith('/__version'):
            mtimes = []
            for dirpath, _, filenames in os.walk(ROOT):
                if '/screens' in dirpath:
                    continue
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    mtimes.append(os.path.getmtime(filepath))
            
            version = str(max(mtimes)) if mtimes else "0"
            body = version.encode()
            self.send_response(200)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        
        # Inject live reload script into HTML pages
        if self.path in ('/', '') or self.path.split('?')[0].endswith('.html'):
            path = self.path.split('?')[0]
            path = '/index.html' if path == '/' else path
            filepath = os.path.join(ROOT, path.lstrip('/'))
            
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    body = f.read()
                
                # Inject live reload script before closing body tag
                body = body.replace(b'</body>', b'<script src="/livereload.js"></script></body>')
                
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        
        # Default behavior for other files
        super().do_GET()

def main():
    """Start the development server"""
    port = int(os.environ.get('PORT', 8080))
    
    print(f"Agri Master Development Server")
    print(f"Serving: {ROOT}")
    print(f"URL: http://localhost:{port}")
    print(f"Live reload: enabled")
    print(f"\nPress Ctrl+C to stop")
    
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(('', port), ReloadHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")

if __name__ == "__main__":
    main()
