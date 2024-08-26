import jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from ..models import Author
from ..dependencies import get_db_session
from ..routers.utils import get_author_by_username
from .utils import verify_password
from ..schemas import Token

SECRECT_KEY = '25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b8'
ALGORITHIM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 5

router = APIRouter()

oauth2_Scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def authenticate_author(db: Session, username: str, password: str) -> bool | HTTPException:
    author: Author = get_author_by_username(db, username)
    if author and verify_password(password, author.hashed_password):
        return True
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid username or password",
                            headers={'WWW-Authenticate': 'bearer'},
                            )


def create_access_token(payload: dict, expire_delta: timedelta | None = None):
    to_encode = payload.copy()
    if expire_delta:
        expire_time = datetime.now(timezone.utc) + \
            expire_delta
    else:
        expire_time = datetime.now(timezone.utc) + timedelta(seconds=60)
    to_encode.update({'exp': expire_time})
    return jwt.encode(to_encode, SECRECT_KEY, ALGORITHIM)


@router.post('/token')
async def login( form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : Annotated[Session, Depends(get_db_session)]):
    username: str = form_data.username
    if authenticate_author(db, username, form_data.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            {'sub': username},
            access_token_expires
        )
        return Token(token=access_token, type='bearer')
