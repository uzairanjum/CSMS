#  here 

from pydantic import  Field




class Settings():
    environment :str = Field(env = "Environment", default = "")
    version :str = Field(env = "Environment", default = "")

class AppSetting(Settings):
    database_url:str = Field(env = "DATABASE_URL", default = "")
    