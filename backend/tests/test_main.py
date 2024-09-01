from fastapi import Response, status

from .test_client import client


def test_health():
    response: Response = client.get('/health')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status':'healthy'}
