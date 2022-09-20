from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class User(Base):
    __tablename__ = "user"

    id           = Column(Integer, primary_key=True, unique=True, index=True)
    username     = Column(String, unique=True, index=True)
    password     = Column(String, index=True)
    is_active    = Column(Boolean, default=True)
    create_at    = Column(Date, default=date.today())
    update_at    = Column(Date)
    finish_at    = Column(Date)
    user_type_id = Column(Integer, ForeignKey("user_type.id"))

    user_type = relationship("User_type", back_populates="user")
    employee  = relationship("Employee", back_populates="user")
    client    = relationship("Client", back_populates="user")