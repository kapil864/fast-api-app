from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .routers.blog import router as blog_router
from .routers.author import router as author_router
from .routers.category import router as category_router
from .security.auth import router as auth_router


app = FastAPI(title='Vblog APIs')

@app.get('/health')
async def health_check():
    return JSONResponse(content={'status': 'healthy'}, status_code=200)

app.include_router(prefix='/blog', router=blog_router, tags=['Blog'])
app.include_router(prefix='/author', router=author_router, tags=['Author'])
app.include_router(prefix='/category',
                   router=category_router, tags=['Category'])
app.include_router(prefix='/auth', router=auth_router,
                   tags=['Authetication and Authorization'])
