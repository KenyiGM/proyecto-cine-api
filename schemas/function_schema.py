from datetime import date
from typing import Optional
from pydantic import BaseModel

class FunctionBase(BaseModel):
    start_time : float
    finish_time : float
    is_started : bool
    movie_id : int
    room_id : int

class FunctionCreate(FunctionBase):
    create_at : date = date.today()

class FunctionUpdate(FunctionBase):
    update_at : date = date.today()

class FunctionUpdateByIsActive(BaseModel):
    is_started : bool = True
    is_active : bool = True
    update_at : date = date.today()

class Function(FunctionBase or FunctionUpdateByIsActive):
    id          : int
    class Config:
        orm_mode = True