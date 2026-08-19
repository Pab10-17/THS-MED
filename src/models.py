from dataclasses import dataclass
from typing import Optional


@dataclass
class Event:
    title: str
    date: str

    start_time: Optional[str] = None
    end_time: Optional[str] = None

    category: Optional[str] = None

    description: Optional[str] = None

    location: Optional[str] = "Tottenham Hotspur Stadium"

    url: Optional[str] = None

    image: Optional[str] = None
