from sqlalchemy.orm import Session
from models.user import User_type
from schemas.user_type_schema import User_typeCreate, User_typeUpdate, User_typeUpdateByIsActive

def get_user_types(db:Session):
    return db.query(User_type).all()

def get_user_type(db:Session, user_type_id : int):
    return db.query(User_type).filter(User_type.id==user_type_id).first()

def insert_user_type(db:Session, user_type:User_typeCreate):
    new_user_type = User_type(type = user_type.type, is_view = user_type.is_view, is_write = user_type.is_write, is_edit = user_type.is_edit, is_delete = user_type.is_delete)
    db.add(new_user_type)
    db.commit()
    db.refresh(new_user_type)
    return new_user_type

def update_user_type(db:Session, user_type_id:int, user_type:User_typeUpdate):
    edit_user_type = db.query(User_type).get(user_type_id)
    edit_user_type.type = user_type.type
    edit_user_type.is_view = user_type.is_view
    edit_user_type.is_write = user_type.is_write
    edit_user_type.is_edit = user_type.is_edit
    edit_user_type.is_delete = user_type.is_delete
    edit_user_type.update_at = user_type.update_at
    db.commit()
    return edit_user_type

def update_user_type_by_is_active(db:Session, user_type_id:int, user_type:User_typeUpdateByIsActive):
    edit_user_type           = db.query(User_type).get(user_type_id)
    edit_user_type.is_active = user_type.is_active
    edit_user_type.update_at = user_type.update_at
    db.commit()
    return edit_user_type

def delete_user_type(db:Session, user_type_id:int):
    user_type = db.query(User_type).get(user_type_id)
    db.delete(user)
    db.commit()
    return "delete"