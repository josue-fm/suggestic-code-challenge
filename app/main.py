from fastapi import FastAPI, status

from app.model.models import SuggesticRequest
from app.service.services import flattens_items


app = FastAPI(
    title='Suggestic challenge',
    description='API for flattens nested list of integer',
    version='0.0.1',
    redoc_url=None
)


@app.post('/items', status_code=status.HTTP_201_CREATED)
async def post_items(request: SuggesticRequest):
    return {'result': await flattens_items(request.items) }