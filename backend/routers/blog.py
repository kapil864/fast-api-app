from fastapi import APIRouter, Response, status


from ..schemas import Blog

router = APIRouter()

blogs_list = []

@router.post('/')
async def add_blogs(blog: Blog):
    blogs_list.append(blog)
    return Response(content="Blog created", status_code=status.HTTP_201_CREATED)

@router.get('/', response_model=list[Blog])
async def get_blogs():
    return blogs_list