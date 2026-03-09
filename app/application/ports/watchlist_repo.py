from __future__ import annotations
from typing import Protocol, List as tlist
from app.domain.models import Stock

class WatchlistRepository(Protocol):
    def add_item(self, user_id: int, stock_id: int) -> None: ...
    def list_stocks(self, user_id: int) -> tlist[Stock]: ...