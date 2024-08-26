from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from ..security.auth import oauth2_Scheme
from ..schemas import BlogCreate, BlogPublic
from ..dependencies import get_db_session
from .utils import create_db_blog, get_all_blogs_db
router = APIRouter()


@router.post(path='/', response_model=BlogPublic )
async def add_blogs(response: Response, blog: BlogCreate, db: Session = Depends(get_db_session), token: str = Depends(oauth2_Scheme)):
    blog = create_db_blog(db, blog)
    response.status_code = status.HTTP_201_CREATED
    return blog


@router.get('/', response_model=list[BlogPublic])
async def get_blogs(db: Session = Depends(get_db_session)):
    return get_all_blogs_db(db)
