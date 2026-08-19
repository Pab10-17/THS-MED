from datetime import datetime
from dateutil.parser import isoparse
from icalendar import Calendar, Event


def build_calendar(events):
    cal = Calendar()

    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    for item in events:

        event = Event()

        event.add("summary", item["title"])
        event.add("description", item["description"])

        if item.get("url"):
            event.add("url", item["url"])

        start = isoparse(item["start"])
        end = isoparse(item["end"])

        event.add("dtstart", start)
        event.add("dtend", end)

        event.add("dtstamp", datetime.utcnow())

        cal.add_component(event)

    return cal
