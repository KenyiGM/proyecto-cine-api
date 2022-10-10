from fastapi import APIRouter, Depends, HTTPException
from services.user_service import *
from databases.repository import get_db
from schemas.user_schema import User

user = APIRouter()

@user.get('/user', response_model=list[User])
async def get_all(db:Session = Depends(get_db)):
    return get_users(db)

@user.get('/user/{user_id}', response_model=User)
async def get_one(user_id:int , db:Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@user.get('/user/{user_id}/username', response_model=User)
async def get_one_by_username(user_username:str , db:Session = Depends(get_db)):
    user = get_user_by_username(db, user_username)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@user.post('/user', response_model=User)
async def insert_one(user:UserCreate, db:Session = Depends(get_db)):
    return insert_user(db, user)

@user.put('/user/{user_id}', response_model=User)
async def update_one(user_id:int, user=UserUpdate, db:Session = Depends(get_db)):
    return update_user(db, user_id, user)

@user.put('/user/{user_id}/is_finish', response_model=User)
async def update_one_is_finish(user_id:int, user:UserFinish, db:Session = Depends(get_db)):
    return update_user_is_finish(db, user_id, user)

@user.delete('/user/{user_id}')
async def delete_one(user_id:int, db:Session = Depends(get_db)):
    return delete_user(db, user_id)