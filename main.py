from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root() -> dict:
    return {'Message': 'Hello World'}
