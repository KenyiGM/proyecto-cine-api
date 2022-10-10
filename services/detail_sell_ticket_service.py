from sqlalchemy.orm import Session
from models.detail_sell_ticket import Detail_sell_ticket
from schemas.detail_sell_ticket_schema import Detail_sell_ticketCreate, Detail_sell_ticketUpdate, Detail_sell_ticketUpdateByIsActive

def get_details_sell_tickets(db:Session):
    return db.query(Detail_sell_ticket).all()

def get_detail_sell_ticket(db:Session, detail_sell_ticket_id : int):
    return db.query(Detail_sell_ticket).filter(Detail_sell_ticket.id==detail_sell_ticket_id).first()

def insert_detail_sell_ticket(db:Session, detail_sell_ticket:Detail_sell_ticketCreate):
    new_detail_sell_ticket = Detail_sell_ticket(quantity = detail_sell_ticket.quantity, subtotal = detail_sell_ticket.subtotal, room_seat_id = detail_sell_ticket.room_seat_id , sell_ticket_id = detail_sell_ticket.sell_ticket_id, ticket_id = detail_sell_ticket.ticket_id)
    db.add(new_detail_sell_ticket)
    db.commit()
    db.refresh(new_detail_sell_ticket)
    return new_detail_sell_ticket

def update_detail_sell_ticket(db:Session, detail_sell_ticket_id:int, detail_sell_ticket:Detail_sell_ticketUpdate):
    edit_detail_sell_ticket = db.query(Detail_sell_ticket).get(detail_sell_ticket_id)
    edit_detail_sell_ticket.quantity = detail_sell_ticket.quantity
    edit_detail_sell_ticket.subtotal = detail_sell_ticket.subtotal
    edit_detail_sell_ticket.room_seat_id = detail_sell_ticket.room_seat_id
    edit_detail_sell_ticket.sell_food_id = detail_sell_ticket.sell_ticket_id
    edit_detail_sell_ticket.ticket_id = detail_sell_ticket.ticket_id
    edit_detail_sell_ticket.update_at = detail_sell_ticket.update_at
    db.commit()
    return edit_detail_sell_ticket

def update_detail_sell_ticket_by_is_active(db:Session, detail_sell_ticket_id:int, detail_sell_ticket:Detail_sell_ticketUpdateByIsActive):
    edit_detail_sell_ticket           = db.query(Detail_sell_ticket).get(detail_sell_ticket_id)
    edit_detail_sell_ticket.is_active = detail_sell_ticket.is_active
    edit_detail_sell_ticket.update_at = detail_sell_ticket.update_at
    db.commit()
    return edit_detail_sell_ticket

def delete_detail_sell_ticket(db:Session, detail_sell_ticket_id:int):
    detail_sell_ticket = db.query(Detail_sell_ticket).get(detail_sell_ticket_id)
    db.delete(detail_sell_ticket)
    db.commit()
    return "delete"