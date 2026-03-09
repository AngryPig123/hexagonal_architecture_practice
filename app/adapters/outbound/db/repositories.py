from __future__ import annotations

from datetime import datetime
from typing import Optional, List as tlist

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.application.ports.article_repo import ArticleRepository
from app.application.ports.briefing_repo import BriefingRepository
from app.application.ports.stock_repo import StockRepository
from app.application.ports.user_repo import UserRepository
from app.application.ports.watchlist_repo import WatchlistRepository
from app.domain.models import User, Stock, Article, Briefing
from .orm_models import UserORM, StockORM, ArticleORM, BriefingORM, WatchlistItemORM


def _to_user(o: UserORM) -> User:
    return User(id=o.id, name=o.name, email=o.email)


def _to_stock(o: StockORM) -> Stock:
    return Stock(id=o.id, symbol=o.symbol, name=o.name)


def _to_article(o: ArticleORM) -> Article:
    return Article(id=o.id, title=o.title, source=o.source, url=o.url, published_at=o.published_at)


def _to_briefing(o: BriefingORM) -> Briefing:
    return Briefing(id=o.id, user_id=o.user_id, content=o.content, created_at=o.created_at)


class SqlUserRepo(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, email: str) -> User:
        obj = UserORM(name=name, email=email)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return _to_user(obj)

    def get(self, user_id: int) -> Optional[User]:
        obj = self.db.get(UserORM, user_id)
        return _to_user(obj) if obj else None


class SqlStockRepo(StockRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, symbol: str, name: str) -> Stock:
        obj = StockORM(symbol=symbol, name=name)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return _to_stock(obj)

    def list(self) -> list[Stock]:
        rows = self.db.execute(select(StockORM).order_by(StockORM.id.desc())).scalars().all()
        return [_to_stock(r) for r in rows]

    def get(self, stock_id: int) -> Optional[Stock]:
        obj = self.db.get(StockORM, stock_id)
        return _to_stock(obj) if obj else None


class SqlArticleRepo(ArticleRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, source: str, url: str, published_at: datetime) -> Article:
        obj = ArticleORM(title=title, source=source, url=url, published_at=published_at)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return _to_article(obj)

    def list(self) -> list[Article]:
        rows = self.db.execute(select(ArticleORM).order_by(ArticleORM.published_at.desc())).scalars().all()
        return [_to_article(r) for r in rows]

    def list_recent(self, since: datetime) -> list[Article]:
        stmt = select(ArticleORM).where(ArticleORM.published_at >= since).order_by(ArticleORM.published_at.desc())
        rows = self.db.execute(stmt).scalars().all()
        return [_to_article(r) for r in rows]


class SqlWatchlistRepo(WatchlistRepository):
    def __init__(self, db):
        self.db = db

    def add_item(self, user_id: int, stock_id: int) -> None:
        obj = WatchlistItemORM(user_id=user_id, stock_id=stock_id)
        self.db.add(obj)
        self.db.commit()

    def list_stocks(self, user_id: int) -> tlist[Stock]:
        stmt = (
            select(StockORM)
            .join(WatchlistItemORM, WatchlistItemORM.stock_id == StockORM.id)
            .where(WatchlistItemORM.user_id == user_id)
            .order_by(WatchlistItemORM.created_at.desc())
        )
        rows = self.db.execute(stmt).scalars().all()
        return [_to_stock(r) for r in rows]


class SqlBriefingRepo(BriefingRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: int, content: str) -> Briefing:
        obj = BriefingORM(user_id=user_id, content=content)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return _to_briefing(obj)

    def get(self, briefing_id: int) -> Optional[Briefing]:
        obj = self.db.get(BriefingORM, briefing_id)
        return _to_briefing(obj) if obj else None
