from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event
import hashlib


def get_icon(title):
    t = title.lower()

    if "spurs" in t:
        return "⚽"

    if "nfl" in t:
        return "🏈"

    if "saracens" in t:
        return "🏉"

    if "tyson" in t or "boxing" in t:
        return "🥊"

    return "🎤"


def build_calendar(events):
    cal = Calendar()

    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    events.sort(key=lambda e: parse(e["start"]))

    for item in events:
        event = Event()

        start = parse(item["start"])
        end = parse(item["end"])

        uid = hashlib.md5(
            f"{item['title']}{item['start']}".encode("utf-8")
        ).hexdigest() + "@ths-med"

        event.add("uid", uid)
        event.add("summary", f"{get_icon(item['title'])} {item['title']}")
        event.add("description", item["description"])
        event.add("location", "Tottenham Hotspur Stadium")
        event.add("url", item["url"])
        event.add("dtstart", start)
        event.add("dtend", end)
        event.add("dtstamp", datetime.utcnow())

        cal.add_component(event)

    return cal
