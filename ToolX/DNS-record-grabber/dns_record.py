import dns.resolver

def grab_dns_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT', 'SOA']
    results = {}

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers) as e:
            results[record] = [f'No {record} record found ({e.__class__.__name__})']
        except Exception as e:
            results[record] = [f'Error fetching {record}: {str(e)}']

    # Auth records
    spf = [txt for txt in results.get('TXT', []) if 'v=spf1' in txt]
    selectors = ['default', 'selector1', 'google']
    dkim = []
    for selector in selectors:
        try:
            dkim_answers = dns.resolver.resolve(f"{selector}._domainkey.{domain}", 'TXT')
            for rdata in dkim_answers:
                dkim.append(f"{selector}._domainkey.{domain}: {str(rdata)}")
        except:
            continue
    dmarc = []
    try:
        dmarc_answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        dmarc = [str(rdata) for rdata in dmarc_answers]
    except:
        pass

    # Store and annotate
    results['SPF'] = spf if spf else ['No SPF record found']
    results['SPF_Commentary'] = (
        "!! No SPF record — this domain is vulnerable to spoofing attacks." if not spf else (
            "✓ SPF present — helps prevent spoofing, but verify it includes authorized senders."
        )
    )

    results['DKIM'] = dkim if dkim else ['No DKIM record found']
    results['DKIM_Commentary'] = (
        "!! No DKIM — message integrity cannot be verified, increasing risk of tampering." if not dkim else (
            "✓ DKIM record found — verify selector coverage and key rotation practices."
        )
    )

    results['DMARC'] = dmarc if dmarc else ['No DMARC record found']
    results['DMARC_Commentary'] = (
        "!! No DMARC — domain has no policy for handling forged emails." if not dmarc else (
            "✓ DMARC present — check policy (p=quarantine/reject) for effectiveness."
        )
    )

    return results

# Run it
if __name__ == "__main__":
    domain = input("Enter domain: ").strip()
    records = grab_dns_records(domain)
    for rtype, rdata_list in records.items():
        if "Commentary" not in rtype:
            print(f"\n{rtype} Records:")
            for rdata in rdata_list:
                print(f"  - {rdata}")
            if rtype in ['SPF', 'DKIM', 'DMARC']:
                print(f"  {records.get(f'{rtype}_Commentary')}")