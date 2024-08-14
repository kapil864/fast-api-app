from datetime import date, datetime
from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, UUID1

class BlogBase(BaseModel):
    pass

class AuthorBase(BaseModel):
    pass

class CategoryBase(BaseModel):
    pass

class CommentsBase(BaseModel):
    pass

class Blog(BlogBase):
    id: UUID1
    timestamp: datetime = Field(default=datetime.now())
    category_id: UUID1
    author_id: UUID1
    title: str
    subheading: str
    content: str

    class Config:
        orm_mode = True

class Author(AuthorBase):
    id: UUID1
    username : str
    first_name: str
    last_name: str
    email: EmailStr
    password : str
    blogs: list[Blog]

class AuthorInDB(Author):
    password: str

class Comment(CommentsBase):
    timestamp: date
    author_id: UUID1
    content: str
    blog_id: UUID1

class Category(CategoryBase):
    category: str
    related_category: list[CategoryBase|None]

