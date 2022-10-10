from sqlalchemy.orm import Session

from models.country import Country
from schemas.country_schema import CountryCreate, CountryUpdate, CountryUpdateByIsActive

def get_countries(db:Session):
    return db.query(Country).all()

def get_country(db:Session, country_id : int):
    return db.query(Country).filter(Country.id==country_id).first()

def insert_country(db:Session, country:CountryCreate):
    new_country = Country(name = country.name)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def update_country(db:Session, country_id:int, country:CountryUpdate):
    edit_country = db.query(Country).get(country_id)
    edit_country.name = country.name
    edit_country.update_at = country.update_at
    db.commit()
    return edit_country

def update_country_by_is_active(db:Session, country_id:int, country:CountryUpdateByIsActive):
    edit_country           = db.query(Country).get(country_id)
    edit_country.is_active = country.is_active
    edit_country.update_at = country.update_at
    db.commit()
    return edit_country

def delete_country(db:Session, country_id:int):
    country = db.query(Country).get(country_id)
    db.delete(country)
    db.commit()
    return "delete"