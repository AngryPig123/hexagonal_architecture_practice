from __future__ import annotations
from typing import Protocol, List as tlist
from datetime import datetime
from app.domain.models import Article


class ArticleRepository(Protocol):
    def create(self, title: str, source: str, url: str, published_at: datetime) -> Article: ...

    def list(self) -> tlist[Article]: ...

    def list_recent(self, since: datetime) -> tlist[Article]: ...
