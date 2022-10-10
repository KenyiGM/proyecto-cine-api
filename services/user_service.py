from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserCreate, UserUpdate, UserFinish

def get_users(db:Session):
    return db.query(User).all()

def get_user(db:Session, user_id : int):
    return db.query(User).filter(User.id==user_id).first()

def get_user_by_username(db:Session, user_username : str):
    return db.query(User).filter(User.username==user_username).first()

def insert_user(db:Session, user:UserCreate):
    new_user = User(username = user.username, password = user.password, user_type_id = user.user_type_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db:Session, user_id:int, user:UserUpdate):
    edit_user = db.query(User).get(user_id)
    edit_user.expire = user.expire
    edit_user.update_at = user.update_at
    db.commit()
    return edit_user

def update_user_is_finish(db:Session, user_id:int, user:UserFinish):
    edit_user           = db.query(User).get(user_id)
    edit_user.is_active = user.is_active
    edit_user.expire = user.expire
    edit_user.finish_at = user.finish_at
    db.commit()
    return edit_user

def delete_user(db:Session, user_id:int):
    user = db.query(User).get(user_id)
    db.delete(user)
    db.commit()
    return "delete"