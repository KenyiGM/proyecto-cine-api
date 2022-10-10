from sqlalchemy.orm import Session
from models.sell_ticket import Sell_ticket
from schemas.sell_ticket_schema import Sell_ticketCreate, Sell_ticketUpdate, Sell_ticketFinish

def get_sell_tickets(db:Session):
    return db.query(Sell_ticket).all()

def get_sell_ticket(db:Session, sell_ticket_id : int):
    return db.query(Sell_ticket).filter(Sell_ticket.id==sell_ticket_id).first()

def insert_sell_ticket(db:Session, sell_ticket:Sell_ticketCreate):
    new_sell_ticket = sell_ticket(is_pay_card = sell_ticket.is_pay_card, client_id = sell_ticket.client_id, employee_id = sell_ticket.employee_id)
    db.add(new_sell_ticket)
    db.commit()
    db.refresh(new_sell_ticket)
    return new_sell_ticket

def update_sell_ticket(db:Session, sell_ticket_id:int, sell_ticket:Sell_ticketUpdate):
    edit_sell_ticket = db.query(Sell_ticket).get(sell_ticket_id)
    edit_sell_ticket.is_pay_card = sell_ticket.is_pay_card
    edit_sell_ticket.client_id = sell_ticket.client_id
    edit_sell_ticket.employee_id = sell_ticket.employee_id
    edit_sell_ticket.total = sell_ticket.total
    edit_sell_ticket.pay = sell_ticket.pay
    edit_sell_ticket.update_at = sell_ticket.update_at
    db.commit()
    return edit_sell_ticket

def update_sell_ticket_is_finish(db:Session, sell_ticket_id:int, sell_ticket:Sell_ticketFinish):
    edit_sell_ticket           = db.query(Sell_ticket).get(sell_ticket_id)
    edit_sell_ticket.is_active = sell_ticket.is_active
    edit_sell_ticket.is_paid   = sell_ticket.is_paid
    edit_sell_ticket.finish_at = sell_ticket.finish_at
    db.commit()
    return edit_sell_ticket

def delete_sell_ticket(db:Session, sell_ticket_id:int):
    sell_ticket = db.query(Sell_ticket).get(sell_ticket_id)
    db.delete(sell_ticket)
    db.commit()
    return "delete"