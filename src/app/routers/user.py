from fastapi import APIRouter


user_router = APIRouter()

@user_router.get('/user', tags=['user'], summary="get user", description="get user")
def create_user():
    return {"message": 'get user'}

@user_router.post('/user', tags=['user'], summary="create a new user", description="create a new user")
def create_user():
    return {"message": 'create a new user'}

@user_router.patch('/user', tags=['user'], summary="update user", description="update user")
def create_user():
    return {"message": 'update user"'}

@user_router.delete('/user', tags=['user'], summary="delete user", description="delete user")
def create_user():
    return {"message": 'delete user'}