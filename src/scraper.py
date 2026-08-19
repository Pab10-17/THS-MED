import requests

BASE_URL = "https://www.tottenhamhotspurstadium.com"

API_URL = (
    "https://api.tottenhamhotspurstadium.com/content/"
    "thstadium/text/EN?limit=100&offset=0&tagExpression=(%22event:2026%22)"
)


def get_event_links():
    response = requests.get(
        API_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    links = []

    for item in data.get("content", []):
        title = item.get("title", "")
        slug = item.get("titleUrlSegment", "")

        # Skip invalid items
        if not slug:
            continue

        # Skip duplicate copy events
        if slug.startswith("copy-"):
            continue

        url = f"{BASE_URL}/events/{item['id']}/{slug}"

        print(title)
        print(url)

        links.append(url)

    return links
