import socket
import argparse
import sys
import time
IHOST="127.0.0.1"
PORT=4000




def socket_sed_recv(socket_client,message,byte):
    """Send a message and receive a response using a socket."""
    try:
        socket_client.send(message.encode('utf-8'))
        received_message = socket_client.recv(byte).decode('utf-8')
        return received_message
    except socket.error as e:
        print(f"Socket Error: {e}")
        sys.exit(1)
def main():
    parser = argparse.ArgumentParser(description="🛰️  Socket Client Application")
    parser.add_argument("-i", "--ihost", type=str, required=True, default="127.0.0.1", help="🌐 Server IP address")
    parser.add_argument("-p", "--port", type=int, required=True, default=4000, help="📡 Server port")
    parser.add_argument("-m", "--message", type=str, help="💬 Message to send to the server")
    parser.add_argument("-b", "--bytes", type=int, default=2048, help="📥 Buffer size for receiving data")


    args = parser.parse_args()

    if args.port < 1 or args.port > 65535:
        print("❌ Error: Port number must be between 1 and 65535")
        sys.exit(1)
    try:
        socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_client.connect((args.ihost,args.port))
        if args.message:
                print(f"✅ Connected to {args.ihost}:{args.port} — Sending: “{args.message}”")

                message=socket_sed_recv(socket_client,"hihihi",args.bytes)
                print(f"🟢 Server replied: {message}")
        else:
            print(f"✅ Connected to {args.ihost}:{args.port}")
            print("💬 Type your messages below. Type 'exit' to end the chat.\n")
            while True:
                sendmsg=str(input(f"\n──(📝㉿{args.ihost})-[~]"))
                if sendmsg.strip().lower() == "exit":
                    print("👋 Exiting chat...")
                    break

                message=socket_sed_recv(socket_client,sendmsg,args.bytes)
                print(f"📨 Reply: {message}")
                time.sleep(0.5) 
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        sys.exit(1)


    socket_client.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Thank you for using me. Goodbye!")
        sys.exit(0)