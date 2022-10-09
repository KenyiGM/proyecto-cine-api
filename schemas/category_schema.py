from datetime import date
from typing import Optional
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name       : str
    
class CategoryCreate(CategoryBase):
    create_at : date = date.today()

class CategoryUpdate(CategoryBase):
    update_at : date = date.today()

class CategoryUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class Category(CategoryBase or CategoryUpdateByIsActive):
    id          : int
    class Config:
        orm_mode = True