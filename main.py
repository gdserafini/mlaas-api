from fastapi import FastAPI
from pydantic import BaseModel
from http import HTTPStatus
from app.user.controller import router as user_router


app = FastAPI()
app.include_router(user_router)


class Root(BaseModel):
    message: str


@app.get(
    path = '/',
    status_code=HTTPStatus.OK,
    response_model=Root)
def root() -> dict:
    return {'message': 'Hello World'}
