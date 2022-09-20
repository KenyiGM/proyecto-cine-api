from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Country(Base):
    __tablename__ = "country"

    id        = Column(Integer, primary_key=True, unique=True, index=True)
    name      = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    create_at = Column(Date, default=date.today())
    update_at = Column(Date)

    city = relationship("City", back_populates="country")
