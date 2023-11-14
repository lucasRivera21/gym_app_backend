from fastapi import APIRouter, Depends
from crud import crud_user
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from schemas import user_schema
from routes import login
from routes.login import oauth2_scheme
from security.auth import get_user_id
user = APIRouter(prefix="/user", tags=["user"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()

# Get a user by id


@user.get("/", status_code=200, response_model=user_schema.User)
def read_user(user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    return crud_user.get_user(db=db, user_id=user_id)

# Create a user


@user.post("/", status_code=201, response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)

# Update a user's name


@user.put("/{user_id}/name", status_code=200, response_model=user_schema.User)
def update_name(user_id: str, name: str, db: Session = Depends(get_db)):
    return crud_user.update_name(db=db, user_id=user_id, name=name)

# Update a user's email


@user.put("/{user_id}/email", status_code=200, response_model=user_schema.User)
def update_email(user_id: str, email: str, db: Session = Depends(get_db)):
    return crud_user.update_email(db=db, user_id=user_id, email=email)

# Update a user's gender


@user.put("/{user_id}/gender", status_code=200, response_model=user_schema.User)
def update_gender(user_id: str, gender: str, db: Session = Depends(get_db)):
    return crud_user.update_gender(db=db, user_id=user_id, gender=gender)

# update a user's password


@user.put("/{user_id}/password", status_code=200, response_model=user_schema.User)
def update_password(user_id: str, password: str, new_password: str, db: Session = Depends(get_db)):
    return crud_user.update_password(db=db, user_id=user_id, password=password, new_password=new_password)
