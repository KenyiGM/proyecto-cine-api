from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Detail_sell_food(Base):
    __tablename__ = "detail_sell_food"
    
    id           = Column(Integer, primary_key=True, unique=True, index=True)
    quantity     = Column(Integer, index=True)
    subtotal     = Column(Float, index=True)
    is_active    = Column(Boolean, default=True)
    create_at    = Column(Date, default=date.today())
    update_at    = Column(Date)
    sell_food_id = Column(Integer, ForeignKey("sell_food.id"))
    food_id      = Column(Integer, ForeignKey("food.id"))

    sell_food = relationship("Sell_food", back_populates="detail_sell_food")
    food      = relationship("Food", back_populates="detail_sell_food")