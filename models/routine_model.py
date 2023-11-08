from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db import Base


class Routine(Base):
    __tablename__ = "routines"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="routines")
    exercises_user = relationship("ExerciseUser", back_populates="routines")
