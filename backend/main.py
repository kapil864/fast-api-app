from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

from .routers.blog import router as blog_router
from .routers.author import router as author_router
from .routers.category import router as category_router
from .security.auth import router as auth_router


app = FastAPI(title="Vblog APIs")


# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Vblog APIs",
#         version="1.0.0",
#         description="API Description",
#         routes=app.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT",
#         }
#     }
#     openapi_schema["security"] = [{"BearerAuth": []}]
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi

@app.get('/health')
async def health_check():
    return JSONResponse(content={'status': 'healthy'}, status_code=200)

app.include_router(prefix='/blog', router=blog_router, tags=['Blog'])
app.include_router(prefix='/author', router=author_router, tags=['Author'])
app.include_router(prefix='/category',
                   router=category_router, tags=['Category'])
app.include_router(prefix='/auth', router=auth_router,
                   tags=['Authetication and Authorization'])
