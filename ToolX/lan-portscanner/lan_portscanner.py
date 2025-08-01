import socket
import termcolor
import threading
import itertools
import sys

# Spinner animation
spinner = itertools.cycle(['-.', '\\..', '|...', '/....'])

open_ports = []
lock = threading.Lock()

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Reduced timeout for faster scanning
        sock.connect((ipaddress, port))
        with lock:
            open_ports.append(port)
            print(termcolor.colored(f"[+] Port {port} is Open!", 'green'))
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        sys.stdout.write("\r" + " " * 15)
        sys.stdout.write("\r" + termcolor.colored(f"Scanning: {next(spinner)}", 'cyan'))
        sys.stdout.flush()
    except Exception as e:
        print(termcolor.colored(f"[-] Error scanning port {port}: {e}", 'red'))

def scan(target, ports):
    print(termcolor.colored(f'\n[*] Starting Scan for {target}', 'cyan'))
    threads = []

    for port in range(1, ports + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(termcolor.colored(f"\n[*] Scan Complete for {target}", 'yellow'))
    if open_ports:
        print(termcolor.colored(f"[+] Open Ports: {open_ports}", 'green'))
    else:
        print(termcolor.colored("[-] No Open Ports Found", 'red'))

# User Input
try:
    targets = input("[*] Enter Targets to Scan (comma-separated): ")
    ports = int(input("[*] Enter the number of ports to scan: "))

    if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets...", 'yellow'))
        for ip_addr in targets.split(','):
            open_ports.clear()
            scan(ip_addr.strip(), ports)
    else:
        scan(targets.strip(), ports)

except KeyboardInterrupt:
    print(termcolor.colored("\n[-] Scan Interrupted by User", 'red'))
except Exception as e:
    print(termcolor.colored(f"[-] Error: {e}", 'red'))