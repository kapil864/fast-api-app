from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import session

from ..schemas import Blog
from ..dependencies import get_db_session

router = APIRouter()


@router.post('/')
async def add_blogs(blog: Blog,db: session = Depends(get_db_session)):
    return Response(content="Blog created", status_code=status.HTTP_201_CREATED)

@router.get('/')
async def get_blogs():
    return "hi"

