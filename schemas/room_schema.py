from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.function_schema import Function
from schemas.room_seat_schema import Room_seat

class RoomBase(BaseModel):
    name      : str
    cinema_id : int
    
class RoomCreate(RoomBase):
    create_at : date = date.today()

class RoomUpdate(RoomBase):
    update_at : date = date.today()

class RoomUpdateByIsActive(BaseModel):
    is_active : bool = True

class Room(RoomBase or RoomUpdateByIsActive):
    id     : int
    function  : list[Function] = []
    room_seat : list[Room_seat] = []
    class Config:
        orm_mode = True