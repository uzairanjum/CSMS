from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user_router, root_router


app = FastAPI(
    title="Fast API Example",
    description="Fast API Example",
    version="0.0.1"
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=['*'],
#     allow_methods=['*'],
#     allow_headers=['*'],
#     allow_credentials=True
#     )

root_router.include_router(user_router)
app.include_router(root_router)  

