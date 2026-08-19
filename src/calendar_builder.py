from datetime import datetime
from dateutil.parser import parse
from icalendar import Calendar, Event


def build_calendar(events):

    cal = Calendar()
    cal.add("prodid", "-//THS-MED//EN")
    cal.add("version", "2.0")

    for item in events:

        for event_date in item["dates"]:

            e = Event()

            e.add("summary", item["title"])
            e.add("description", item["description"])
            e.add("url", item["url"])

            dt = parse(event_date, dayfirst=True)

            e.add("dtstart", dt.date())
            e.add("dtend", dt.date())

            e.add("dtstamp", datetime.utcnow())

            cal.add_component(e)

    return cal
