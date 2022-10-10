from datetime import date
from sqlalchemy import Float, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from databases.database import Base

class Movie(Base):
    __tablename__ = "movie"

    id          = Column(Integer, primary_key=True, unique=True, index=True)
    name        = Column(String, index=True)
    description = Column(Text)
    duration    = Column(Float, index=True)
    director    = Column(String)
    cast        = Column(Text)
    is_active   = Column(Boolean, default=True)
    create_at   = Column(Date, default=date.today())
    update_at   = Column(Date)
    quality_id  = Column(Integer, ForeignKey("quality.id"))

    function = relationship("Function", back_populates="movie")
    quality  = relationship("Quality", back_populates="movie")