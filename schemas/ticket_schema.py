from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.detail_sell_ticket_schema import Detail_sell_ticket

class TicketBase(BaseModel):
    expire : date

class TicketCreate(TicketBase):
    create_at : date = date.today()

class TicketUpdate(TicketBase):
    update_at : date = date.today()

class TicketFinish(BaseModel):
    is_active : bool = False
    expire : date = date.today()
    finish_at : date = date.today()

class Ticket(TicketBase or TicketFinish):
    id          : int
    detail_sell_ticket : list[Detail_sell_ticket] = []
    class Config:
        orm_mode = True