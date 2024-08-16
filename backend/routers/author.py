from fastapi import APIRouter, Response, status, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from ..schemas import Author, AuthorCreate, AuthorPublic
from ..dependencies import get_db_session
from .utils import get_author_by_username, create_author as create_db_author, get_all_authors_db

router = APIRouter()


@router.get('/me', response_model=Author)
async def get_author(response: Response, db: Session = Depends(get_db_session), username: str = None):
    if username is not None:
        author = get_author_by_username(db, username)
        if author:
            response.status_code = status.HTTP_200_OK
            return author
    return JSONResponse(status_code=404, content="Not found")


@router.post('/register', response_model=AuthorPublic)
async def create_author(response: Response, author: AuthorCreate, db: Session = Depends(get_db_session)):
    author_db = get_author_by_username(db, author.username)
    if author_db:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"message": "Author already exists."})
    author = create_db_author(db,author)
    return author

@router.get('/all', response_model=list[AuthorPublic])
async def get_all_authors(response: Response, db: Session = Depends(get_db_session)):
    authors = get_all_authors_db(db)
    return authors