from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class Model(BaseModel):
    is_active :Optional[bool] = True
    is_deleted :Optional[bool]= False

    class Config:
        orm_mode = True

class UserModel(Model):
    prefix :Optional[str] = None
    first_name : Optional[str] = None
    middle_name : Optional[str] = None
    last_name : Optional[str] = None
    email : Optional[str] = None
    ssn:Optional[str] = None
    phone_number : Optional[int] = 0
    home_number : Optional[int] = 0
    phone_number_verified : Optional[bool] =False
    home_number_verified : Optional[bool]= False
    date_of_birth : Optional[datetime] = None
    meta_data : Optional[Dict] ={}
    created_by : Optional[str]= None

class UserResponseModel(UserModel):
    id : Optional[int] 




    