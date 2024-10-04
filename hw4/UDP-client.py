import socket
import sys
from time import time
from datetime import datetime, timezone


def client() -> None:
    if len(sys.argv) != 3:
        print("Usage: python UDP-client.py <server-IP-address> <server-port-number>")
        sys.exit(1)

    server_ip: str = sys.argv[1]
    server_port: int = int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(b"", (server_ip, server_port))
        client_socket.settimeout(5)
        try:
            t_send: float = time()
            data, _addr = client_socket.recvfrom(1024)
            t_receive: float = time()
        except socket.timeout:
            print("Request timed out")
            sys.exit(1)

    local_time: datetime = datetime.now(timezone.utc)
    server_timestamp_str: str = data.decode("utf-8")
    server_timestamp: datetime = datetime.fromisoformat(
        server_timestamp_str.rstrip("Z")
    )

    time_difference: float = (local_time - server_timestamp).microseconds / 1000
    rtt_ms: float = (t_receive - t_send) * 1000

    print(f"Server timestamp: {server_timestamp_str}")
    print(f"Local time: {local_time.isoformat(timespec='milliseconds') + 'Z'}")
    print(f"Time difference (ms): {time_difference}")
    print(f"RTT (ms): {rtt_ms}")

    return None


if __name__ == "__main__":
    client()
