from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.sell_ticket_schema import Sell_ticket

class EmployeeBase(BaseModel):
    firstname : str
    lastname : str
    years_old : int
    birthday : date
    indentity_number : str
    address : str
    email   : str  
    start_date : date
    departure_date : Optional[date]
    user_id : int

class EmployeeCreate(EmployeeBase):
    create_at : date = date.today()

class EmployeeUpdate(EmployeeBase):
    update_at : date = date.today()

class EmployeeFinish(EmployeeBase):
    is_active : bool = False
    departure_date : date = date.today()
    finish_at : date = date.today()

class Employee(EmployeeBase or EmployeeFinish):
    id          : int
    sell_ticket : list[Sell_ticket] = []
    class Config:
        orm_mode = True