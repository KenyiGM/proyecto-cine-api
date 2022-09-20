from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class City(Base):
    __tablename__ = "city"

    id         = Column(Integer, primary_key=True, unique=True, index=True)
    name       = Column(String, unique=True, index=True)
    is_active  = Column(Boolean, default=True)
    create_at  = Column(Date, default=date.today())
    update_at  = Column(Date)
    country_id = Column(Integer, ForeignKey("country.id"))
    
    country = relationship("Country", back_populates="city")
    cinema  = relationship("Cinema", back_populates="city")