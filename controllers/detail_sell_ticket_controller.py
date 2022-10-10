from fastapi import APIRouter, Depends, HTTPException
from services.detail_sell_ticket_service import *
from databases.repository import get_db
from schemas.detail_sell_ticket_schema import Detail_sell_ticket

detail_sell_ticket = APIRouter()

@detail_sell_ticket.get('/detail_sell_ticket', response_model=list[Detail_sell_ticket])
async def get_all(db:Session = Depends(get_db)):
    return get_details_sell_tickets(db)

@detail_sell_ticket.get('/detail_sell_ticket/{detail_sell_ticket_id}', response_model=Detail_sell_ticket)
async def get_one(detail_sell_ticket_id:int , db:Session = Depends(get_db)):
    detail_sell_ticket = get_detail_sell_ticket(db, detail_sell_ticket_id)
    if detail_sell_ticket is None:
        raise HTTPException(status_code=404, detail="detail_sell_ticket not found")
    return detail_sell_ticket

@detail_sell_ticket.post('/detail_sell_ticket', response_model=Detail_sell_ticket)
async def insert_one(detail_sell_ticket:Detail_sell_ticketCreate, db:Session = Depends(get_db)):
    return insert_detail_sell_ticket(db, detail_sell_ticket)

@detail_sell_ticket.put('/detail_sell_ticket/{detail_sell_ticket_id}', response_model=Detail_sell_ticket)
async def update_one(detail_sell_ticket_id:int, detail_sell_ticket:Detail_sell_ticketUpdate, db:Session = Depends(get_db)):
    return update_detail_sell_ticket(db, detail_sell_ticket_id, detail_sell_ticket) 

@detail_sell_ticket.put('/detail_sell_ticket/{detail_sell_ticket_id}/is_active', response_model=Detail_sell_ticket)
async def update_one_by_is_active(detail_sell_ticket_id:int, detail_sell_ticket:Detail_sell_ticketUpdateByIsActive, db:Session = Depends(get_db)):
    return update_detail_sell_ticket_by_is_active(db, detail_sell_ticket_id, detail_sell_ticket)

@detail_sell_ticket.delete('/detail_sell_ticket/{detail_sell_ticket_id}')
async def delete_one(detail_sell_ticket_id:int, db:Session = Depends(get_db)):
    return delete_detail_sell_ticket(db, detail_sell_ticket_id)