from fastapi import FastAPI

from .routers.blog import router as blog_router

app = FastAPI()

app.include_router(prefix='/blog', router=blog_router)