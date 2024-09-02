from fastapi import Response

from .test_client import client
from .utils import create_author, create_test_author


def test_create_author(create_author):
    body = create_author
    response: Response = client.post('/author/register', json=body)
    assert response.status_code == 201
    assert response.json().get('username') == create_author.get('username')


def test_get_author(create_test_author):

    response: Response = client.get('/author/me')

    assert response.json().get('username') == create_test_author.get('username')
    assert response.json().get('first_name') == create_test_author.get('first_name')
    assert response.json().get('last_name') == create_test_author.get('last_name')
    assert response.json().get('email') == create_test_author.get('email')


def test_get_all_authors(create_test_author):

    response: Response = client.get('/author/all')

    assert response.json() == [
        {
            "username": create_test_author.get('username'),
            "first_name": create_test_author.get('first_name'),
            "last_name": create_test_author.get('last_name'),
            "email": create_test_author.get('email'),
            "blogs": [],
            "id": create_test_author.get('id')
        }
    ]
