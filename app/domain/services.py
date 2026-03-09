from __future__ import annotations
from datetime import datetime, timedelta
from typing import Iterable

from .models import Stock, Article

class BriefingComposer:
    """
    도메인 서비스: 브리핑 문구 생성 규칙을 여기에 둔다.
    (나중에 LLM 요약을 붙일 때도 여기의 인터페이스를 유지하고 교체 가능)
    """

    def compose(self, stocks: Iterable[Stock], articles: Iterable[Article]) -> str:
        stock_list = list(stocks)
        article_list = list(articles)

        lines = []
        lines.append(f"[Briefing] watched_stocks={len(stock_list)}, recent_articles={len(article_list)}")

        if stock_list:
            lines.append("- Watchlist")
            for s in stock_list:
                lines.append(f"  - {s.symbol} ({s.name})")

        if article_list:
            lines.append("- Articles")
            for a in article_list[:10]:
                dt = a.published_at.strftime("%Y-%m-%d %H:%M")
                lines.append(f"  - [{dt}] {a.title} ({a.source})")

        if not stock_list and not article_list:
            lines.append("- No data yet.")

        return "\n".join(lines)

def default_recent_window() -> datetime:
    return datetime.utcnow() - timedelta(days=3)