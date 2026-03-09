from __future__ import annotations

from app.application.ports.stock_repo import StockRepository
from app.application.ports.user_repo import UserRepository
from app.application.ports.watchlist_repo import WatchlistRepository
from app.domain.models import Stock


class AddWatchItem:
    def __init__(self, users: UserRepository, stocks: StockRepository, watchlist: WatchlistRepository):
        self.users = users
        self.stocks = stocks
        self.watchlist = watchlist

    def execute(self, user_id: int, stock_id: int) -> None:
        if not self.users.get(user_id):
            raise ValueError("User not found")
        if not self.stocks.get(stock_id):
            raise ValueError("Stock not found")
        self.watchlist.add_item(user_id=user_id, stock_id=stock_id)


class GetWatchlist:
    def __init__(self, users: UserRepository, watchlist: WatchlistRepository):
        self.users = users
        self.watchlist = watchlist

    def execute(self, user_id: int) -> list[Stock]:
        if not self.users.get(user_id):
            raise ValueError("User not found")
        return self.watchlist.list_stocks(user_id=user_id)
