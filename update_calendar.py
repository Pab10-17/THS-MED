from src.scraper import get_event_links

links = get_event_links()

print(f"Found {len(links)} event links")

for link in links:
    print(link)
