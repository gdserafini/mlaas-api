from pydantic import BaseModel, EmailStr


class User:
    pass


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserSchemaResponse(BaseModel):
    username: str
    email: str
    message: str
