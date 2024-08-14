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
