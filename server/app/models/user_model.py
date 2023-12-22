from beanie import Document
from pydantic import BaseModel, EmailStr


class Users(Document):
    first_name: str
    last_name: str
    username: EmailStr
    password: hash

    class Settings:
        name = "users"