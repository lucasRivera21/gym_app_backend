from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    aproach = Column(String)
    equipament = Column(String)
    img_url = Column(String)

    exercises_user = relationship("ExerciseUser", back_populates="exercise")
