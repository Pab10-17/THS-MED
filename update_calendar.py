import requests
from bs4 import BeautifulSoup

from src.scraper import get_event_links
from src.parser import parse_event
from src.calendar_builder import build_calendar

events = []

for link in get_event_links():
    response = requests.get(
        link,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    event = parse_event(soup)
    event["url"] = link

    events.append(event)

calendar = build_calendar(events)

with open("THS-MED.ics", "wb") as f:
    f.write(calendar.to_ical())

print(f"Created calendar with {len(events)} events")
