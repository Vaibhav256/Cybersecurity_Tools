import socket
import termcolor
import itertools
import sys
import time

# Scanning Animation
spinner = itertools.cycle(['-.', '\\..', '|...', '/....'])  # Spinner animation

def scan(target, ports):
    print(termcolor.colored(f'\n[*] Starting Scan for {target}', 'cyan'))
    for port in range(1, ports + 1):  # Scanning up to the given port (inclusive)
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Prevents hanging on unresponsive ports
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] Port {port} is Open!", 'green'))
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        sys.stdout.write("\r" + " " * 15)
        sys.stdout.write("\r" + termcolor.colored(f"Scanning: {next(spinner)}", 'cyan'))  # Scanner animation
        sys.stdout.flush()
        time.sleep(0.1)  # Control speed
    except Exception as e:
        print(termcolor.colored(f"[-] Error scanning port {port}: {e}", 'red'))

# User Input
targets = input("[*] Enter Targets to Scan(comma-separated): ")
ports = int(input("[*] Enter the number of ports to scan: "))

# Scanning logic
if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets...", 'yellow'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)
