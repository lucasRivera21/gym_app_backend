from pydantic import BaseModel


class ExerciseUserBase(BaseModel):
    exercise_id: str


class ExerciseUserCreate(ExerciseUserBase):
    pass


class ExercisesUser(ExerciseUserBase):
    id: str
    routine_id: str

    class Config:
        orm_mode = True
