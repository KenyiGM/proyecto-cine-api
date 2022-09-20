from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Sell_food(Base):
    __tablename__ = "sell_food"
    
    id          = Column(Integer, primary_key=True, unique=True, index=True)
    total       = Column(Float)
    pay         = Column(Float)
    is_paid     = Column(Boolean, default=False)
    is_pay_card = Column(Boolean, default=False)
    is_active   = Column(Boolean, default=True)
    create_at   = Column(Date, default=date.today())
    update_at   = Column(Date)
    finish_at   = Column(Date)
    client_id   = Column(Integer, ForeignKey("client.id"))
    employee_id = Column(Integer, ForeignKey("employee.id"))

    client           = relationship("Client", back_populates="sell_food")
    employee         = relationship("Employee", back_populates="sell_food")
    detail_sell_food = relationship("Detail_sell_food", back_populates="sell_food")
