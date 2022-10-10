from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.employee_schema import Employee
from schemas.client_schema import Client

class UserBase(BaseModel):
    username : str
    password : str
    user_type_id : int

class UserCreate(UserBase):
    create_at : date = date.today()

class UserUpdate(UserBase):
    update_at : date = date.today()

class UserFinish(BaseModel):
    is_active : bool = False
    finish_at : date = date.today()

class User(UserBase or UserFinish):
    id          : int
    client : list[Client] = []
    employee : list[Employee] = []
    class Config:
        orm_mode = True