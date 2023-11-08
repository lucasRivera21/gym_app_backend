from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import user_model
from schemas import user_schema, token_schema
import hashlib
from passlib.context import CryptContext
from datetime import datetime, timedelta
from decouple import config
from jose import JWTError, jwt

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

'''
async def auth_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         if decode_token['exp'] < datetime.utcnow():
           raise HTTPException(status_code=401, detail="Token expired")
        if decode_token is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return decode_token['sub']

'''


def get_current_user(db: Session, token: str):
    try:
        decode_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_user = db.query(user_model.User).filter(
        user_model.User.id == decode_token['sub']).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    if not db_user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    return db_user


def login(db: Session, email: str, password: str) -> user_schema.User:
    # password_hashed = hashlib.sha256(password.encode()).hexdigest()
    db_user = db.query(user_model.User).filter(
        user_model.User.email == email).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not pwd_context.verify(password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    expire = datetime.utcnow(
    ) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    acces_token = {"sub": db_user.id, "exp": expire}
    '''
    if db_user.hashed_password != password_hashed:
        raise HTTPException(status_code=400, detail="Incorrect password")
    '''
    return jwt.encode(acces_token, SECRET_KEY, algorithm=ALGORITHM)
