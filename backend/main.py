from fastapi import FastAPI

from .routers.blog import router as blog_router
from .routers.author import router as author_router
from .routers.category import router as category_router
from .security.auth import router as auth_router

from . import models, schemas
from .database import engine

app = FastAPI(title='Vblog APIs')

# models.Base.metadata.create_all(bind=engine)


app.include_router(prefix='/blog', router=blog_router, tags=['Blog'])
app.include_router(prefix='/author', router=author_router, tags=['Author'])
app.include_router(prefix='/category',
                   router=category_router, tags=['Category'])
app.include_router(prefix='/auth', router=auth_router,
                   tags=['Authetication and Authorization'])
