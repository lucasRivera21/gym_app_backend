from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import exercises_user_model
from schemas import exercise_user_schema
from uuid import uuid4


def get_exercise_users(db: Session, routine_id: str) -> list[exercise_user_schema.ExercisesUser]:

    return db.query(exercises_user_model.ExerciseUser).filter(exercises_user_model.ExerciseUser.routine_id == routine_id).all()


def create_exercise_user(db: Session, routine_id: str, exercise_id: str) -> exercise_user_schema.ExercisesUser:

    db_exercise_user = exercises_user_model.ExerciseUser(
        routine_id=routine_id, exercise_id=exercise_id, id=uuid4())
    db.add(db_exercise_user)
    db.commit()
    db.refresh(db_exercise_user)
    return db_exercise_user
