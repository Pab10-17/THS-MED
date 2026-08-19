import requests
from bs4 import BeautifulSoup

from src.scraper import get_event_links
from src.parser import parse_event

links = get_event_links()

print(f"Found {len(links)} events\n")

for link in links:

    response = requests.get(
        link,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    event = parse_event(soup)

    print("=" * 80)
    print(event["title"])
    print(event["description"])
    print(event["image"])
    print(link)
