from sqlalchemy.orm import Session
from models.room_seat import Room_seat
from schemas.room_seat_schema import Room_seatCreate, Room_seatUpdate, Room_seatUpdateByIsActive, Room_seatUpdateByIsOccupied

def get_room_seats(db:Session):
    return db.query(Room_seat).all()

def get_room_seat(db:Session, room_seat_id : int):
    return db.query(Room_seat).filter(Room_seat.id==room_seat_id).first()

def insert_room_seat(db:Session, room_seat:Room_seatCreate):
    new_room_seat = Room_seat(row = room_seat.row, column = room_seat.column, room_id = room_seat.room_id, seat_id = room_seat.seat_id)
    db.add(new_room_seat)
    db.commit()
    db.refresh(new_room_seat)
    return new_room_seat

def update_room_seat(db:Session, room_seat_id:int, room_seat:Room_seatUpdate):
    edit_room_seat = db.query(Room_seat).get(room_seat_id)
    edit_room_seat.row = room_seat.row
    edit_room_seat.column = room_seat.column
    edit_room_seat.room_id = room_seat.room_id
    edit_room_seat.seat_id = room_seat.seat_id
    edit_room_seat.update_at = room_seat.update_at
    db.commit()
    return edit_room_seat

def update_room_seat_by_is_active(db:Session, room_seat_id:int, room_seat:room_seatUpdateByIsActive):
    edit_room_seat           = db.query(Room_seat).get(room_seat_id)
    edit_room_seat.is_active = room_seat.is_active
    edit_room_seat.update_at = room_seat.update_at
    db.commit()
    return edit_room_seat

def update_room_seat_by_is_occupied(db:Session, room_seat_id:int, room_seat:Room_seatUpdateByIsOccupied):
    edit_room_seat           = db.query(Room_seat).get(room_seat_id)
    edit_room_seat.is_occupied = room_seat.is_occupied
    edit_room_seat.update_at = room_seat.update_at
    db.commit()
    return edit_room_seat
    

def delete_room_seat(db:Session, room_seat_id:int):
    room_seat = db.query(Room_seat).get(room_seat_id)
    db.delete(room_seat)
    db.commit()
    return "delete"