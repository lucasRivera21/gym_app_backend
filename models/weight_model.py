from datetime import date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from db import Base


class Weight(Base):
    __tablename__ = "weights"

    id = Column(String, primary_key=True, index=True)
    weight = Column(Integer)
    magnitude = Column(String)
    date = Column(Date, default=date.today())
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="weights")
