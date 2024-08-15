from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from ..schemas import Blog
from ..dependencies import get_db_session
from .utils import create_db_blog

router = APIRouter()


@router.post('/')
async def add_blogs(response: Response, blog: Blog,db: Session = Depends(get_db_session)):
    blog = create_db_blog(db, blog)
    return Response(content="Blog created", status_code=status.HTTP_201_CREATED)

@router.get('/')
async def get_blogs():
    return "hi"

