from sqlalchemy.orm import Session
from models.cinema import Cinema
from schemas.cinema_schema import CinemaCreate, CinemaUpdate, CinemaUpdateByIsActive

def get_cinemas(db:Session):
    return db.query(Cinema).all()

def get_cinema(db:Session, cinema_id : int):
    return db.query(Cinema).filter(Cinema.id==cinema_id).first()

def insert_cinema(db:Session, cinema:CinemaCreate):
    new_cinema = Cinema(name = cinema.name, address = cinema.address, city_id = cinema.city_id)
    db.add(new_cinema)
    db.commit()
    db.refresh(new_cinema)
    return new_cinema

def update_cinema(db:Session, cinema_id:int, cinema:CinemaUpdate):
    edit_cinema = db.query(Cinema).get(cinema_id)
    edit_cinema.name       = cinema.name
    edit_cinema.address       = cinema.address
    edit_cinema.city_id       = cinema.city_id
    edit_cinema.update_at  = cinema.update_at
    db.commit()
    return edit_cinema

def update_cinema_by_is_active(db:Session, cinema_id:int, cinema:CinemaUpdateByIsActive):
    edit_cinema           = db.query(Cinema).get(cinema_id)
    edit_cinema.is_active = cinema.is_active
    edit_cinema.update_at  = cinema.update_at
    db.commit()
    return edit_cinema

def delete_cinema(db:Session, cinema_id:int):
    cinema = db.query(Cinema).get(cinema_id)
    db.delete(cinema)
    db.commit()
    return "delete"