import requests
from bs4 import BeautifulSoup

url = "https://www.tottenhamhotspurstadium.com/events/1075568/jay-z"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30,
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Print every element that has a class containing "date"
for tag in soup.find_all(True):
    classes = tag.get("class") or []
    if any("date" in c.lower() for c in classes):
        print("-" * 80)
        print(tag.name)
        print(classes)
        print(tag.get_text(" ", strip=True))
