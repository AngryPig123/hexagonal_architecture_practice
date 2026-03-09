from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str


@dataclass(frozen=True)
class Stock:
    id: int
    symbol: str
    name: str


@dataclass(frozen=True)
class Article:
    id: int
    title: str
    source: str
    url: str
    published_at: datetime


@dataclass(frozen=True)
class Briefing:
    id: int
    user_id: int
    content: str
    created_at: datetime
