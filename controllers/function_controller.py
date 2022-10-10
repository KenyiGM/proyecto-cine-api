from fastapi import APIRouter, Depends, HTTPException
from services.function_service import *
from databases.repository import get_db
from schemas.function_schema import Function

function = APIRouter()

@function.get('/function', response_model=list[Function])
async def get_all(db:Session = Depends(get_db)):
    return get_functions(db)

@function.get('/function/{function_id}', response_model=Function)
async def get_one(function_id:int , db:Session = Depends(get_db)):
    function = get_function(db, function_id)
    if function is None:
        raise HTTPException(status_code=404, detail="function not found")
    return function

@function.post('/function', response_model=Function)
async def insert_one(function:FunctionCreate, db:Session = Depends(get_db)):
    return insert_function(db, function)

@function.put('/function/{function_id}', response_model=Function)
async def update_one(function_id:int, function:FunctionUpdate, db:Session = Depends(get_db)):
    return update_function(db, function_id, function)

@function.put('/function/{function_id}/is_active', response_model=Function)
async def update_one_by_is_active(function_id:int, function:FunctionUpdateByIsActive, db:Session = Depends(get_db)):
    return update_function_by_is_active(db, function_id, function)

@function.delete('/function/{function_id}')
async def delete_one(function_id:int, db:Session = Depends(get_db)):
    return delete_function(db, function_id)