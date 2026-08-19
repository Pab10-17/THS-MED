from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event


def build_calendar(events):
    cal = Calendar()

    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    for item in events:
        for date in item["dates"]:

            event = Event()

            event.add("summary", item["title"])
            event.add("description", item["description"])
            event.add("url", item["url"])

            dt = parse(date, dayfirst=True)

            event.add("dtstart", dt.date())
            event.add("dtend", dt.date())

            event.add("dtstamp", datetime.utcnow())

            cal.add_component(event)

    return cal
