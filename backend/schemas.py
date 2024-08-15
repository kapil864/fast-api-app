from datetime import date, datetime
from typing import Annotated
from pydantic import BaseModel, EmailStr, Field


class BlogBase(BaseModel):
    pass


class AuthorBase(BaseModel):
    pass


class CategoryBase(BaseModel):
    pass


class CommentsBase(BaseModel):
    pass


class Blog(BlogBase):
    categories: list[CategoryBase]
    author_id: int
    title: str
    subheading: str
    content: str

    class Config:
        orm_mode = True


class BlogCreate(Blog):
    pass


class BlogPublic(Blog):
    id: int
    timestamp: datetime


class Author(AuthorBase):
    username: str
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True


class AuthorPublic(Author):
    id: int
    blogs: list[Blog]


class AuthorCreate(Author):
    password: str


class Comment(CommentsBase):
    timestamp: date
    author_id: int
    content: str
    blog_id: int


class Category(CategoryBase):
    name: str

    class Config:
        orm_mode = True


class CategoryCreate(Category):
    pass


class CategoryPublic(Category):
    id: int
    related_category: list[CategoryBase]
