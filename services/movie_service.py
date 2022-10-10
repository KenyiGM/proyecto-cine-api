from sqlalchemy.orm import Session
from models.movie import Movie
from schemas.movie_schema import MovieCreate, MovieUpdate, MovieUpdateByIsActive

def get_movies(db:Session):
    return db.query(Movie).all()

def get_movie(db:Session, movie_id : int):
    return db.query(Movie).filter(Movie.id==movie_id).first()

def get_movie_by_name(db:Session, movie_name: str):
    return db.query(Movie).filter(Movie.name==movie_name).first()

def insert_movie(db:Session, movie:MovieCreate):
    new_movie = Movie(name = movie.name, description = movie.description, duration = movie.duration, director = movie.director, cast = movie.cast, quality_id = movie.quality_id)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

def update_movie(db:Session, movie_id:int, movie:MovieUpdate):
    edit_movie = db.query(Movie).get(movie_id)
    edit_movie.name = movie.name
    edit_movie.description = movie.description
    edit_movie.duration = movie.duration
    edit_movie.director = movie.director
    edit_movie.cast = movie.cast
    edit_movie.quality_id = movie.quality_id
    edit_movie.update_at = movie.update_at
    db.commit()
    return edit_movie

def update_movie_by_is_active(db:Session, movie_id:int, movie:MovieUpdateByIsActive):
    edit_movie           = db.query(Movie).get(movie_id)
    edit_movie.is_active = movie.is_active
    edit_movie.update_at = movie.update_at
    db.commit()
    return edit_movie

def delete_movie(db:Session, movie_id:int):
    movie = db.query(Movie).get(movie_id)
    db.delete(movie)
    db.commit()
    return "delete"