import requests

from src.calendar_builder import build_calendar

API_URL = (
    "https://api.tottenhamhotspurstadium.com/content/"
    "thstadium/text/EN?limit=100&offset=0&tagExpression=(%22event:2026%22)"
)

response = requests.get(
    API_URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30,
)

response.raise_for_status()

data = response.json()

events = []

for item in data["content"]:

    metadata = item.get("metadata", {})

    start = metadata.get("EventStartDate")
    end = metadata.get("EventEndDate")

    if not start or not end:
        continue

    slug = item.get("titleUrlSegment", "")

    url = (
        f"https://www.tottenhamhotspurstadium.com/events/"
        f"{item['id']}/{slug}"
    )

    events.append(
        {
            "title": item["title"],
            "description": item.get("description", ""),
            "start": start,
            "end": end,
            "url": url,
        }
    )

print(f"Found {len(events)} events")

calendar = build_calendar(events)

with open("THS-MED.ics", "wb") as f:
    f.write(calendar.to_ical())

print("Calendar created successfully")
