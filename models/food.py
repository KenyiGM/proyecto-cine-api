from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Food(Base):
    __tablename__ = "food"
    
    id          = Column(Integer, primary_key=True, unique=True, index=True)
    name        = Column(String, index=True)
    price       = Column(Float, index=True)
    quantity    = Column(Integer, index=True)
    is_active   = Column(Boolean, default=True)
    create_at   = Column(Date, default=date.today())
    update_at   = Column(Date)
    category_id = Column(Integer, ForeignKey("category.id"))

    detail_sell_food = relationship("Detail_sell_food", back_populates="food")
    category         = relationship("Category", back_populates="food")
