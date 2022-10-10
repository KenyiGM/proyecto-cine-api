from fastapi import APIRouter, Depends, HTTPException
from services.cinema_service import *
from databases.repository import get_db
from schemas.cinema_schema import Cinema
cinema = APIRouter()

@cinema.get('/cinema', response_model=list[Cinema])
async def get_all(db:Session = Depends(get_db)):
    return get_cinemas(db)

@cinema.get('/cinema/{cinema_id}', response_model=Cinema)
async def get_one(cinema_id:int , db:Session = Depends(get_db)):
    cinema = get_cinema(db, cinema_id)
    if cinema is None:
        raise HTTPException(status_code=404, detail="cinema not found")
    return cinema

@cinema.post('/cinema', response_model=Cinema)
async def insert_one(cinema:CinemaCreate, db:Session = Depends(get_db)):
    return insert_cinema(db, cinema)

@cinema.put('/cinema/{cinema_id}', response_model=Cinema)
async def update_one(cinema_id:int, cinema:CinemaUpdate, db:Session = Depends(get_db)):
    return update_cinema(db, cinema_id, cinema) 

@cinema.put('/cinema/{cinema_id}/is_active', response_model=Cinema)
async def update_one_by_is_active(cinema_id:int, cinema:CinemaUpdateByIsActive, db:Session = Depends(get_db)):
    return update_cinema_by_is_active(db, cinema_id, cinema)

@cinema.delete('/cinema/{cinema_id}')
async def delete_one(cinema_id:int, db:Session = Depends(get_db)):
    return delete_cinema(db, cinema_id)