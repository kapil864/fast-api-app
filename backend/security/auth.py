from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from ..dependencies import get_db_session
from ..routers.utils import get_author_by_username

router = APIRouter()

oauth2_Scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/token')
async def login(db=Annotated[Session, Depends(get_db_session)], form_data=Annotated[OAuth2PasswordRequestForm, Depends()]):
    author = get_author_by_username(db, form_data.username)