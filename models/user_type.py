from datetime import date
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from databases.database import Base

class User_type(Base):
    __tablename__ = "user_type"

    id        = Column(Integer, primary_key=True, unique=True, index=True)
    type      = Column(String, index=True)
    is_view   = Column(Boolean, default=True, index=True)
    is_write  = Column(Boolean, default=True, index=True)
    is_edit   = Column(Boolean, default=True, index=True)
    is_delete = Column(Boolean, default=True, index=True)
    is_active = Column(Boolean, default=True, index=True)
    create_at = Column(Date, default=date.today())
    update_at = Column(Date)

    user = relationship("User", back_populates="user_type")