from fastapi import FastAPI
from pydantic import BaseModel
from http import HTTPStatus


app = FastAPI()


class Root(BaseModel):
    message: str

@app.get(
    path = '/',
    status_code=HTTPStatus.OK,
    response_model=Root)
def root() -> dict:
    return {'message': 'Hello World'}
