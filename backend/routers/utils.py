from datetime import datetime
from fastapi import HTTPException
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


def get_all_authors_db(db: Session):
    return db.query(models.Author).all()


def get_author_by_email(db: Session, email: str):
    return db.query(models.Author).filter(models.Author.email == email).first()


def get_author_by_username(db: Session, username: str):
    return db.query(models.Author).filter(models.Author.username == username).first()


def get_all_blogs_db(db: Session):
    return db.query(models.Blog).all()


def get_category_db(db: Session, category: str):
    category = db.query(models.Category).filter(
        models.Category.name == category).first()
    return category


def get_all_categories_db(db: Session):
    return db.query(models.Category).all()


def create_category_db(db: Session, category: schemas.Category):
    if get_category_db(db, category.name) is None:
        category = models.Category(**category.model_dump())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    return None


def create_db_blog(db: Session, blog: schemas.BlogCreate):
    category_models = db.query(models.Category).filter(models.Category.id.in_(blog.categories)).all()

    if len(blog.categories) != len(category_models):
        raise HTTPException(status_code=404, detail='One or more categories not found')
    
    blog = models.Blog(author_id = blog.author_id,
                       title = blog.title,
                       subheading = blog.subheading,
                       content = blog.content,
                       timestamp=datetime.now(),
                       categories=category_models)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
