from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import weight_schema
from models import weight_model
from uuid import uuid4

# get weight for user id


def get_weights(db: Session, user_id: str) -> list[weight_schema.Weight]:
    return db.query(weight_model.Weight).filter(weight_model.Weight.user_id == user_id).all()

# create weight for user id


def create_weight(db: Session, weight: weight_schema.WeightCreate, user_id: str) -> weight_schema.Weight:
    db_weight = weight_model.Weight(
        **weight.dict(), user_id=user_id, id=uuid4())
    db.add(db_weight)
    db.commit()
    db.refresh(db_weight)
    return db_weight
