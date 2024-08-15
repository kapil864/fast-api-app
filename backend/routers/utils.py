from datetime import datetime
from sqlalchemy.orm import Session

from .. import models, schemas
from ..utils import encrypt_password


def create_author(db: Session, author: schemas.AuthorCreate):
    hashed_password = encrypt_password(author.password)
    author = models.Author(
        username=author.username,
        first_name=author.first_name,
        last_name=author.last_name,
        email=author.email,
        password=hashed_password
    )
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def get_author_by_email(db: Session, email: str):
    return db.query(models.Author).filter(models.Author.email == email).first()


def get_author_by_username(db: Session, username: str):
    return db.query(models.Author).filter(models.Author.username == username).first()

def create_db_blog(db:Session, blog: schemas.Blog):
    blog = models.Blog(**blog.model_dump(), timestamp = datetime.now())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_category_db(db:Session, category: str):
    category = db.query(models.Category).filter(models.Category.name == category).first()
    return category

def get_all_categories_db(db:Session):
    return db.query(models.Category).all()

def create_category_db(db:Session, category : schemas.Category):
    if get_category_db(db, category.name) is None:
        category = models.Category(**category.model_dump())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    return None