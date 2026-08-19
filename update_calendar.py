import requests
import re

url = "https://www.tottenhamhotspurstadium.com/events/1075568/jay-z"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30,
)

response.raise_for_status()

html = response.text

patterns = [
    "4 September",
    "September",
    "Friday",
    "2026",
    "19:00",
    "Doors",
    "Kick",
]

for pattern in patterns:
    print(f"\n===== {pattern} =====")

    for match in re.finditer(pattern, html, re.IGNORECASE):
        start = max(0, match.start() - 200)
        end = min(len(html), match.end() + 200)

        print(html[start:end])
        print("-" * 80)
