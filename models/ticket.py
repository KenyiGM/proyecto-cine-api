from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

from databases.database import Base

class Ticket(Base):
    __tablename__ = "ticket"

    id        = Column(String, primary_key=True, unique=True, index=True, default = uuid4())
    expire    = Column(Date, index=True)
    is_active = Column(Boolean, default=True)
    create_at = Column(Date, default=date.today())
    update_at = Column(Date)
    finish_at = Column(Date)

    detail_sell_ticket = relationship("Detail_sell_ticket", back_populates="ticket")