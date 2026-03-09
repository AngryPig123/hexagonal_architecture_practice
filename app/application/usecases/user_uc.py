from __future__ import annotations

from app.application.ports.user_repo import UserRepository
from app.domain.models import User


class CreateUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, name: str, email: str) -> User:
        return self.repo.create(name, email)


class GetUser:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: int) -> User:
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user
