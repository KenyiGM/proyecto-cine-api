from sqlalchemy.orm import Session
from models.ticket import Ticket
from schemas.ticket_schema import TicketCreate, TicketUpdate, TicketFinish

def get_tickets(db:Session):
    return db.query(Ticket).all()

def get_ticket(db:Session, ticket_id : int):
    return db.query(Ticket).filter(Ticket.id==ticket_id).first()

def insert_ticket(db:Session, ticket:TicketCreate):
    new_ticket = Ticket(expire = ticket.expire)
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def update_ticket(db:Session, ticket_id:int, ticket:TicketUpdate):
    edit_ticket = db.query(Ticket).get(ticket_id)
    edit_ticket.expire = ticket.expire
    edit_ticket.update_at = ticket.update_at
    db.commit()
    return edit_ticket

def update_ticket_is_finish(db:Session, ticket_id:int, ticket:TicketFinish):
    edit_ticket           = db.query(Ticket).get(ticket_id)
    edit_ticket.is_active = ticket.is_active
    edit_ticket.expire = ticket.expire
    edit_ticket.finish_at = ticket.finish_at
    db.commit()
    return edit_ticket

def delete_ticket(db:Session, ticket_id:int):
    ticket = db.query(Ticket).get(ticket_id)
    db.delete(ticket)
    db.commit()
    return "delete"