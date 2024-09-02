from fastapi import APIRouter, Response, status, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from ..schemas import Author, AuthorCreate, AuthorPublic
from ..dependencies import get_db_session
from .utils import get_author_by_username, create_author as create_db_author, get_all_authors_db
from ..security.auth import get_current_user

router = APIRouter()


@router.get('/me', response_model=Author)
async def get_author(author: Author = Depends(get_current_user)):
    return author


@router.post('/register', response_model=AuthorPublic, status_code=status.HTTP_201_CREATED)
async def create_author(author: AuthorCreate, db: Session = Depends(get_db_session)):
    author_db = get_author_by_username(db, author.username)
    if author_db:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"message": "Author already exists."})
    author = create_db_author(db, author)
    return author


@router.post('/update-profile-photo')
async def update_profile_picture(db: Session = Depends(get_db_session), author: Author = Depends(get_current_user), ):
    pass


@router.get('/all', response_model=list[AuthorPublic])
async def get_all_authors(db: Session = Depends(get_db_session), author: Author = Depends(get_current_user)):
    authors = get_all_authors_db(db)
    return authors
