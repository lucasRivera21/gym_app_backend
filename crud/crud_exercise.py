from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import exercises_model
from schemas import exercise_schema
from uuid import uuid4

# get all exercises from database


def get_exercises(db: Session) -> list[exercise_schema.Exercise]:
    return db.query(exercises_model.Exercise).all()
