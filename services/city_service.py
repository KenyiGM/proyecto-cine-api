from sqlalchemy.orm import Session
from models.city import City
from schemas.city_schema import CityCreate, CityUpdate, CityUpdateByIsActive

def get_cities(db:Session):
    return db.query(City).all()

def get_city(db:Session, city_id : int):
    return db.query(City).filter(City.id==city_id).first()

def insert_city(db:Session, city:CityCreate):
    new_city = City(name = city.name, country_id = city.country_id)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

def update_city(db:Session, city_id:int, city:CityUpdate):
    edit_city = db.query(City).get(city_id)
    edit_city.name       = city.name
    edit_city.country_id = city.country_id or edit_city.country_id
    edit_city.update_at  = city.update_at
    db.commit()
    return edit_city

def update_city_by_is_active(db:Session, city_id:int, city:CityUpdateByIsActive):
    edit_city           = db.query(City).get(city_id)
    edit_city.is_active = city.is_active
    db.commit()
    return edit_city

def delete_city(db:Session, city_id:int):
    city = db.query(City).get(city_id)
    db.delete(city)
    db.commit()
    return "delete"