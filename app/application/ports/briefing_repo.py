from __future__ import annotations
from typing import Protocol, Optional
from app.domain.models import Briefing

class BriefingRepository(Protocol):
    def create(self, user_id: int, content: str) -> Briefing: ...
    def get(self, briefing_id: int) -> Optional[Briefing]: ...