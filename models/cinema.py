from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Cinema(Base):
    __tablename__ = "cinema"

    id        = Column(Integer, primary_key=True, unique=True, index=True)
    name      = Column(String, unique=True, index=True)
    address   = Column(Text, index=True)
    is_active = Column(Boolean, default=True)
    create_at = Column(Date, default=date.today())
    update_at = Column(Date)
    city_id   = Column(Integer, ForeignKey("city.id"))

    city = relationship("City", back_populates="cinema")
    room = relationship("Room", back_populates="cinema")