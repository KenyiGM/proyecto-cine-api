from fastapi import APIRouter, Depends, HTTPException
from services.detail_sell_food_service import *
from databases.repository import get_db
from schemas.detail_sell_food_schema import Detail_sell_food

detail_sell_food = APIRouter()

@detail_sell_food.get('/detail_sell_food', response_model=list[Detail_sell_food])
async def get_all(db:Session = Depends(get_db)):
    return get_details_sell_foods(db)

@detail_sell_food.get('/detail_sell_food/{detail_sell_food_id}', response_model=Detail_sell_food)
async def get_one(detail_sell_food_id:int , db:Session = Depends(get_db)):
    detail_sell_food = get_detail_sell_food(db, detail_sell_food_id)
    if detail_sell_food is None:
        raise HTTPException(status_code=404, detail="detail_sell_food not found")
    return detail_sell_food

@detail_sell_food.post('/detail_sell_food', response_model=Detail_sell_food)
async def insert_one(detail_sell_food:Detail_sell_foodCreate, db:Session = Depends(get_db)):
    return insert_detail_sell_food(db, detail_sell_food)

@detail_sell_food.put('/detail_sell_food/{detail_sell_food_id}', response_model=Detail_sell_food)
async def update_one(detail_sell_food_id:int, detail_sell_food:Detail_sell_foodUpdate, db:Session = Depends(get_db)):
    return update_detail_sell_food(db, detail_sell_food_id, detail_sell_food) 

@detail_sell_food.put('/detail_sell_food/{detail_sell_food_id}/is_active', response_model=Detail_sell_food)
async def update_one_by_is_active(detail_sell_food_id:int, detail_sell_food:Detail_sell_foodUpdateByIsActive, db:Session = Depends(get_db)):
    return update_detail_sell_food_by_is_active(db, detail_sell_food_id, detail_sell_food)

@detail_sell_food.delete('/detail_sell_food/{detail_sell_food_id}')
async def delete_one(detail_sell_food_id:int, db:Session = Depends(get_db)):
    return delete_detail_sell_food(db, detail_sell_food_id)