from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class Function(Base):
    __tablename__ = "function"

    id          = Column(Integer, primary_key=True, unique=True, index=True)
    start_time  = Column(Float, index=True)
    finish_time = Column(Float, index=True)
    is_started  = Column(Boolean, default=False)
    is_active   = Column(Boolean, default=True)
    create_at   = Column(Date, default=date.today())
    update_at   = Column(Date)
    movie_id    = Column(Integer, ForeignKey("movie.id"))
    room_id     = Column(Integer, ForeignKey("room.id"))

    movie = relationship("Movie", back_populates="function")
    room  = relationship("Room", back_populates="function")