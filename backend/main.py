from fastapi import FastAPI

from .routers.blog import router as blog_router
from .routers.author import router as author_router

from . import models, schemas
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(prefix='/blog', router=blog_router)
app.include_router(prefix='/author', router=author_router)