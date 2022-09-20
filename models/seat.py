from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Seat(Base):
    __tablename__ = "seat"

    id         = Column(Integer, primary_key=True, unique=True, index=True)
    label      = Column(String, index=True)
    rows       = Column(Integer, index=True)
    columns    = Column(Integer, index=True)
    is_active  = Column(Boolean, default=True)
    create_at  = Column(Date, default=date.today())
    update_at  = Column(Date)

    room_seat = relationship("Room_seat", back_populates="seat")