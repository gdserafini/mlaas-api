from fastapi import APIRouter
from http import HTTPStatus
from app.user.user import UserSchema, UserSchemaResponse


router = APIRouter()


@router.post(
    '/user',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaResponse
)
def create_user(user: UserSchema):
    return UserSchemaResponse(
        username=user.username,
        email=user.email,
        message='User created.'
    )
