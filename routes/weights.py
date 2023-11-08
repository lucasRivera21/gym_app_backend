from fastapi import APIRouter, Depends
from crud import crud_weight
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from schemas import weight_schema

weight = APIRouter(prefix="/weights", tags=["weights"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all weights for user id


@weight.get("/{user_id}", status_code=200, response_model=list[weight_schema.Weight])
def read_weights(user_id: str, db: Session = Depends(get_db)):
    weights = crud_weight.get_weights(db, user_id)
    return weights
# create weight for user id


@weight.post("/{user_id}", status_code=201, response_model=weight_schema.Weight)
def create_weight(user_id: str, weight: weight_schema.WeightCreate, db: Session = Depends(get_db)):
    return crud_weight.create_weight(db=db, weight=weight, user_id=user_id)
