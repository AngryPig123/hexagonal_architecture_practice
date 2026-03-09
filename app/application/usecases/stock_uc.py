from __future__ import annotations
from app.application.ports.stock_repo import StockRepository
from app.domain.models import Stock


class CreateStock:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def execute(self, symbol: str, name: str) -> Stock:
        return self.repo.create(symbol=symbol, name=name)


class ListStocks:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def execute(self) -> list[Stock]:
        return self.repo.list()
