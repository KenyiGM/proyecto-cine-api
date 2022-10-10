from fastapi import APIRouter, Depends, HTTPException
from services.user_type_service import *
from databases.repository import get_db
from schemas.user_type_schema import User_type

user_type = APIRouter()

@user_type.get('/user_type', response_model=list[User_type])
async def get_all(db:Session = Depends(get_db)):
    return get_user_types(db)

@user_type.get('/user_type/{user_type_id}', response_model=User_type)
async def get_one(user_type_id:int , db:Session = Depends(get_db)):
    user_type = get_user_type(db, user_type_id)
    if user_type is None:
        raise HTTPException(status_code=404, detail="user_type not found")
    return user_type

@user_type.post('/user_type', response_model=User_type)
async def insert_one(user_type:User_typeCreate, db:Session = Depends(get_db)):
    return insert_user_type(db, user_type)

@user_type.put('/user_type/{user_type_id}', response_model=User_type)
async def update_one(user_type_id:int, user_type=User_typeUpdate, db:Session = Depends(get_db)):
    return update_user_type(db, user_type_id, user_type)

@user_type.put('/user_type/{user_type_id}/is_active', response_model=User_type)
async def update_one_by_is_active(user_type_id:int, user_type:User_typeUpdateByIsActive, db:Session = Depends(get_db)):
    return update_user_type_by_is_active(db, user_type_id, user_type)

@user_type.delete('/user_type/{user_type_id}')
async def delete_one(user_type_id:int, db:Session = Depends(get_db)):
    return delete_user_type(db, user_type_id)