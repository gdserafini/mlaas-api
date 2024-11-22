from http import HTTPStatus


def test_create_201_wmsg(client):
    data = {
        'username': 'string',
        'email': 'string@example.com',
        'password': 'string'
    }
    response = client.post('/user', json=data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'string',
        'email': 'string@example.com',
        'message': 'User created.'
    }


def test_get_users_200(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [
        {
            'id': 1,
            'username': 'string',
            'email': 'string@example.com'
        }
    ]