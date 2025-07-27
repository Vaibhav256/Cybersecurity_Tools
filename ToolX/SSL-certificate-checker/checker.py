import socket
import ssl
from datetime import datetime
from urllib.parse import urlparse

def get_hostname(domain):
    parsed = urlparse(domain)
    return parsed.hostname or domain

def get_signature_algorithm(cert_bin):
    try:
        from cryptography import x509
        from cryptography.hazmat.backends import default_backend
        cert = x509.load_der_x509_certificate(cert_bin, default_backend())
        return cert.signature_hash_algorithm.name.upper()
    except Exception:
        return "Unknown"

def check_ssl_cert(domain):
    try:
        hostname = get_hostname(domain)
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                binary_cert = ssock.getpeercert(binary_form=True)

                expiry = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")
                start = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y GMT")
                issuer = cert.get('issuer')
                issuer_str = ' / '.join([val for group in issuer for key, val in group])
                san = [entry[1] for entry in cert.get('subjectAltName', [])]
                days_left = (expiry - datetime.utcnow()).days
                algo = get_signature_algorithm(binary_cert)
                algo_status = "✓ Strong" if "SHA256" in algo else "Weak !!"

                print(f"\n### SSL Certificate Info for: {hostname}")
                print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"• Status            : {'Valid' if days_left > 0 else 'Expired'}")
                print(f"• Start Date        : {start.strftime('%Y-%m-%d')}")
                print(f"• Expiry Date       : {expiry.strftime('%Y-%m-%d')}")
                print(f"• Days Remaining    : {days_left}")
                print(f"• Hash Algorithm    : {algo} ({algo_status})")
                print(f"• Issuer            : {issuer_str}")
                print(f"• Subject Alt Names :")
                for entry in san:
                    print(f"  - {entry}")
                print()
    except Exception as e:
        print(f"\n## Error checking SSL for {domain}: {str(e)}\n")

# Header
print("===== SSL Certificate Scanner =====")

while True:
    domain = input("Enter domain (or 'exit'): ").strip()
    if domain.lower() == "exit":
        print("Exiting... Stay secure!")
        break
    check_ssl_cert(domain)