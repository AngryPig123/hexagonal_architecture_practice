from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: str = Field(min_length=3, max_length=120)


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class StockCreate(BaseModel):
    symbol: str = Field(min_length=1, max_length=16)
    name: str = Field(min_length=1, max_length=80)


class StockOut(BaseModel):
    id: int
    symbol: str
    name: str


class ArticleCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    source: str = Field(min_length=1, max_length=80)
    url: str = Field(min_length=5, max_length=500)
    published_at: datetime


class ArticleOut(BaseModel):
    id: int
    title: str
    source: str
    url: str
    published_at: datetime


class WatchItemAdd(BaseModel):
    stock_id: int


class BriefingOut(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: datetime
