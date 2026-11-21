import threading
from http.server import HTTPServer
from urllib.request import urlopen

from intent_engine.main import Handler


def test_healthz():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with urlopen(f"http://127.0.0.1:{server.server_port}/healthz") as response:
            assert response.status == 200
            assert response.read() == b"ok"
    finally:
        server.shutdown()
