from datetime import datetime

from app.application.ports.article_repo import ArticleRepository
from app.application.ports.briefing_repo import BriefingRepository
from app.application.ports.user_repo import UserRepository
from app.application.ports.watchlist_repo import WatchlistRepository
from app.domain.models import Briefing
from app.domain.services import BriefingComposer, default_recent_window


class GenerateBriefing:
    def __init__(
            self,
            users: UserRepository,
            articles: ArticleRepository,
            watchlist: WatchlistRepository,
            briefings: BriefingRepository,
            composer: BriefingComposer
    ):
        self.users = users
        self.articles = articles
        self.watchlist = watchlist
        self.briefings = briefings
        self.composer = composer

    def execute(self, user_id: int, since: datetime | None = None) -> Briefing:
        if not self.users.get(user_id):
            raise ValueError("User not found")

        if since is None:
            since = default_recent_window()

        stocks = self.watchlist.list_stocks(user_id)
        recent_articles = self.articles.list_recent(since=since)

        content = self.composer.compose(stocks=stocks, articles=recent_articles)
        return self.briefings.create(user_id=user_id, content=content)


class GetBriefing:
    def __init__(self, repo: BriefingRepository):
        self.repo = repo

    def execute(self, briefing_id:int) -> Briefing:
        briefing = self.repo.get(briefing_id)
        if not briefing:
            raise ValueError("Briefing not found")
        return briefing

