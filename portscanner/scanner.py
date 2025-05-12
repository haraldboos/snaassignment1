import socket
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Simple port scanner")
parser.add_argument("-i", "--ihost", type=str, required=True, help="Host IP address to scan")
parser.add_argument("-p", "--port", type=int, required=False, help="Single port to scan")
parser.add_argument("-s", "--start", type=int, required=False, help="Starting port of range")
parser.add_argument("-e", "--end", type=int, required=False, help="Ending port of range")
args = parser.parse_args()

ipaddress = args.ihost
def main():
    print("Welcome to Harald's SNA Port Scanning Assignment!")

    try:
        if args.port:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                try:
                    result = soc.connect_ex((ipaddress, args.port))
                    if result == 0:
                        tqdm.write(f"[+] Port {args.port} is open on {ipaddress}")
                    # else:
                    #     tqdm.write(f"[-] Port {args.port} is closed on {ipaddress}")
                except socket.timeout:
                    tqdm.write(f"⏳ Timeout occurred while scanning port {args.port}")
                except socket.error as e:
                    tqdm.write(f"❌ Socket error on port {args.port}: {e}")
                except socket.gaierror:
                    tqdm.write(f"❌ Failed to resolve address for {ipaddress} on port {args.port}")
                except socket.herror:
                    tqdm.write(f"❌ Hostname-related error on {ipaddress} for port {args.port}")

        elif args.start is not None and args.end is not None:
            for port in tqdm(range(args.start, args.end + 1), desc="Scanning", unit="port"):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    try:
                        soc.settimeout(0.5)
                        result = soc.connect_ex((ipaddress, port))
                        if result == 0:
                            tqdm.write(f"[+] Port {port} is open on {ipaddress}")
                        else:
                            tqdm.write(f"[-] Port {port} is closed on {ipaddress}")
                    except socket.timeout:
                        tqdm.write(f"⏳ Timeout occurred while scanning port {port}")
                    except socket.error as e:
                        tqdm.write(f"❌ Socket error on port {port}: {e}")
                    except socket.gaierror:
                        tqdm.write(f"❌ Failed to resolve address for {ipaddress} on port {port}")
                    except socket.herror:
                        tqdm.write(f"❌ Hostname-related error on {ipaddress} for port {port}")

        else:
            for port in tqdm(range(1, 65536), desc="Scanning", unit="port"):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    try:
                        soc.settimeout(0.5)
                        result = soc.connect_ex((ipaddress, port))
                        if result == 0:
                            tqdm.write(f"[+] Port {port} is open on {ipaddress}")
                        else:
                            tqdm.write(f"[-] Port {port} is closed on {ipaddress}")
                    except socket.timeout:
                        tqdm.write(f"⏳ Timeout occurred while scanning port {port}")
                    except socket.error as e:
                        tqdm.write(f"❌ Socket error on port {port}: {e}")
                    except socket.gaierror:
                        tqdm.write(f"❌ Failed to resolve address for {ipaddress} on port {port}")
                    except socket.herror:
                        tqdm.write(f"❌ Hostname-related error on {ipaddress} for port {port}")

    except KeyboardInterrupt:
        print("Port scanning interrupted. Goodbye!")

main()