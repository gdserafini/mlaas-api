from fastapi.testclient import TestClient
from main import app
from http import HTTPStatus


client = TestClient(app)


def test_create_201_msg():
    data = {
        'username': 'string',
        'email': 'string@example.com',
        'password': 'string'
    }
    response = client.post('/user', json=data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'string',
        'email': 'string@example.com',
        'message': 'User created.'
    }