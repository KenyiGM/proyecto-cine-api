from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Employee(Base):
    __tablename__ = "employee"

    id               = Column(Integer, primary_key=True, unique=True, index=True)
    firstname        = Column(String, index=True)
    lastname         = Column(String, index=True)
    years_old        = Column(Integer, index=True)
    birthday         = Column(Date, index=True)
    indentity_number = Column(String, index=True)
    address          = Column(String, index=True)
    email            = Column(String, index=True)
    start_date       = Column(Date, index=True)
    departure_date   = Column(Date)
    is_active        = Column(Boolean, default=True)
    create_at        = Column(Date, default=date.today())
    update_at        = Column(Date)
    finish_at        = Column(Date)
    user_id          = Column(Integer, ForeignKey("user.id"))

    user        = relationship("User", back_populates="employee")
    sell_ticket = relationship("Sell_ticket", back_populates="employee")
    sell_food = relationship("Sell_food", back_populates="employee")
    