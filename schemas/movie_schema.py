from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.function_schema import Function

class MovieBase(BaseModel):
    name        : str
    description : Optinal[str]
    duration    : float
    director    : Optional[str]
    cast        : Optional[str]
    quality_id  : int

class MovieCreate(MovieBase):
    create_at : date = date.today()

class MovieUpdate(MovieBase):
    update_at : date = date.today()

class MovieUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Movie(MovieBase or MovieUpdateByIsActive):
    id          : int
    function    : list[Function] = []
    class Config:
        orm_mode = True