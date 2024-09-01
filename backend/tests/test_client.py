from fastapi.testclient import TestClient

from ..security.auth import get_current_user
from ..main import app
from .dependency_overrides import override_get_db_session, override_get_current_user
from ..dependencies import get_db_session

app.dependency_overrides[get_db_session] = override_get_db_session
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)
