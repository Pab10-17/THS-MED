from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event
import hashlib


def build_calendar(events):
    cal = Calendar()

    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    # Sort by date
    events.sort(key=lambda e: parse(e["dates"][0], dayfirst=True))

    for item in events:
        for date in item["dates"]:
            event = Event()

            dt = parse(date, dayfirst=True)

            # Stable UID
            uid = hashlib.md5(
                f"{item['title']}-{date}".encode("utf-8")
            ).hexdigest() + "@ths-med"

            event.add("uid", uid)
            event.add("summary", item["title"])
            event.add("description", item["description"])
            event.add("url", item["url"])
            event.add("dtstart", dt.date())
            event.add("dtend", dt.date())
            event.add("dtstamp", datetime.utcnow())

            cal.add_component(event)

    return cal
