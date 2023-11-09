from datetime import datetime
from pydantic import BaseModel
from typing import List


class WeightBase(BaseModel):
    weight: float
    magnitude: str


class WeightUpdate(WeightBase):
    id: str


class WeightCreate(WeightBase):
    pass


class Weight(WeightBase):
    id: str
    user_id: str

    class Config:
        orm_mode = True
