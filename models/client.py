from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Client(Base):
    __tablename__ = "client"

    id               = Column(Integer, primary_key=True, unique=True, index=True)
    firstname        = Column(String, index=True)
    lastname         = Column(String)
    years_old        = Column(Integer)
    indentity_number = Column(String)
    is_active        = Column(Boolean, default=True)
    create_at        = Column(Date, default=date.today())
    update_at        = Column(Date)
    user_id          = Column(Integer, ForeignKey("user.id"))

    user        = relationship("User", back_populates="client")
    sell_ticket = relationship("Sell_ticket", back_populates="client")
    sell_food   = relationship("Sell_food", back_populates="client")
    