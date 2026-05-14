from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # ارسال پاسخ ساده
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "alive",
            "time": datetime.now().isoformat(),
            "message": "Server is running on Vercel",
            "test": "اگر این متن را می‌بینید، Vercel از ایران قابل دسترس است"
        }
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        # برای تست Webhook
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "received",
            "your_data": body.decode() if body else "nothing",
            "time": datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(response).encode())
