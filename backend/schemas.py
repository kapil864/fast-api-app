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
    id: int
    timestamp: datetime = Field(default=datetime.now())
    category_id: int
    author_id: int
    title: str
    subheading: str
    content: str

    class Config:
        orm_mode = True

class Author(AuthorBase):
    username : str
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
    category: str
    related_category: list[CategoryBase|None]

    class Config:
        orm_mode = True

