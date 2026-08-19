import requests

url = "https://www.tottenhamhotspurstadium.com/events"

print("Downloading:", url)

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("Status Code:", response.status_code)
print("Downloaded", len(response.text), "characters")
