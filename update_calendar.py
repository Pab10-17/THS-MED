import time
import requests
from bs4 import BeautifulSoup

from src.scraper import get_event_links
from src.parser import parse_event
from src.calendar_builder import build_calendar

events = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for link in get_event_links():
    print(f"Fetching {link}")

    response = requests.get(
        link,
        headers=headers,
        timeout=30,
    )

    if response.status_code == 429:
        print("Rate limited - waiting 5 seconds...")
        time.sleep(5)

        response = requests.get(
            link,
            headers=headers,
            timeout=30,
        )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    event = parse_event(soup)
    event["url"] = link

    events.append(event)

    time.sleep(1)

calendar = build_calendar(events)

with open("THS-MED.ics", "wb") as f:
    f.write(calendar.to_ical())

print(f"\nCreated calendar with {len(events)} events")
