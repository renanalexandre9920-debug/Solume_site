from flask import Flask, send_from_directory, make_response, request
from pathlib import Path

# Servidor opcional para servir o site com headers de segurança.
# Uso:
#   python secure_server.py
# Depois acesse: http://127.0.0.1:8000

APP_ROOT = Path(__file__).parent
STATIC_ROOT = APP_ROOT

app = Flask(__name__, static_folder=None)

CSP = ("default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; "
       "img-src 'self' data:; font-src 'self' https://fonts.gstatic.com; "
       "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "script-src 'self'; connect-src 'self'; "
       "form-action 'self' https://wa.me https://www.instagram.com; upgrade-insecure-requests")

SEC_HEADERS = {
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=(), payment=(), usb=()",
    "Content-Security-Policy": CSP,
    # HSTS só faz sentido em HTTPS; ao publicar, configure no host também.
}

@app.after_request
def add_security_headers(resp):
    for k, v in SEC_HEADERS.items():
        resp.headers[k] = v
    return resp

@app.route("/")
def index():
    return send_from_directory(STATIC_ROOT, "index.html")

@app.route("/<path:path>")
def static_files(path):
    full = (STATIC_ROOT / path).resolve()
    if not str(full).startswith(str(STATIC_ROOT.resolve())):
        return make_response("Not found", 404)
    return send_from_directory(STATIC_ROOT, path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
