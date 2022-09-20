from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Room(Base):
    __tablename__ = "room"

    id         = Column(Integer, primary_key=True, unique=True, index=True)
    name       = Column(String, unique=True, index=True)
    is_active  = Column(Boolean, default=True)
    create_at  = Column(Date, default=date.today())
    update_at  = Column(Date)
    cinema_id  = Column(Integer, ForeignKey("cinema.id"))
    
    cinema    = relationship("Cinema", back_populates="room")
    function = relationship("Function", back_populates="room")
    room_seat = relationship("Room_seat", back_populates="room")