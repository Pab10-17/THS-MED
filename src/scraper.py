import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.tottenhamhotspurstadium.com"


def get_events_page():
    """Download the main events page."""

    url = f"{BASE_URL}/events"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")
