from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event
import hashlib


def get_icon(title):
    t = title.lower()

    if "spurs" in t:
        return "⚽"
    elif "nfl" in t:
        return "🏈"
    elif "saracens" in t or "rugby" in t:
        return "🏉"
    elif "tyson" in t or "boxing" in t:
        return "🥊"
    else:
        return "🎤"


def build_calendar(events):
    cal = Calendar()
    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")
    cal.add("X-WR-CALNAME", "THS-MED")
    cal.add("X-WR-CALDESC", "Tottenham Hotspur Stadium Events")
    cal.add("X-WR-TIMEZONE", "Europe/London")

    events.sort(key=lambda e: parse(e["start"]))

    for item in events:
        event = Event()

        start = parse(item["start"])
        end = parse(item["end"])

        uid = hashlib.md5(
            f"{item['title']}-{item['start']}".encode("utf-8")
        ).hexdigest() + "@ths-med"

        description = (
            f"{item['description']}\n\n"
            f"📍 Tottenham Hotspur Stadium\n"
            f"📅 {start.strftime('%A %d %B %Y')}\n"
            f"🕒 {start.strftime('%H:%M')} - {end.strftime('%H:%M')}\n\n"
            f"More information:\n{item['url']}"
        )

        event.add("uid", uid)
        event.add("summary", f"{get_icon(item['title'])} {item['title']}")
        event.add("description", description)
        event.add(
            "location",
            "Tottenham Hotspur Stadium, 782 High Road, London N17 0BX",
        )
        event.add("url", item["url"])
        event.add("dtstart", start)
        event.add("dtend", end)
        event.add("dtstamp", datetime.utcnow())

        cal.add("method", "PUBLISH")
        cal.add_component(event)

    return cal
