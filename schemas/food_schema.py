from datetime import date
from typing import Optional
from pydantic import BaseModel

class FoodBase(BaseModel):
    name        : str
    price       : float
    quantity    : int  
    category_id : int

class FoodCreate(FoodBase):
    create_at : date = date.today()

class FoodUpdate(FoodBase):
    update_at : date = date.today()

class FoodUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Food(FoodBase or FoodUpdateByIsActive):
    id : int
    class Config:
        orm_mode = True