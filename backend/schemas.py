from datetime import date, datetime
from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class BlogBase(BaseModel):
    pass


class AuthorBase(BaseModel):
    pass


class CategoryBase(BaseModel):
    pass


class CommentsBase(BaseModel):
    pass


class Blog(BlogBase):

    model_config = ConfigDict(from_attributes=True)

    title: str
    subheading: str
    content: str



class BlogCreate(Blog):
    categories: list[int]


class BlogPublic(Blog):
    id: int
    timestamp: datetime
    author_id: int
    categories: list['Category']


class Author(AuthorBase):
    username: str
    first_name: str
    last_name: str
    email: EmailStr


class AuthorPublic(Author):

    model_config = ConfigDict(from_attributes=True)

    id: int
    blogs: list[Blog]


class AuthorCreate(Author):
    password: str


class Category(CategoryBase):
    
    model_config = ConfigDict(from_attributes=True)

    name: str


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
    access_token: str
    token_type: str
