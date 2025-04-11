import socket
import argparse
import sys
IHOST="127.0.0.1"
PORT=4000


if args.port < 1 or args.port > 65535:
        print("Error: Port number must be between 1 and 65535")
        sys.exit(1)

def socket_sed_recv(socket_client,message):
    """Send a message and receive a response using a socket."""
    try:
        socket_client.send(message.encode('utf-8'))
        received_message = socket_client.recv(4096).decode('utf-8')
        return received_message
    except socket.error as e:
        print(f"Socket Error: {e}")
        sys.exit(1)
def main():
    parser = argparse.ArgumentParser(description="Socket Client Application")
    parser.add_argument("-i", "--ihost", type=str, default="127.0.0.1", help="Server IP address (default: 127.0.0.1)")
    parser.add_argument("-p", "--port", type=int, default=4000, help="Server port (default: 4000)")
    parser.add_argument("-m", "--message", type=str, help="Message to send to the server")
    args = parser.parse_args()

    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect((args.ihost,args.port))
    send_message,recive_message=socket_sed_recv(socket_client,"hihihi")
    print(socket_client.recv(4096))
    socket_client.close()