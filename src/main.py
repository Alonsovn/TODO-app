from fastapi import FastAPI, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models
from db import DBContext

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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
