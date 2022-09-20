from datetime import date
from pydantic import BaseModel
from schemas.city_schema import City

class CountryBase(BaseModel):
    name : str

class CountryCreate(CountryBase):
    create_at : date = date.today()

class CountryUpdate(CountryBase):
    update_at : date = date.today()

class CountryUpdateByIsActive(BaseModel):
    is_active : bool = True

class Country(CountryBase or CountryUpdateByIsActive):
    id   : int
    city : list[City] = []
    class Config:
        orm_mode = True