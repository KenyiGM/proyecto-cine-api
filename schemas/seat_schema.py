from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.room_seat_schema import Room_seat

class SeatBase(BaseModel):
    label : str
    rows  : int
    columns : int

class SeatCreate(SeatBase):
    create_at : date = date.today()

class SeatUpdate(SeatBase):
    update_at : date = date.today()

class SeatUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Seat(SeatBase or SeatUpdateByIsActive):
    id          : int
    room_seat : list[Room_seat] = []
    class Config:
        orm_mode = True