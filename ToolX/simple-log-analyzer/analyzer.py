import re
from collections import defaultdict

def analyze_logs(log_lines):
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    port_pattern = re.compile(r'(?<=port\s)\d+')
    failed_keywords = ['failed', 'unauthorized', 'denied']

    ip_data = defaultdict(lambda: {'count': 0, 'failed': 0, 'lines': []})
    port_hits = defaultdict(set)
    flagged_logs = []

    for line in log_lines:
        ip_match = ip_pattern.search(line)
        port_match = port_pattern.search(line)
        line_lower = line.lower()

        if ip_match:
            ip = ip_match.group()
            ip_data[ip]['count'] += 1
            ip_data[ip]['lines'].append(line)
            if any(word in line_lower for word in failed_keywords):
                ip_data[ip]['failed'] += 1

        if port_match:
            port = port_match.group()
            ip = ip_match.group() if ip_match else "unknown"
            port_hits[port].add(ip)

    # Flag anomalies and provide remediation guidance
    for ip, data in ip_data.items():
        if data['count'] > 100:
            flagged_logs.append(f"[CRITICAL] High traffic from {ip} ({data['count']} entries)")
            flagged_logs.append(f"    → Sample log: {data['lines'][0].strip()}")
            flagged_logs.append("    → Fix: Rate-limit this IP, audit services it accessed, investigate burst patterns")

        if data['failed'] > 10:
            flagged_logs.append(f"[WARN] Repeated failed attempts from {ip} ({data['failed']} times)")
            flagged_logs.append(f"    → Sample log: {data['lines'][0].strip()}")
            flagged_logs.append("    → Fix: Enable lockout policies, use fail2ban, check for leaked credentials")

    for port, ips in port_hits.items():
        if port not in ['80', '443', '22', '53']:  # common ports
            flagged_logs.append(f"[WARN] Unusual port accessed: {port} by {len(ips)} unique IPs")
            flagged_logs.append(f"    → Fix: Audit firewall rules, verify service exposure on port {port}, restrict if unnecessary")

    return {
        'ip_data': ip_data,
        'port_hits': port_hits,
        'flagged_logs': flagged_logs
    }

# Example usage
if __name__ == "__main__":
    logfile = input("Enter path to log file: ").strip()
    with open(logfile, 'r') as f:
        lines = f.readlines()

    results = analyze_logs(lines)

    print("\n== IP Activity ==")
    for ip, data in results['ip_data'].items():
        print(f"  - {ip}: {data['count']} entries")

    print("\n== Failed Attempts ==")
    for ip, data in results['ip_data'].items():
        if data['failed'] > 0:
            print(f"  - {ip}: {data['failed']} failed")

    print("\n== Ports Accessed ==")
    for port, ips in results['port_hits'].items():
        print(f"  - Port {port}: accessed by {len(ips)} IPs")

    print("\n== Flagged Logs and Recommendations ==")
    if results['flagged_logs']:
        for entry in results['flagged_logs']:
            print(f"  - {entry}")
    else:
        print("  No anomalies detected.")