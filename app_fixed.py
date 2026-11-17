#!/usr/bin/env python3
"""Fixed localhost-only training API. Synthetic data only."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

TOKENS = {"token-user-1": 1, "token-user-2": 2}
USERS = {
    1: {"id": 1, "name": "Alice Example", "email": "alice@example.test"},
    2: {"id": 2, "name": "Bob Example", "email": "bob@example.test"},
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith("/api/users/"):
            return self.reply(404, {"error": "not found"})
        token = self.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        requester = TOKENS.get(token)
        if requester is None:
            return self.reply(401, {"error": "unauthorized"})
        try:
            target_id = int(self.path.rsplit("/", 1)[1])
        except ValueError:
            return self.reply(400, {"error": "invalid user id"})
        # FIX: enforce object-level authorization on every requested object.
        if target_id != requester:
            return self.reply(403, {"error": "forbidden"})
        user = USERS.get(target_id)
        if user is None:
            return self.reply(404, {"error": "user not found"})
        return self.reply(200, {"requester_id": requester, "profile": user})

    def reply(self, status, body):
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

if __name__ == "__main__":
    print("Fixed training API listening on http://127.0.0.1:8000 (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
