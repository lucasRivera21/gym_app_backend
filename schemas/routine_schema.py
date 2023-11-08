from pydantic import BaseModel
from . import exercise_user_schema
from typing import List


class RoutineBase(BaseModel):
    name: str


class RoutineCreate(RoutineBase):
    pass


class RoutineUpdate(RoutineBase):
    pass


class Routine(RoutineBase):
    id: str
    user_id: str
    exercises_user: List[exercise_user_schema.ExercisesUser] = []

    class Config:
        orm_mode = True
