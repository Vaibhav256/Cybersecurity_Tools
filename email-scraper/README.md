# Email Scraper

This is a simple Python-based email scraper that extracts email addresses from the webpages of a specified URL. It recursively scrapes links found on each page and collects emails as it goes. It can be very useful for attacks like Social Engineering.

## Features
- Recursively scrapes all URLs on a webpage.
- Extracts email addresses using regular expressions.
- Stops after scraping a maximum of 100 URLs (to avoid infinite loops).
- Handles connection errors and missing schemas gracefully.

## Requirements
- Python 3.x
- `requests` - For sending HTTP requests.
- `beautifulsoup4` - For parsing HTML pages.
- `lxml` - For faster HTML parsing.

## Installation

1. Clone the repository:

	git clone https://github.com/Vaibhav256/Cybersecurity_Tools/email-scraper

2. Change the directory:

	cd email-scraper

3. Install the requirements:

	pip install -r requirements.txt

## Usage

1. Open the directory:

	cd /path to/email-scraper

2. Run the Tool:

	python email_scraper.py

3. Enter the Full URL like: https://google.com 

4. Scraped emails will be printed..