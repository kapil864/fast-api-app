from fastapi import Response
from .test_client import client


def test_get_author():
    response: Response = client.get('/author/me')
    assert response.json() == {
        'first_name': 'kapil',
        'last_name': 'string',
        'username': 'string',
        'email': 'string@string.com'
    }
