import requests

def hackertarget(domain):
    print("\n--> Using Hackertarget...")
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        res = requests.get(url)
        if res.ok:
            return {line.split(',')[0] for line in res.text.splitlines()}
    except Exception as e:
        print(f"[Hackertarget Error] {e}")
    return set()

def certspotter(domain):
    print("\n--> Using CertSpotter...")
    try:
        url = f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
        res = requests.get(url)
        if res.ok:
            data = res.json()
            return {dns for entry in data for dns in entry.get("dns_names", []) if domain in dns}
    except Exception as e:
        print(f"[CertSpotter Error] {e}")
    return set()

# ---------- MAIN ----------
domain = input("Enter domain (e.g., example.com): ").strip()

results = set()
results |= hackertarget(domain)
results |= certspotter(domain)

print(f"\n✓ Found {len(results)} unique subdomains:\n")
for sub in sorted(results):
    print(sub)