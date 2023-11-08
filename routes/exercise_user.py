from fastapi import APIRouter, Depends
from crud import crud_exercise_user
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from schemas import exercise_user_schema

exercise_user = APIRouter(prefix="/exercise_user", tags=["exercise_user"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@exercise_user.get("/{routine_id}", status_code=200)
def get_exercise_users(routine_id: str, db: Session = Depends(get_db)):
    return crud_exercise_user.get_exercise_users(db, routine_id)


@exercise_user.post("/{routine_id}", status_code=201)
def create_exercise_user(routine_id: str, exercise_id: str, db: Session = Depends(get_db)):
    return crud_exercise_user.create_exercise_user(db, routine_id, exercise_id)
