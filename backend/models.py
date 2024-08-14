from backend.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Uuid, ForeignKey, Table
from sqlalchemy.orm import relationship

class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Uuid, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    title = Column(String, nullable=False)
    subheading = Column(String, nullable= True)
    content = Column(String, nullable=False)
    author_id = Column(Uuid, ForeignKey('authors.id'))
    categories = relationship(secondary='blog_category_association', back_populates='blogs')

class Author(Base):

    __tablename__ = 'authors'

    id = Column(Uuid, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    blogs = relationship('Blog')

class Category(Base):

    __tablename__ = 'categories'

    id = Column(Uuid, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    blogs = relationship(secondary='blog_category_association', back_populates='categories')

blog_category_association = Table(
    'blog_category_association',
    Base.metadata,
    Column('blog_id', ForeignKey('blogs.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True),
)