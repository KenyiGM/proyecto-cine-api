from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.user_schema import User

class User_typeBase(BaseModel):
    type : str
    is_view : bool
    is_write : bool
    is_edit : bool
    is_delete : bool

class User_typeCreate(User_typeBase):
    create_at : date = date.today()

class User_typeUpdate(User_typeBase):
    update_at : date = date.today()

class User_typeUpdateByIsActive(BaseModel):
    is_active : bool = True
    update_at : date = date.today()

class User_type(User_typeBase or User_typeUpdateByIsActive):
    id          : int
    user : list[User] = []
    class Config:
        orm_mode = True