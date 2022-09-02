from fastapi import FastAPI, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi_login import LoginManager
import os


import models
from db import DBContext

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 60

manager = LoginManager(SECRET_KEY, token_url="login", use_cookie=True)
manager.cookie_name = "auth"


def get_db():
    with DBContext() as db:
        yield db


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "title": "Home"})


@app.get("/task")
def get_task(db: Session = Depends(get_db)):
    return jsonable_encoder(db.query(models.Task.first()))


@app.get("/login")
def root(request: Request):
    return templates.TemplateResponse("login.html",
                                      {"request": request, "title": "Login"})
