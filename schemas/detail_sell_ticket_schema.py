from datetime import date
from typing import Optional
from pydantic import BaseModel

class Detail_sell_ticketBase(BaseModel):
    quantity     : int
    subtotal     : float 
    room_seat_id : int
    sell_ticket_id : int
    ticket_id : id

class Detail_sell_ticketCreate(Detail_sell_ticketBase):
    create_at : date = date.today()

class Detail_sell_ticketUpdate(Detail_sell_ticketBase):
    update_at : date = date.today()

class Detail_sell_ticketUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Detail_sell_ticket(Detail_sell_ticketBase or Detail_sell_ticketUpdateByIsActive):
    id          : int
    class Config:
        orm_mode = True