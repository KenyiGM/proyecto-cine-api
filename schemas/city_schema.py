from datetime import date
from typing import Optional
from pydantic import BaseModel

class CityBase(BaseModel):
    name       : str
    country_id : int
    
class CityCreate(CityBase):
    create_at : date = date.today()

class CityUpdate(CityBase):
    country_id: Optional[int]
    update_at : date = date.today()

class CityUpdateByIsActive(BaseModel):
    is_active : bool = True

class City(CityBase or CityUpdateByIsActive):
    id          : int
    class Config:
        orm_mode = True