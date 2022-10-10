from fastapi import APIRouter, Depends, HTTPException
from services.food_service import *
from databases.repository import get_db
from schemas.food_schema import Food

food = APIRouter()

@food.get('/food', response_model=list[Food])
async def get_all(db:Session = Depends(get_db)):
    return get_foods(db)

@food.get('/food/{food_id}', response_model=Food)
async def get_one(food_id:int , db:Session = Depends(get_db)):
    food = get_food(db, food_id)
    if food is None:
        raise HTTPException(status_code=404, detail="food not found")
    return food

@food.post('/food', response_model=Food)
async def insert_one(food:FoodCreate, db:Session = Depends(get_db)):
    return insert_food(db, food)

@food.put('/food/{food_id}', response_model=Food)
async def update_one(food_id:int, food:FoodUpdate, db:Session = Depends(get_db)):
    return update_food(db, food_id, food)

@food.put('/food/{food_id}/is_active', response_model=Food)
async def update_one_by_is_active(food_id:int, food:FoodUpdateByIsActive, db:Session = Depends(get_db)):
    return update_food_by_is_active(db, food_id, food)

@food.delete('/food/{food_id}')
async def delete_one(food_id:int, db:Session = Depends(get_db)):
    return delete_food(db, food_id)