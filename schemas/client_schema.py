from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.sell_ticket_schema import Sell_ticket
from schemas.sell_food_schema import Sell_food

class ClientBase(BaseModel):
    firstname : str
    lastname : Optional[str]
    years_old : Optional[int]
    indentity_number : Optional[str]
    user_id : int

class ClientCreate(ClientBase):
    create_at : date = date.today()

class ClientUpdate(ClientBase):
    update_at : date = date.today()

class ClientUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Client(ClientBase or ClientUpdateByIsActive):
    id          : int
    sell_ticket : list[Sell_ticket] = [] 
    sell_food   : list[Sell_food]   = []
    class Config:
        orm_mode = True