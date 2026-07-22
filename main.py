from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float

