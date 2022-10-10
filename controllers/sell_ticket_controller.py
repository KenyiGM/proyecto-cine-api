from fastapi import APIRouter, Depends, HTTPException
from services.sell_ticket_service import *
from databases.repository import get_db
from schemas.sell_ticket_schema import sell_ticket

sell_ticket = APIRouter()

@sell_ticket.get('/sell_ticket', response_model=list[Sell_ticket])
async def get_all(db:Session = Depends(get_db)):
    return get_sell_tickets(db)

@sell_ticket.get('/sell_ticket/{sell_ticket_id}', response_model=Sell_ticket)
async def get_one(sell_ticket_id:int , db:Session = Depends(get_db)):
    sell_ticket = get_sell_ticket(db, sell_ticket_id)
    if sell_ticket is None:
        raise HTTPException(status_code=404, detail="sell_ticket not found")
    return sell_ticket

@sell_ticket.post('/sell_ticket', response_model=Sell_ticket)
async def insert_one(sell_ticket:Sell_ticketCreate, db:Session = Depends(get_db)):
    return insert_sell_ticket(db, sell_ticket)

@sell_ticket.put('/sell_ticket/{sell_ticket_id}', response_model=Sell_ticket)
async def update_one(sell_ticket_id:int, sell_ticket:Sell_ticketUpdate, db:Session = Depends(get_db)):
    return update_sell_ticket(db, sell_ticket_id, sell_ticket)

@sell_ticket.put('/sell_ticket/{sell_ticket_id}/is_finish', response_model=Sell_ticket)
async def update_one_is_finish(sell_ticket_id:int, sell_ticket:Sell_ticketFinish, db:Session = Depends(get_db)):
    return update_sell_ticket_is_finish(db, sell_ticket_id, sell_ticket)

@sell_ticket.delete('/sell_ticket/{sell_ticket_id}')
async def delete_one(sell_ticket_id:int, db:Session = Depends(get_db)):
    return delete_sell_ticket(db, sell_ticket_id)