from sqlalchemy.orm import Session
from models.function import Function
from schemas.function_schema import FunctionCreate, FunctionUpdate, FunctionUpdateByIsActive

def get_functions(db:Session):
    return db.query(Function).all()

def get_function(db:Session, function_id : int):
    return db.query(Function).filter(Function.id==function_id).first()

def insert_function(db:Session, function:FunctionCreate):
    new_function = Function(name = function.name, price = function.price, quantity = function.quantity, category_id = function.category_id)
    db.add(new_function)
    db.commit()
    db.refresh(new_function)
    return new_function

def update_function(db:Session, function_id:int, function:FunctionUpdate):
    edit_function = db.query(Function).get(function_id)
    edit_function.start_time = function.start_time
    edit_function.finish_time = function.finish_time
    edit_function.is_started = function.is_started
    edit_function.movie_id = function.movie_id
    edit_function.room_id = function.room_id
    edit_function.update_at = function.update_at
    db.commit()
    return edit_function

def update_function_by_is_active(db:Session, function_id:int, function:FunctionUpdateByIsActive):
    edit_function           = db.query(Function).get(function_id)
    edit_function.is_active = function.is_active
    edit_function.is_started = function.is_started
    edit_function.update_at = function.update_at
    db.commit()
    return edit_function

def delete_function(db:Session, function_id:int):
    function = db.query(Function).get(function_id)
    db.delete(function)
    db.commit()
    return "delete"