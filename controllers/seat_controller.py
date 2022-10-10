from fastapi import APIRouter, Depends, HTTPException
from services.seat_service import *
from databases.repository import get_db
from schemas.seat_schema import Seat

seat = APIRouter()

@seat.get('/seat', response_model=list[Seat])
async def get_all(db:Session = Depends(get_db)):
    return get_seats(db)

@seat.get('/seat/{seat_id}', response_model=Seat)
async def get_one(seat_id:int , db:Session = Depends(get_db)):
    seat = get_seat(db, seat_id)
    if seat is None:
        raise HTTPException(status_code=404, detail="seat not found")
    return seat

@seat.post('/seat', response_model=Seat)
async def insert_one(seat:SeatCreate, db:Session = Depends(get_db)):
    return insert_seat(db, seat)

@seat.put('/seat/{seat_id}', response_model=Seat)
async def update_one(seat_id:int, seat:SeatUpdate, db:Session = Depends(get_db)):
    return update_seat(db, seat_id, seat)

@seat.put('/seat/{seat_id}/is_active', response_model=Seat)
async def update_one_by_is_active(seat_id:int, seat:SeatUpdateByIsActive, db:Session = Depends(get_db)):
    return update_seat_by_is_active(db, seat_id, seat)

@seat.delete('/seat/{seat_id}')
async def delete_one(seat_id:int, db:Session = Depends(get_db)):
    return delete_seat(db, seat_id)