from sqlalchemy.orm import Session
from models.sell_food import Sell_food
from schemas.sell_food_schema import Sell_foodCreate, Sell_foodUpdate, Sell_foodFinish

def get_sell_foods(db:Session):
    return db.query(Sell_food).all()

def get_sell_food(db:Session, sell_food_id : int):
    return db.query(Sell_food).filter(Sell_food.id==sell_food_id).first()

def insert_sell_food(db:Session, sell_food:Sell_foodCreate):
    new_sell_food = Sell_food(is_pay_card = sell_food.is_pay_card, client_id = sell_food.client_id, employee_id = sell_food.employee_id)
    db.add(new_sell_food)
    db.commit()
    db.refresh(new_sell_food)
    return new_sell_food

def update_sell_food(db:Session, sell_food_id:int, sell_food:Sell_foodUpdate):
    edit_sell_food = db.query(Sell_food).get(sell_food_id)
    edit_sell_food.is_pay_card = sell_food.is_pay_card
    edit_sell_food.client_id = sell_food.client_id
    edit_sell_food.employee_id = sell_food.employee_id
    edit_sell_food.total = sell_food.total
    edit_sell_food.pay = sell_food.pay
    edit_sell_food.update_at = sell_food.update_at
    db.commit()
    return edit_sell_food

def update_sell_food_is_finish(db:Session, sell_food_id:int, sell_food:Sell_foodFinish):
    edit_sell_food           = db.query(Sell_food).get(sell_food_id)
    edit_sell_food.is_active = sell_food.is_active
    edit_sell_food.is_paid   = sell_food.is_paid
    edit_sell_food.finish_at = sell_food.finish_at
    db.commit()
    return edit_sell_food

def delete_sell_food(db:Session, sell_food_id:int):
    sell_food = db.query(Sell_food).get(sell_food_id)
    db.delete(sell_food)
    db.commit()
    return "delete"