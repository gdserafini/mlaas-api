from pydantic import BaseModel, EmailStr


class User:
    pass


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserSchemaResponse(BaseModel):
    id: int
    username: str
    email: str


class UserSchemaResponseWMsg(UserSchemaResponse):
    message: str


class UserDB(UserSchema):
    id: int