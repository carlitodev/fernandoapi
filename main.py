from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int


DB: List[Person] = [
    Person(id=1, name="Jamila", age=25),
    Person(id=2, name="Gabriela", age=31),
    Person(id=3, name="Fernando", age=22),
]


@app.get("/api")
def read_api():
    return DB


@app.get("/")
def read_root ():
    return {"Hello": "Rick"}


@app.get("/items/{item_id}")
def read_item (item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
