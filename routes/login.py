from fastapi import APIRouter, Depends
from security import auth

from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from schemas import user_schema
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from security.auth import oauth2_scheme


login = APIRouter(prefix="/login", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@login.post("/", status_code=200)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = auth.login(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}

'''
@login.get("/me", status_code=200, response_model=user_schema.User)
async def get_user_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = auth.get_current_user(db, token)
    return user
'''
