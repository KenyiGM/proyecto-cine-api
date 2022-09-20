from fastapi import APIRouter, Depends
from services.country_service import * 
from databases.repository import get_db
from schemas.country_schema import Country

country = APIRouter()

@country.get('/country', response_model=list[Country])
async def get_all(db:Session = Depends(get_db)):
    return get_countries(db)

@country.get('/country/{country_id}', response_model=Country)
async def get_one(country_id:int , db:Session = Depends(get_db)):
    return get_country(db, country_id)

@country.post('/country', response_model=Country)
async def insert_one(country:CountryCreate, db:Session = Depends(get_db)):
    return insert_country(db, country)

@country.put('/country/{country_id}', response_model=Country)
async def update_one(country_id:int, country:CountryUpdate, db:Session = Depends(get_db)):
    return update_country(db, country_id, country) 

@country.put('/country/{country_id}/is_active', response_model=Country)
async def update_one_by_is_active(country_id:int, country:CountryUpdateByIsActive, db:Session = Depends(get_db)):
    return update_country_by_is_active(db, country_id, country)

@country.delete('/country/{country_id}')
async def delete_one(country_id:int, db:Session = Depends(get_db)):
    return delete_country(db, country_id)