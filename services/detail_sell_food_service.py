from sqlalchemy.orm import Session
from models.detail_sell_food import Detail_sell_food
from schemas.detail_sell_food_schema import Detail_sell_foodCreate, Detail_sell_foodUpdate, Detail_sell_foodUpdateByIsActive

def get_details_sell_foods(db:Session):
    return db.query(Detail_sell_food).all()

def get_detail_sell_food(db:Session, detail_sell_food_id : int):
    return db.query(Detail_sell_food).filter(Detail_sell_food.id==detail_sell_food_id).first()

def insert_detail_sell_food(db:Session, detail_sell_food:Detail_sell_foodCreate):
    new_detail_sell_food = Detail_sell_food(quantity = detail_sell_food.quantity, subtotal = detail_sell_food.subtotal, sell_food_id = detail_sell_food.sell_food_id, food_id = detail_sell_food.food_id)
    db.add(new_detail_sell_food)
    db.commit()
    db.refresh(new_detail_sell_food)
    return new_detail_sell_food

def update_detail_sell_food(db:Session, detail_sell_food_id:int, detail_sell_food:detail_sell_foodUpdate):
    edit_detail_sell_food = db.query(Detail_sell_food).get(detail_sell_food_id)
    edit_detail_sell_food.quantity = detail_sell_food.quantity
    edit_detail_sell_food.subtotal = detail_sell_food.subtotal
    edit_detail_sell_food.sell_food_id = detail_sell_food.sell_food_id
    edit_detail_sell_food.food_id = detail_sell_food.food_id
    edit_detail_sell_food.update_at = detail_sell_food.update_at
    db.commit()
    return edit_detail_sell_food

def update_detail_sell_food_by_is_active(db:Session, detail_sell_food_id:int, detail_sell_food:detail_sell_foodUpdateByIsActive):
    edit_detail_sell_food           = db.query(Detail_sell_food).get(detail_sell_food_id)
    edit_detail_sell_food.is_active = detail_sell_food.is_active
    edit_detail_sell_food.update_at = detail_sell_food.update_at
    db.commit()
    return edit_detail_sell_food

def delete_detail_sell_food(db:Session, detail_sell_food_id:int):
    detail_sell_food = db.query(Detail_sell_food).get(detail_sell_food_id)
    db.delete(detail_sell_food)
    db.commit()
    return "delete"