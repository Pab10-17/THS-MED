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

print("Title:")
print(soup.title.text)

print("\nJSON-LD scripts found:")

scripts = soup.find_all("script", type="application/ld+json")

print(len(scripts))

for i, script in enumerate(scripts):
    print(f"\n--- JSON Script {i+1} ---")
    print(script.text[:1000])
