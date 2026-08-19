import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.tottenhamhotspurstadium.com"


def get_events_page():
    response = requests.get(
        f"{BASE_URL}/events",
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )

    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


def get_event_links():
    soup = get_events_page()

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/events/" in href:
            if href.startswith("/"):
                href = BASE_URL + href

            if href not in links:
                links.append(href)

    return links
