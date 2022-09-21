from datetime import date
from typing import Optional
from pydantic import BaseModel

class Detail_sell_foodBase(BaseModel):
    name        : str
    price       : float
    quantity    : int  
    category_id : int

class Detail_sell_foodCreate(Detail_sell_foodBase):
    create_at : date = date.today()

class Detail_sell_foodUpdate(Detail_sell_foodBase):
    update_at : date = date.today()

class Detail_sell_foodUpdateByIsActive(BaseModel):
    is_active : bool = True

class Detail_sell_food(Detail_sell_foodBase or Detail_sell_foodUpdateByIsActive):
    id : int
    class Config:
        orm_mode = True