from fastapi import APIRouter, Depends, HTTPException
from services.client_service import *
from databases.repository import get_db
from schemas.client_schema import Client

client = APIRouter()

@client.get('/client', response_model=list[Client])
async def get_all(db:Session = Depends(get_db)):
    return get_categories(db)

@client.get('/client/{client_id}', response_model=Client)
async def get_one(client_id:int , db:Session = Depends(get_db)):
    client = get_client(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return client

@client.get('/client/{client_firstname}/firstname', response_model=Client)
async def get_one_by_firstname(client_firstname:str , db:Session = Depends(get_db)):
    client = get_client_by_firstname(db, client_firstname)
    if client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return client

@client.post('/client', response_model=Client)
async def insert_one(client:ClientCreate, db:Session = Depends(get_db)):
    return insert_client(db, client)

@client.put('/client/{client_id}', response_model=Client)
async def update_one(client_id:int, client:ClientUpdate, db:Session = Depends(get_db)):
    return update_client(db, client_id, client) 

@client.put('/client/{client_id}/is_active', response_model=Client)
async def update_one_by_is_active(client_id:int, client:clientUpdateByIsActive, db:Session = Depends(get_db)):
    return update_client_by_is_active(db, client_id, client)

@client.delete('/client/{client_id}')
async def delete_one(client_id:int, db:Session = Depends(get_db)):
    return delete_client(db, client_id)