from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Room_seat(Base):
    __tablename__ = "room_seat"

    id           = Column(Integer, primary_key=True, unique=True, index=True)
    row          = Column(Integer, index=True)
    column       = Column(Integer, index=True)
    is_occupied  = Column(Boolean, default=False)
    is_active    = Column(Boolean, default=True)
    create_at    = Column(Date, default=date.today())
    update_at    = Column(Date)
    room_id      = Column(Integer, ForeignKey("room.id"), index=True)
    seat_id      = Column(Integer, ForeignKey("seat.id"), index=True)

    room = relationship("Room", back_populates="room_seat")
    seat = relationship("Seat", back_populates="room_seat")
    detail_sell_ticket = relationship("Detail_sell_ticket", back_populates="room_seat")