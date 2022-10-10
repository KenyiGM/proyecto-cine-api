from fastapi import APIRouter, Depends, HTTPException
from services.ticket_service import *
from databases.repository import get_db
from schemas.ticket_schema import Ticket

ticket = APIRouter()

@ticket.get('/ticket', response_model=list[Ticket])
async def get_all(db:Session = Depends(get_db)):
    return get_tickets(db)

@ticket.get('/ticket/{ticket_id}', response_model=Ticket)
async def get_one(ticket_id:int , db:Session = Depends(get_db)):
    ticket = get_ticket(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="ticket not found")
    return ticket

@ticket.post('/ticket', response_model=Ticket)
async def insert_one(ticket:TicketCreate, db:Session = Depends(get_db)):
    return insert_ticket(db, ticket)

@ticket.put('/ticket/{ticket_id}', response_model=Ticket)
async def update_one(ticket_id:int, ticket:TicketUpdate, db:Session = Depends(get_db)):
    return update_ticket(db, ticket_id, ticket)

@ticket.put('/ticket/{ticket_id}/is_finish', response_model=Ticket)
async def update_one_is_finish(ticket_id:int, ticket:TicketFinish, db:Session = Depends(get_db)):
    return update_ticket_is_finish(db, ticket_id, ticket)

@ticket.delete('/ticket/{ticket_id}')
async def delete_one(ticket_id:int, db:Session = Depends(get_db)):
    return delete_ticket(db, ticket_id)