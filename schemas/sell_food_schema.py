from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.detail_sell_food_schema import Detail_sell_food

class Sell_foodBase(BaseModel):
    is_pay_card : bool 
    client_id   : int
    employee_id : int

class Sell_foodCreate(Sell_foodBase):
    create_at   : date = date.today()

class Sell_foodUpdate(Sell_foodBase):
    total       : float
    pay         : float
    update_at : date = date.today()

class Sell_foodFinish(Sell_foodBase):
    is_active : bool = False
    is_paid : bool = True
    finish_at : date = date.today()

class Sell_food(Sell_foodBase or Sell_foodFinish):
    id : int
    detail_sell_food : list[Detail_sell_food] = []
    class Config:
        orm_mode = True