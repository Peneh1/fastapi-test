from typing import Union

from fastapi import FastAPI

from . import Func



app = FastAPI()


@app.get("/")
def index():
    return Func.index()

@app.get('/a')
def a():
    return Func.a()

@app.get("/name/{name}")
def name(name):
    return Func.name(name)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fun/{amount:int}/{years:int}")
def fun(amount, years):
    return Func.fun(amount, years)
