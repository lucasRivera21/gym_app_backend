from fastapi import APIRouter, Depends
from crud import crud_routine
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from security.auth import get_user_id
from schemas import routine_schema

routine = APIRouter(prefix="/routine", tags=["routine"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all routines for user id


@routine.get("/", status_code=200, response_model=list[routine_schema.Routine])
def read_routine(user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    routines = crud_routine.get_routine(db, user_id)
    return routines

# create routine for user id


@routine.post("/", status_code=201, response_model=routine_schema.Routine)
def create_rotine(routine: routine_schema.RoutineCreate, user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    return crud_routine.create_routine(db=db, routine=routine, user_id=user_id)

# update routine for routine id


@routine.put("/", status_code=200, response_model=routine_schema.Routine)
def update_routine(routine: routine_schema.RoutineUpdate, routine_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    return crud_routine.update_routine(db=db, routine=routine, routine_id=routine_id)

# delete routine for routine id


@routine.delete("/", status_code=200, response_model=routine_schema.Routine)
def delete_routine(routine_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    return crud_routine.delete_routine(db=db, routine_id=routine_id)
