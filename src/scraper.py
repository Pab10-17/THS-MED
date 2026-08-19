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

    # Look at every event card
    for card in soup.select(".w-event-listing__item"):
        title = card.select_one(".w-event-listing__event-title")

        if title:
            print("Found:", title.get_text(strip=True))

        link = card.find("a", href=True)

        if link:
            href = link["href"]

            if href.startswith("/"):
                href = BASE_URL + href

            if href not in links:
                links.append(href)

    print(f"\nFound {len(links)} links:\n")

    for link in links:
        print(link)

    return links
