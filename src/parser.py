import re
from bs4 import BeautifulSoup


def get_meta_content(soup, attribute, value):
    tag = soup.find("meta", attrs={attribute: value})
    return tag.get("content") if tag else None


def parse_event(soup):
    title = get_meta_content(soup, "property", "og:title")
    description = get_meta_content(soup, "property", "og:description")
    image = get_meta_content(soup, "property", "og:image")

    year = None
    if description:
        match = re.search(r"(20\d{2})", description)
        if match:
            year = match.group(1)

    dates = []

    for tag in soup.select(".w-key-info__date"):
        day = tag.select_one(".w-key-info__date-day").get_text(strip=True)
        month = tag.select_one(".w-key-info__date-month").get_text(strip=True)

        date = f"{day} {month} {year}"

        if date not in dates:
            dates.append(date)

    return {
        "title": title,
        "description": description,
        "image": image,
        "dates": dates,
    }
