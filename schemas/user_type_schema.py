from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.user_schema import User

class UserBase(BaseModel):
    type : str
    is_view : bool
    is_write : bool
    is_edit : bool
    is_delete : bool

class UserCreate(UserBase):
    create_at : date = date.today()

class UserUpdate(UserBase):
    update_at : date = date.today()

class UserUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class User(UserBase or UserUpdateByIsActive):
    id          : int
    user : list[User] = []
    class Config:
        orm_mode = True