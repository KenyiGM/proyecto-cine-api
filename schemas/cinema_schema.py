from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.room_schema import Room

class CinemaBase(BaseModel):
    name    : str
    address : str
    city_id : int
    
class CinemaCreate(CinemaBase):
    create_at : date = date.today()

class CinemaUpdate(CinemaBase):
    update_at : date = date.today()

class CinemaUpdateByIsActive(BaseModel):
    is_active : bool = True

class Cinema(CinemaBase or CinemaUpdateByIsActive):
    id     : int
    room   : list[Room] = []
    class Config:
        orm_mode = True