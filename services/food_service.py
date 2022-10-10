from sqlalchemy.orm import Session
from models.food import Food
from schemas.food_schema import FoodCreate, FoodUpdate, FoodUpdateByIsActive

def get_foods(db:Session):
    return db.query(Food).all()

def get_food(db:Session, food_id : int):
    return db.query(Food).filter(Food.id==food_id).first()

def insert_food(db:Session, food:FoodCreate):
    new_food = Food(name = food.name, price = food.price, quantity = food.quantity, category_id = food.category_id)
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food

def update_food(db:Session, food_id:int, food:FoodUpdate):
    edit_food = db.query(Food).get(food_id)
    edit_food.name = food.name
    edit_food.price = food.price
    edit_food.quantity = food.quantity
    edit_food.category_id = food.category_id
    edit_food.update_at = food.update_at
    db.commit()
    return edit_food

def update_food_by_is_active(db:Session, food_id:int, food:FoodUpdateByIsActive):
    edit_food           = db.query(Food).get(food_id)
    edit_food.is_active = food.is_active
    edit_food.update_at = food.update_at
    db.commit()
    return edit_food

def delete_food(db:Session, food_id:int):
    food = db.query(Food).get(food_id)
    db.delete(food)
    db.commit()
    return "delete"