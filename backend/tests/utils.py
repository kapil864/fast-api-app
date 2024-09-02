import pytest
from sqlalchemy.orm import Session

from ..security.utils import encrypt_password
from ..models import Author
from .database_override import TestingSessionLocal
from ..routers.utils import get_author_by_username, create_author as create_db_author

author = {
    "username": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com",
    "password": "string",
    "id": 1
}


@pytest.fixture
def create_author():

    yield author
    session: Session = TestingSessionLocal()
    db_author = get_author_by_username(
        db=session, username=author.get('username'))
    session.delete(db_author)
    session.commit()
    session.close()


@pytest.fixture
def create_test_author():

    session: Session = TestingSessionLocal()
    hashed_password = encrypt_password(author.get('password'))
    db_author = Author(
        username=author.get('username'),
        first_name=author.get('first_name'),
        last_name=author.get('last_name'),
        email=author.get('email'),
        hashed_password=hashed_password,
        id=author.get('id')
    )
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    yield author
    session.delete(db_author)
    session.commit()
    session.close()
