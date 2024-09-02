from sqlalchemy.orm import Session

from .database_override import TestingSessionLocal
from ..models import Author
from .utils import author


def override_get_db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    session: Session = TestingSessionLocal()
    yield session.query(Author).filter(Author.username == author.get('username')).first()
    session.close()