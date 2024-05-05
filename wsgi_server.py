import socket
import io
import sys
import traceback

class WSGIServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self, app):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"WSGI server running on {self.host}:{self.port}...")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Client connected: {client_address}")
                self.handle_request(client_socket, app)

    def handle_request(self, client_socket, app):
        try:
            request_data = client_socket.recv(1024).decode("utf-8")
            if not request_data:
                return

            method, path, _ = request_data.split(" ", 2)
            environ = self.make_environ(method, path)

            # Start response function to send headers
            def start_response(status, headers):
                status_line = f"HTTP/1.1 {status}\r\n"
                header_lines = [f"{key}: {value}\r\n" for key, value in headers]
                response_headers = "".join(header_lines)
                client_socket.sendall(status_line.encode("utf-8"))
                client_socket.sendall(response_headers.encode("utf-8"))

            # Call the WSGI application
            response_body = app(environ, start_response)

            # Send the response body
            for data in response_body:
                client_socket.sendall(data)
        except Exception:
            traceback.print_exc()
        finally:
            client_socket.close()

    def make_environ(self, method, path):
        environ = {
            "REQUEST_METHOD": method,
            "PATH_INFO": path,
            "SERVER_NAME": self.host,
            "SERVER_PORT": str(self.port),
            "wsgi.version": (1, 0),
            "wsgi.url_scheme": "http",
            "wsgi.input": io.BytesIO(),
            "wsgi.errors": sys.stderr,
            "wsgi.multithread": False,
            "wsgi.multiprocess": False,
            "wsgi.run_once": False,
        }
        return environ

# Example WSGI application
def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]

    start_response(status, headers)
    return [b"Hello, World!"]

if __name__ == "__main__":
    server = WSGIServer("127.0.0.1", 8000)
    server.run(app)
