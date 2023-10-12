from fastapi import FastAPI, Request, APIRouter

root_router = APIRouter(prefix="/v1")


@root_router.get('/health', tags=['server'],  summary="healthy", description ="healthy")
def health(request:Request):
    return {"message":"healthy"}