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
    author_id: int
    title: str
    subheading: str
    content: str

    class Config:
        orm_mode = True


class BlogCreate(Blog):
    categories: list[int]


class BlogPublic(Blog):
    id: int
    timestamp: datetime
    categories: list['Category']


class Author(AuthorBase):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class AuthorPublic(Author):
    id: int
    blogs: list[Blog]

    class Config:
        orm_mode = True


class AuthorCreate(Author):
    password: str


class Category(CategoryBase):
    name: str

    class Config:
        orm_mode = True

class CategoryPublic(Category):
    id: int


class CategoryPublicBlogs(Category):
    blogs: list[BlogPublic]


class Comment(CommentsBase):
    timestamp: date
    author_id: int
    content: str
    blog_id: int


class Token(BaseModel):
    token: str
    type: str
