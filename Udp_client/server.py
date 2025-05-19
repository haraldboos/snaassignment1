import socket
import random
import argparse
import sys

parser = argparse.ArgumentParser(description="UDP Server Tool")
parser.add_argument("--host", type=str, default="127.0.0.1", help="Server host address")
parser.add_argument("--port", type=int, default=9999, help="Server port number")
parser.add_argument("--buffer", type=int, default=1024, help="Buffer size for receiving messages")

args = parser.parse_args()

HOST = args.host
PORT = args.port
BUFFERSIZE = args.buffer

try:
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((HOST, PORT))
    print(f"✅ UDP server up and listening on {HOST}:{PORT}...")
except socket.error as err:
    print(f"❌ Socket error: {err}")
    sys.exit(1)

try:
    while True:
        try:
            data, client_address = UDPServerSocket.recvfrom(BUFFERSIZE)
            print(f"📩 Received '{data.decode()}' from {client_address[0]}")
            
            number = random.randint(1111, 9999)
            response_message = f"Hello, client! {number}".encode()
            UDPServerSocket.sendto(response_message, client_address)

            print(f"📤 Sent '{response_message.decode()}' to {client_address[0]} port {client_address[1]}")

        except socket.error as err:
            print(f"⚠️ Communication error: {err}")

except KeyboardInterrupt:
    print("\n🚪 Server shutting down gracefully...")
    UDPServerSocket.close()
    sys.exit(0)
