from fastapi import APIRouter, Depends, HTTPException
from services.movie_service import *
from databases.repository import get_db
from schemas.movie_schema import Movie

movie = APIRouter()

@movie.get('/movie', response_model=list[Movie])
async def get_all(db:Session = Depends(get_db)):
    return get_movies(db)

@movie.get('/movie/{movie_id}', response_model=Movie)
async def get_one(movie_id:int , db:Session = Depends(get_db)):
    movie = get_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="movie not found")
    return movie

@movie.get('/movie/{movie_id}/name', response_model=Movie)
async def get_one_by_name(movie_name:str , db:Session = Depends(get_db)):
    movie = get_movie_by_name(db, movie_name)
    if movie is None:
        raise HTTPException(status_code=404, detail="movie not found")
    return movie

@movie.post('/movie', response_model=Movie)
async def insert_one(movie:MovieCreate, db:Session = Depends(get_db)):
    return insert_movie(db, movie)

@movie.put('/movie/{movie_id}', response_model=Movie)
async def update_one(movie_id:int, movie:MovieUpdate, db:Session = Depends(get_db)):
    return update_movie(db, movie_id, movie)

@movie.put('/movie/{movie_id}/is_active', response_model=Movie)
async def update_one_by_is_active(movie_id:int, movie:MovieUpdateByIsActive, db:Session = Depends(get_db)):
    return update_movie_by_is_active(db, movie_id, movie)

@movie.delete('/movie/{movie_id}')
async def delete_one(movie_id:int, db:Session = Depends(get_db)):
    return delete_movie(db, movie_id)