from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.outbound.db.repositories import SqlUserRepo
from app.application.usecases.user_uc import CreateUser, GetUser
from app.adapters.inbound.http.schemas import UserCreate, UserOut
from app.adapters.outbound.db.session import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserOut, status_code=201)
def create_user(body: UserCreate, db: Session = Depends(get_session)):
    try:
        uc = CreateUser(SqlUserRepo(db))
        return uc.execute(name=body.name, email=body.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_session)):
    try:
        uc = GetUser(SqlUserRepo(db))
        return uc.execute(user_id=user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

