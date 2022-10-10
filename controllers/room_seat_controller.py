from fastapi import APIRouter, Depends, HTTPException
from services.room_seat_service import *
from databases.repository import get_db
from schemas.room_seat_schema import Room_seat

room_seat = APIRouter()

@room_seat.get('/room_seat', response_model=list[Room_seat])
async def get_all(db:Session = Depends(get_db)):
    return get_room_seats(db)

@room_seat.get('/room_seat/{room_seat_id}', response_model=Room_seat)
async def get_one(room_seat_id:int , db:Session = Depends(get_db)):
    room_seat = get_room_seat(db, room_seat_id)
    if room_seat is None:
        raise HTTPException(status_code=404, detail="room_seat not found")
    return room_seat

@room_seat.post('/room_seat', response_model=Room_seat)
async def insert_one(room_seat:Room_seatCreate, db:Session = Depends(get_db)):
    return insert_room_seat(db, room_seat)

@room_seat.put('/room_seat/{room_seat_id}', response_model=Room_seat)
async def update_one(room_seat_id:int, room_seat:Room_seatUpdate, db:Session = Depends(get_db)):
    return update_room_seat(db, room_seat_id, room_seat)

@room_seat.put('/room_seat/{room_seat_id}/is_active', response_model=Room_seat)
async def update_one_by_is_active(room_seat_id:int, room_seat:Room_seatUpdateByIsActive, db:Session = Depends(get_db)):
    return update_room_seat_by_is_active(db, room_seat_id, room_seat)

@room_seat.delete('/room_seat/{room_seat_id}')
async def delete_one(room_seat_id:int, db:Session = Depends(get_db)):
    return delete_room_seat(db, room_seat_id)