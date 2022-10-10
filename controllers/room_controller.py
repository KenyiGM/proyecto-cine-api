from fastapi import APIRouter, Depends, HTTPException
from services.room_service import *
from databases.repository import get_db
from schemas.room_schema import Room

room = APIRouter()

@room.get('/room', response_model=list[Room])
async def get_all(db:Session = Depends(get_db)):
    return get_rooms(db)

@room.get('/room/{room_id}', response_model=Room)
async def get_one(room_id:int , db:Session = Depends(get_db)):
    room = get_room(db, room_id)
    if room is None:
        raise HTTPException(status_code=404, detail="room not found")
    return room

@room.post('/room', response_model=Room)
async def insert_one(room:RoomCreate, db:Session = Depends(get_db)):
    return insert_room(db, room)

@room.put('/room/{room_id}', response_model=room)
async def update_one(room_id:int, room:RoomUpdate, db:Session = Depends(get_db)):
    return update_room(db, room_id, room)

@room.put('/room/{room_id}/is_active', response_model=Room)
async def update_one_by_is_active(room_id:int, room:roomUpdateByIsActive, db:Session = Depends(get_db)):
    return update_room_by_is_active(db, room_id, room)

@room.delete('/room/{room_id}')
async def delete_one(room_id:int, db:Session = Depends(get_db)):
    return delete_room(db, room_id)