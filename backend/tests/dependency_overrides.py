

from .database_override import TestingSessionLocal


def override_get_db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {
        'first_name': 'kapil',
        'last_username': 'string',
        'username': 'string',
        'email': 'string@string.com'
    }
