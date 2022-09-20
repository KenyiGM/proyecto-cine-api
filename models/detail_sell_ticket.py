from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Detail_sell_ticket(Base):
    __tablename__ = "detail_sell_ticket"
    
    id             = Column(Integer, primary_key=True, unique=True, index=True)
    is_active      = Column(Boolean, default=True)
    create_at      = Column(Date, default=date.today())
    finish_at      = Column(Date)
    room_seat_id   = Column(Integer, ForeignKey("room_seat.id"))
    sell_ticket_id = Column(Integer, ForeignKey("sell_ticket.id"))
    ticket_id      = Column(String, ForeignKey("ticket.id"))

    sell_ticket = relationship("Sell_ticket", back_populates="detail_sell_ticket")
    ticket      = relationship("Ticket", back_populates="detail_sell_ticket")
    room_seat   = relationship("Room_seat", back_populates="detail_sell_ticket")
