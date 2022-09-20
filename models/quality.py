from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Quality(Base):
    __tablename__ = "quality"

    id        = Column(Integer, primary_key=True, unique=True, index=True)
    name      = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    create_at = Column(Date, default=date.today())
    update_at = Column(Date)

    movie = relationship("Movie", back_populates="quality")