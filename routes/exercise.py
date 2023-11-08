from fastapi import APIRouter, Depends
from crud import crud_exercise
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from schemas import exercise_schema

exercise = APIRouter(prefix="/exercise", tags=["exercise"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all exercises from database


@exercise.get("/", status_code=200, response_model=list[exercise_schema.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    return crud_exercise.get_exercises(db)
