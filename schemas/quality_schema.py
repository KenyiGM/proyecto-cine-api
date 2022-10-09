from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.movie_schema import Movie

class QualityBase(BaseModel):
    name : str

class QualityCreate(QualityBase):
    create_at : date = date.today()

class QualityUpdate(QualityBase):
    update_at : date = date.today()

class QualityUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Quality(QualityBase or QualityUpdateByIsActive):
    id          : int
    movie : list[Movie] = []
    class Config:
        orm_mode = True