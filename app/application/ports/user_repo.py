from __future__ import annotations
from typing import Protocol, Optional
from app.domain.models import User


class UserRepository(Protocol):
    def create(self, name: str, email: str) -> User: ...

    def get(self, user_id: int) -> Optional[User]: ...
