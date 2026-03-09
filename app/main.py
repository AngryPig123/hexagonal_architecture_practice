from fastapi import FastAPI

from app.adapters.inbound.http.routers.users import router as users_router
from app.adapters.outbound.db.base import Base
from app.adapters.outbound.db.session import engine


def create_app() -> FastAPI:
    app = FastAPI(title="Stock Supporters Mini (Hexagonal)")

    # 학습용: 앱 시작 시 테이블 생성
    Base.metadata.create_all(bind=engine)

    app.include_router(users_router)

    return app


app = create_app()
