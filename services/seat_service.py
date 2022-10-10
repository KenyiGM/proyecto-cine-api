from sqlalchemy.orm import Session
from models.seat import Seat
from schemas.seat_schema import SeatCreate, SeatUpdate, SeatUpdateByIsActive

def get_seats(db:Session):
    return db.query(Seat).all()

def get_seat(db:Session, seat_id : int):
    return db.query(Seat).filter(Seat.id==seat_id).first()

def insert_seat(db:Session, seat:SeatCreate):
    new_seat = Seat(label = seat.label ,rows = seat.rows, columns = seat.columns)
    db.add(new_seat)
    db.commit()
    db.refresh(new_seat)
    return new_seat

def update_seat(db:Session, seat_id:int, seat:SeatUpdate):
    edit_seat = db.query(Seat).get(seat_id)
    edit_seat.label = seat.label
    edit_seat.rows = seat.rows
    edit_seat.columns = seat.columns
    edit_seat.update_at = seat.update_at
    db.commit()
    return edit_seat

def update_seat_by_is_active(db:Session, seat_id:int, seat:SeatUpdateByIsActive):
    edit_seat           = db.query(Seat).get(seat_id)
    edit_seat.is_active = seat.is_active
    edit_seat.update_at = seat.update_at
    db.commit()
    return edit_seat

def delete_seat(db:Session, seat_id:int):
    seat = db.query(Seat).get(seat_id)
    db.delete(seat)
    db.commit()
    return "delete"