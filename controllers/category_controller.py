from fastapi import APIRouter, Depends, HTTPException
from services.category_service import *
from databases.repository import get_db
from schemas.category_schema import Category

category = APIRouter()

@category.get('/category', response_model=list[Category])
async def get_all(db:Session = Depends(get_db)):
    return get_categories(db)

@category.get('/category/{category_id}', response_model=Category)
async def get_one(category_id:int , db:Session = Depends(get_db)):
    category = get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return category

@category.post('/category', response_model=Category)
async def insert_one(category:CategoryCreate, db:Session = Depends(get_db)):
    return insert_category(db, category)

@category.put('/category/{category_id}', response_model=Category)
async def update_one(category_id:int, category:CategoryUpdate, db:Session = Depends(get_db)):
    return update_category(db, category_id, category) 

@category.put('/category/{category_id}/is_active', response_model=Category)
async def update_one_by_is_active(category_id:int, category:CategoryUpdateByIsActive, db:Session = Depends(get_db)):
    return update_category_by_is_active(db, category_id, category)

@category.delete('/category/{category_id}')
async def delete_one(category_id:int, db:Session = Depends(get_db)):
    return delete_category(db, category_id)