import socket
import argparse
import sys

parser = argparse.ArgumentParser(description="UDP Client Tool")
parser.add_argument("--server", type=str, default="127.0.0.1", help="Server address")
parser.add_argument("--port", type=int, default=9999, help="Server port number")
parser.add_argument("--buffer", type=int, default=1024, help="Buffer size for receiving messages")

args = parser.parse_args()

SERVER = args.server
PORT = args.port
BUFFERSIZE = args.buffer

try:
    udpclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    print(f"✅ Connected to UDP server at {SERVER}:{PORT}")
except socket.error as err:
    print(f"❌ Socket error: {err}")
    sys.exit(1)

try:
    while True:
        msgFromClient = input("✏️ Enter message to server (or type 'exit' to quit): ")
        
        if msgFromClient.lower() == "exit":
            print("🚪 Exiting UDP client...")
            break
        
        udpclient.sendto(msgFromClient.encode(), (SERVER, PORT))
        
        try:
            msgfromserver, server_address = udpclient.recvfrom(BUFFERSIZE)
            print("📩 Message from server:", msgfromserver.decode())
        except socket.error as err:
            print(f"⚠️ Error receiving data: {err}")

except KeyboardInterrupt:
    print("\n🚪 Client shutting down gracefully...")
    udpclient.close()
    sys.exit(0)
