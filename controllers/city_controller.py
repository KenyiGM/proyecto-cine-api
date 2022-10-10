from fastapi import APIRouter, Depends, HTTPException
from services.city_service import *
from databases.repository import get_db
from schemas.city_schema import City

city = APIRouter()

@city.get('/city',  response_model=list[City])
async def get_all(db:Session = Depends(get_db)):
    return get_cities(db)

@city.get('/city/{city_id}', response_model=City)
async def get_one(city_id:int , db:Session = Depends(get_db)):
    city = get_city(db, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@city.post('/city', response_model=City)
async def insert_one(city:CityCreate, db:Session = Depends(get_db)):
    return insert_city(db, city)

@city.put('/city/{city_id}', response_model=City)
async def update_one(city_id:int, city:CityUpdate, db:Session = Depends(get_db)):
    return update_city(db, city_id, city) 

@city.put('/city/{city_id}/is_active', response_model=City)
async def update_one_by_is_active(city_id:int, city:CityUpdateByIsActive, db:Session = Depends(get_db)):
    return update_city_by_is_active(db, city_id, city)

@city.delete('/city/{city_id}')
async def delete_one(city_id:int, db:Session = Depends(get_db)):
    return delete_city(db, city_id)