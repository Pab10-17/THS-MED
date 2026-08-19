from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event
import hashlib


def build_calendar(events):
    cal = Calendar()

    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    # Sort by start date
    events.sort(key=lambda e: parse(e["start"]))

    for item in events:
        event = Event()

        start = parse(item["start"])
        end = parse(item["end"])

        uid = hashlib.md5(
            f"{item['title']}{item['start']}".encode("utf-8")
        ).hexdigest() + "@ths-med"

        event.add("uid", uid)
        event.add("summary", item["title"])
        event.add("description", item["description"])
        event.add("url", item["url"])
        event.add("dtstart", start)
        event.add("dtend", end)
        event.add("dtstamp", datetime.utcnow())

        cal.add_component(event)

    return cal
