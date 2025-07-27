from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

user_url = input('[+] Enter Target URL To Scan: ').strip()
urls = deque([user_url])

scraped_urls = set()
emails = set()
count = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Filter out common non-HTTP schemes
invalid_schemes = ['javascript:', 'mailto:', 'tel:', '#']

try:
    while urls:
        count += 1
        if count >= 100:
            break

        url = urls.popleft()
        scraped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print(f'[{count}] Processing {url}')
        try:
            response = requests.get(url, headers=headers, timeout=10)
        except (requests.exceptions.RequestException, requests.exceptions.MissingSchema):
            continue

        # Extract and store emails
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a", href=True):
            href = anchor['href'].strip()

            # Skip invalid or JavaScript links
            if any(href.lower().startswith(scheme) for scheme in invalid_schemes):
                continue

            if href.startswith('/'):
                link = base_url + href
            elif href.startswith('http'):
                link = href
            else:
                link = urllib.parse.urljoin(path, href)

            if link not in urls and link not in scraped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print('[-] Interrupted. Closing!')

# Output found emails
for mail in sorted(emails):
    print("\n Gathered Emails : \n")
    print(mail)