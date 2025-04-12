import socket
import threading
import argparse
import sys

def handle_client(client_socket, buffer_size):
    with client_socket as sock:
        try:
            while True:
                data = sock.recv(buffer_size)
                if not data:
                    print("Client disconnected.")
                    break
                print(f"Received: {data.decode('utf-8')}")
                sock.send("📨 Got it! Hit me with the next one.".encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")

def start_server(host, port, backlog, buffer_size):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(backlog)
        print(f"🚀 Server listening on {host}:{port} with backlog {backlog}")

        while True:
            try:
                client_socket, address = server_socket.accept()
                print(f"🔗 Connection from {address}")
                client_thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, buffer_size),
                    daemon=True,
                    name=f"Thread-{address[1]}"
                )
                client_thread.start()
            except socket.timeout:
                print("⏰ Socket accept timeout")
            except Exception as e:
                print(f"❗ Error accepting client: {e}")

    except OSError as e:
        print(f"🔌 Socket Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Multi-threaded Socket Server")
    parser.add_argument("-i", "--ihost", type=str, default="0.0.0.0", help="Server IP address")
    parser.add_argument("-p", "--port", type=int, default=4000, help="Server port")
    parser.add_argument("-c", "--count", type=int, default=6, help="Max queued connections")
    parser.add_argument("-b", "--bytes", type=int, default=2048, help="Buffer size for receiving data")
    args = parser.parse_args()

    start_server(args.ihost, args.port, args.count, args.bytes)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Thank you for using me. Goodbye!")
        sys.exit(0)