from sqlalchemy.orm import Session
from app.adapters.outbound.db.session import get_session

def db_session() -> Session:
    return next(get_session())