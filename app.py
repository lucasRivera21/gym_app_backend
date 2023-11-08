from fastapi import FastAPI, Depends
from routes import users, weights, routines, exercise_user, exercise, login
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

origins = [config('FRONTEND_URL')]

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(users.user)
app.include_router(weights.weight)
app.include_router(routines.routine)
app.include_router(exercise_user.exercise_user)
app.include_router(exercise.exercise)
app.include_router(login.login)
