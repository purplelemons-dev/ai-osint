"Serve this app as a RESTful API."
from http.server import BaseHTTPRequestHandler, HTTPServer
from . import ai_osint
import json


class ServeAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        # method not implemented
        self.send_response(501)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write('{"error": "Method not implemented, try POST"}'.encode())
        return

    def do_POST(self):
        # Body should have name, email, phone, username, address, ip, domain, password, or hashed_password
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode("utf-8")
        post_data: dict = json.loads(post_data)

        ai_response = (
            ai_osint(
                name=post_data.get("name"),
                phone=post_data.get("phone"),
                email=post_data.get("email"),
                username=post_data.get("username"),
                address=post_data.get("address"),
                ip=post_data.get("ip"),
                domain=post_data.get("domain"),
                password=post_data.get("password"),
                hashed_password=post_data.get("hashed_password"),
                debug=True,
            )
            .choices[0]
            .message.content
        )
        try:
            parsed = json.loads(ai_response)
            self.wfile.write(json.dumps(parsed).encode())
        except:
            self.wfile.write(ai_response.encode())
        return


def run(server_class=HTTPServer, handler_class=ServeAPI, port=10021):
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
