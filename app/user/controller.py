from fastapi import APIRouter
from http import HTTPStatus
from app.user import service
from app.user.user import UserSchema, UserSchemaResponse, UserDB, UserSchemaResponseWMsg

router = APIRouter()


@router.post(
    '/user',
    status_code=HTTPStatus.CREATED,
    response_model=UserSchemaResponseWMsg
)
def create_user(user: UserSchema) -> UserSchemaResponseWMsg:
    return service.create_user(user)


@router.get(
    '/users',
    status_code=HTTPStatus.OK,
    response_model=list[UserSchemaResponse]
)
def get_users() -> list[UserSchemaResponse]:
    return service.get_users()