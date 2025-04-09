import socket
import argparse


parser = argparse.ArgumentParser(description="Network Banner Grabbing Tool")
parser.add_argument("-i", "--ihost", type=str, required=True, help="Target host IP address to connect and scan for service banners")
parser.add_argument("-p", "--port", type=int, required=False, help="Specific port to scan on the target host (optional)")
parser.add_argument("-b", "--byte", type=int, default=1024, help="Number of bytes to retrieve while grabbing the banner (default: 1024)")

args = parser.parse_args()


if not args.ihost:
    print("[!] IP address not provided.")
    exit(1)

if args.port is None or not (1 <= args.port <= 65535):
    print("[!] Invalid port number. Must be between 1 and 65535.")
    exit(1)


if args.byte <= 0:
    print("[!] Invalid byte size. Must be a positive integer.")
    exit(1)

def gt_banner(ip, port, data_byte=1024):
    try:
        sokt = socket.socket()
        sokt.settimeout(2)  
        sokt.connect((ip, port))
        
        try:
            banner = sokt.recv(data_byte).decode('utf-8', errors='ignore').strip()
            print(f"[+] Banner from {ip}:{port} => {banner}")
        except socket.timeout:
            print(f"[!] Timeout occurred while receiving data from {ip}:{port}")
        except socket.error as e:
            print(f"[!] Error receiving data from {ip}:{port}: {e}")

    except ConnectionRefusedError:
        print(f"[-] Port {port} is closed on [{ip}]")
    except socket.timeout:
        print(f"[!] Connection timed out for {ip}:{port}")
    except socket.gaierror:
        print(f"[!] Address-related error for {ip}")
    except socket.herror:
        print(f"[!] Hostname-related error for {ip}")
    except PermissionError:
        print("[!] Insufficient permissions to open socket. Try running as admin/root.")
    except OSError as e:
        print(f"[!] OS-level error occurred: {e}")
    except Exception as e:
        print(f"[!] Unexpected error for {ip}:{port}: {e}")
    finally:
        sokt.close()

def main():
    print("Welcome to Harald's SNA Banner Grab Assignment!")
    gt_banner(args.ihost, args.port, args.byte)

main()