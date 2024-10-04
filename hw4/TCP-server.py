import socket
import sys
from select import select
from datetime import datetime, timezone


def server() -> None:
    if len(sys.argv) != 2:
        print("Usage: python TCP-server.py <server-port-number>")
        sys.exit(1)

    port: int = int(sys.argv[1])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", port))
        server_socket.listen()

        print(f"TCP server listening on port {port}")

        while True:
            # allow CTRL+C by using select to prevent accept from blocking any I/O -@codyduong
            readable, _, _ = select([server_socket], [], [], 1)
            if readable:
                conn, addr = server_socket.accept()
                with conn:
                    conn.settimeout(5)
                    print(f"Connected by {addr}")
                    timestamp: str = (
                        datetime.now(timezone.utc).isoformat(timespec="milliseconds")
                        + "Z"
                    )
                    conn.sendall(timestamp.encode("utf-8"))


if __name__ == "__main__":
    server()
