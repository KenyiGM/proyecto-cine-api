from fastapi import APIRouter, Depends, HTTPException
from services.sell_food_service import *
from databases.repository import get_db
from schemas.sell_food_schema import Sell_food

sell_food = APIRouter()

@sell_food.get('/sell_food', response_model=list[Sell_food])
async def get_all(db:Session = Depends(get_db)):
    return get_sell_foods(db)

@sell_food.get('/sell_food/{sell_food_id}', response_model=Sell_food)
async def get_one(sell_food_id:int , db:Session = Depends(get_db)):
    sell_food = get_sell_food(db, sell_food_id)
    if sell_food is None:
        raise HTTPException(status_code=404, detail="sell_food not found")
    return sell_food

@sell_food.post('/sell_food', response_model=Sell_food)
async def insert_one(sell_food:Sell_foodCreate, db:Session = Depends(get_db)):
    return insert_sell_food(db, sell_food)

@sell_food.put('/sell_food/{sell_food_id}', response_model=Sell_food)
async def update_one(sell_food_id:int, sell_food:Sell_foodUpdate, db:Session = Depends(get_db)):
    return update_sell_food(db, sell_food_id, sell_food)

@sell_food.put('/sell_food/{sell_food_id}/is_finish', response_model=Sell_food)
async def update_one_is_finish(sell_food_id:int, sell_food:Sell_foodFinish, db:Session = Depends(get_db)):
    return update_sell_food_is_finish(db, sell_food_id, sell_food)

@sell_food.delete('/sell_food/{sell_food_id}')
async def delete_one(sell_food_id:int, db:Session = Depends(get_db)):
    return delete_sell_food(db, sell_food_id)