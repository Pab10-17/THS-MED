import re
from bs4 import BeautifulSoup


def get_meta_content(soup, attribute, value):
    tag = soup.find("meta", attrs={attribute: value})
    return tag.get("content") if tag else None


def parse_event(soup):

    title = get_meta_content(soup, "property", "og:title")
    description = get_meta_content(soup, "property", "og:description")
    image = get_meta_content(soup, "property", "og:image")

    dates = []

    for tag in soup.select(".w-key-info__date"):
        date = tag.get_text(" ", strip=True)

        if date not in dates:
            dates.append(date)

    year_match = re.search(r"20\d\d", description or "")
    year = year_match.group(0) if year_match else ""

    full_dates = [f"{d} {year}" for d in dates]

    return {
        "title": title,
        "description": description,
        "image": image,
        "dates": full_dates,
    }
