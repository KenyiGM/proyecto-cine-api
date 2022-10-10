from sqlalchemy.orm import Session
from models.category import Category
from schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryUpdateByIsActive

def get_categories(db:Session):
    return db.query(Category).all()

def get_category(db:Session, category_id : int):
    return db.query(Category).filter(Category.id==category_id).first()

def insert_category(db:Session, category:CategoryCreate):
    new_category = Category(name = category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db:Session, category_id:int, category:CategoryUpdate):
    edit_category = db.query(category).get(category_id)
    edit_category.name       = category.name
    edit_category.update_at  = category.update_at
    db.commit()
    return edit_category

def update_category_by_is_active(db:Session, category_id:int, category:CategoryUpdateByIsActive):
    edit_category           = db.query(Category).get(category_id)
    edit_category.is_active = category.is_active
    edit_category.update_at  = category.update_at
    db.commit()
    return edit_category

def delete_category(db:Session, category_id:int):
    category = db.query(Category).get(category_id)
    db.delete(category)
    db.commit()
    return "delete"