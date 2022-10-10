from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.detail_sell_ticket_schema import Detail_sell_ticket

class Room_seatBase(BaseModel):
    row     : str
    column  : str
    room_id : int
    seat_id : int

class Room_seatCreate(Room_seatBase):
    create_at : date = date.today()

class Room_seatUpdate(Room_seatBase):
    update_at : date = date.today()

class Room_seatUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Room_seatUpdateByIsOccupied(BaseModel):
    is_occupied : bool = False
    update_at : date = date.today()

class Room_seat(Room_seatBase or Room_seatUpdateByIsActive or Room_seatUpdateByIsOccupied):
    id     : int
    detail_sell_ticket   : list[Detail_sell_ticket] = []
    class Config:
        orm_mode = True