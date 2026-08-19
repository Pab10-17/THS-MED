import requests

BASE_URL = "https://www.tottenhamhotspurstadium.com"
API_BASE = "https://api.tottenhamhotspurstadium.com/content/thstadium/text/EN"


def get_event_links():
    links = []
    seen = set()

    year = 2026

    while True:
        response = requests.get(
            f"{API_BASE}?limit=100&offset=0&tagExpression=(%22event:{year}%22)",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()
        events = data.get("content", [])

        if not events:
            break

        print(f"\n{year}: {len(events)} events")

        for item in events:
            slug = item.get("titleUrlSegment", "")

            if not slug or slug.startswith("copy-"):
                continue

            url = f"{BASE_URL}/events/{item['id']}/{slug}"

            if url not in seen:
                seen.add(url)
                links.append(url)

        year += 1

    print(f"\nFound {len(links)} unique events")

    return links
