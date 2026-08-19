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

print("=== H1 ===")

for h1 in soup.find_all("h1"):
    print(h1.get_text(strip=True))

print("\n=== H2 ===")

for h2 in soup.find_all("h2"):
    print(h2.get_text(strip=True))

print("\n=== H3 ===")

for h3 in soup.find_all("h3"):
    print(h3.get_text(strip=True))
