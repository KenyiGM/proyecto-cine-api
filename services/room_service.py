from sqlalchemy.orm import Session
from models.room import Room
from schemas.room_schema import RoomCreate, RoomUpdate, RoomUpdateByIsActive

def get_rooms(db:Session):
    return db.query(Room).all()

def get_room(db:Session, room_id : int):
    return db.query(Room).filter(Room.id==room_id).first()

def insert_room(db:Session, room:RoomCreate):
    new_room = Room(name = room.name, cinema_id = room.cinema_id)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

def update_room(db:Session, room_id:int, room:RoomUpdate):
    edit_room = db.query(Room).get(room_id)
    edit_room.name = room.name
    edit_room.cinema_id = room.cinema_id
    edit_room.update_at = room.update_at
    db.commit()
    return edit_room

def update_room_by_is_active(db:Session, room_id:int, room:RoomUpdateByIsActive):
    edit_room           = db.query(Room).get(room_id)
    edit_room.is_active = room.is_active
    edit_room.update_at = room.update_at
    db.commit()
    return edit_room

def delete_room(db:Session, room_id:int):
    room = db.query(Room).get(room_id)
    db.delete(room)
    db.commit()
    return "delete"