from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import routine_model
from schemas import routine_schema
from uuid import uuid4

# get routine for user id


def get_routine(db: Session, user_id: str) -> list[routine_schema.Routine]:
    return db.query(routine_model.Routine).filter(routine_model.Routine.user_id == user_id).all()

# create routine for user id


def create_routine(db: Session, routine: routine_schema.RoutineCreate, user_id: str) -> routine_schema.Routine:
    db_routine = routine_model.Routine(
        id=uuid4(), name=routine.name, user_id=user_id)
    db.add(db_routine)
    db.commit()
    db.refresh(db_routine)
    return db_routine

# update routine for routine id


def update_routine(db: Session, routine: routine_schema.RoutineUpdate, routine_id: str) -> routine_schema.Routine:
    db_routine = db.query(routine_model.Routine).filter(
        routine_model.Routine.id == routine_id).first()
    if not db_routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    db_routine.name = routine.name
    db.commit()
    db.refresh(db_routine)
    return db_routine

# delete routine for routine id


def delete_routine(db: Session, routine_id: str) -> routine_schema.Routine:
    db_routine = db.query(routine_model.Routine).filter(
        routine_model.Routine.id == routine_id).first()
    if not db_routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    db.delete(db_routine)
    db.commit()
    return db_routine
