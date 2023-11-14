from pydantic import BaseModel
from schemas.exercise_schema import Exercise
from typing import List


class ExerciseUserBase(BaseModel):
    exercise_id: str


class ExerciseUserCreate(ExerciseUserBase):
    pass


class ExercisesUser(ExerciseUserBase):
    id: str
    routine_id: str
    exercise: Exercise

    class Config:
        orm_mode = True
