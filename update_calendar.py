import requests

url = "https://www.tottenhamhotspurstadium.com/events/1075568/jay-z"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30,
)

response.raise_for_status()

text = response.text

print(text[:5000])
