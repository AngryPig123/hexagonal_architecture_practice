from __future__ import annotations
from datetime import datetime
from app.application.ports.article_repo import ArticleRepository
from app.domain.models import Article

class CreateArticle:
    def __init__(self, repo: ArticleRepository):
        self.repo = repo

    def execute(self, title: str, source: str, url: str, published_at: datetime) -> Article:
        return self.repo.create(title=title, source=source, url=url, published_at=published_at)

class ListArticles:
    def __init__(self, repo: ArticleRepository):
        self.repo = repo

    def execute(self) -> list[Article]:
        return self.repo.list()