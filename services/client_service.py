from sqlalchemy.orm import Session
from models.client import Client
from schemas.client_schema import ClientCreate, ClientUpdate, ClientUpdateByIsActive

def get_clients(db:Session):
    return db.query(Client).all()

def get_client(db:Session, client_id : int):
    return db.query(Client).filter(Client.id==client_id).first()

def get_client_by_firstname(db:Session, client_firstname: str):
    return db.query(Client).filter(Client.firstname==client_firstname).first()

def insert_client(db:Session, client:ClientCreate):
    new_client = client(firstname = client.firstname, lastname = client.lastname, years_old = client.years_old, indentity_number = client.indentity_number, user_id = client.user_id)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def update_client(db:Session, client_id:int, client:ClientUpdate):
    edit_client = db.query(Client).get(client_id)
    edit_client.firstname = client.firstname
    edit_client.lastname = client.lastname
    edit_client.years_old = client.years_old
    edit_client.indentity_number = client.indentity_number
    edit_client.user_id = client.user_id
    edit_client.update_at  = client.update_at
    db.commit()
    return edit_client

def update_client_by_is_active(db:Session, client_id:int, client:ClientUpdateByIsActive):
    edit_client           = db.query(Client).get(client_id)
    edit_client.is_active = client.is_active
    edit_client.update_at  = client.update_at
    db.commit()
    return edit_client

def delete_client(db:Session, client_id:int):
    client = db.query(Client).get(client_id)
    db.delete(client)
    db.commit()
    return "delete"