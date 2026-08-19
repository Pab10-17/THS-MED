from bs4 import BeautifulSoup


def get_meta_content(soup: BeautifulSoup, attribute: str, value: str):
    tag = soup.find("meta", attrs={attribute: value})
    if tag:
        return tag.get("content")
    return None


def parse_event(soup):
    return {
        "title": get_meta_content(soup, "property", "og:title"),
        "description": get_meta_content(soup, "property", "og:description"),
        "image": get_meta_content(soup, "property", "og:image"),
    }
