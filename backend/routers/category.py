from fastapi import APIRouter, Response, status, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from ..dependencies import get_db_session
from ..models import Category
from ..schemas import Category as sCategory, CategoryPublic
from .utils import get_all_categories_db, get_category_db, create_category_db

router = APIRouter()


@router.get('/all')
async def get_all_categories(response: Response, db: Session = Depends(get_db_session)):
    categories = get_all_categories_db(db)
    if len(categories) != 0:
        return categories
    return JSONResponse(content={'message': 'No categories exist, create one'}, status_code=200)


@router.get('/', response_model=CategoryPublic)
async def get_category(category: str = None, db: Session = Depends(get_db_session)):
    category = get_category_db(db, category)
    if category is not None:
        return category
    return JSONResponse(status_code=404, content={'message': 'Category does not exist'})


@router.post('/')
async def create_category(category: sCategory, db: Session = Depends(get_db_session)):
    category = create_category_db(db, category)
    if category is not None:
        return category
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={'message': 'category already exist'})
