from fastapi.testclient import TestClient
from main import app
from http import HTTPStatus


client = TestClient(app)


def test_root_should_return_ok():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}