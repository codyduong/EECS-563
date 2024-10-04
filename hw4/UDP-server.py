import socket
import sys
from select import select
from datetime import datetime, timezone


def server() -> None:
    if len(sys.argv) != 2:
        print("Usage: python UDP-server.py <server-port-number>")
        sys.exit(1)

    port: int = int(sys.argv[1])

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(("", port))

        print(f"UDP server listening on port {port}")

        while True:
             # allow CTRL+C by using select to prevent accept from blocking any I/O -@codyduong
            readable, _, _ = select([server_socket], [], [], 1)
            if readable:
                _data, addr = server_socket.recvfrom(1024)
                print(f"Received request from {addr}")
                timestamp: str = (
                    datetime.now(timezone.utc).isoformat(timespec="milliseconds") + "Z"
                )
                server_socket.sendto(timestamp.encode("utf-8"), addr)


if __name__ == "__main__":
    server()
