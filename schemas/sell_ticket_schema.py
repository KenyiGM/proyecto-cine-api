from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.detail_sell_ticket_schema import Detail_sell_ticket

class Sell_ticketBase(BaseModel):
    is_pay_card : bool 
    client_id   : int
    employee_id : int

class Sell_ticketCreate(Sell_ticketBase):
    create_at   : date = date.today()

class Sell_ticketUpdate(Sell_ticketBase):
    total       : float
    pay         : float
    update_at : date = date.today()

class Sell_ticketFinish(Sell_ticketBase):
    is_active : bool = False
    is_paid : bool = True
    finish_at : date = date.today()

class Sell_ticket(Sell_ticketBase or Sell_ticketFinish):
    id : int
    detail_sell_ticket : list[Detail_sell_ticket] = []
    class Config:
        orm_mode = True