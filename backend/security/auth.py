import jwt
from os import getenv
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from ..models import Author
from ..dependencies import get_db_session
from ..routers.utils import get_author_by_username
from .utils import verify_password
from ..schemas import Token

SECRET_KEY = getenv('SECRET_KEY')
ALGORITHIM = getenv('ALGORITHIM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

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
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHIM)


async def get_current_user(db: Annotated[Session, Depends(get_db_session)], token: Annotated[str, Depends(oauth2_Scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHIM])
    try:
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    author = get_author_by_username(db, username)
    if author is None:
        raise credentials_exception
    return author


async def verify_token(author: Annotated[Author, Depends(get_current_user)]):
    if author:
        return True
    return False


@router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db_session)]):
    username: str = form_data.username
    if authenticate_author(db, username, form_data.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            {'sub': username},
            access_token_expires
        )
        return Token(access_token=access_token, token_type='bearer')
