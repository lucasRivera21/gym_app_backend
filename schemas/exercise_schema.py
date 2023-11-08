from pydantic import BaseModel


class Exercise(BaseModel):
    id: str
    name: str
    aproach: str
    equipament: str
    img_url: str

    class Config:
        orm_mode = True
