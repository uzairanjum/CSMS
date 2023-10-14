from fastapi import APIRouter
from .schema import UserModel, UserResponseModel


user_router = APIRouter()


@user_router.post(
    "/user",
    tags=["user"],
    status_code=201,
    summary="create a new user",
    description="create a new user",
    # response_model=UserResponseModel,
)
def create_user(request: UserModel):
    print("Creating new user", request.first_name)
    return request


@user_router.get(
    "/user",
    tags=["user"],
    summary="get user",
    description="get user",
    response_model=UserResponseModel,
)
def create_user():
    return {"message": "get user", "code": 201, "data": "request"}


@user_router.patch(
    "/user",
    tags=["user"],
    summary="update user",
    description="update user",
    response_model=UserResponseModel,
)
def create_user():
    return {"message": 'update user"'}


@user_router.delete(
    "/user",
    tags=["user"],
    summary="delete user",
    description="delete user",
    response_model=UserResponseModel,
)
def create_user():
    return {"message": "delete user"}
