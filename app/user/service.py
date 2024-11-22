from app.user.repository import database
from app.user.user import UserDB, UserSchema, UserSchemaResponse, UserSchemaResponseWMsg
from app.user import repository
from app.utils.messages import ResponseMessage


def create_user(user: UserSchema) -> UserSchemaResponseWMsg:
    user_db = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )
    created_user = repository.create_user(user_db)
    return UserSchemaResponseWMsg(
        **created_user.model_dump(),
        message=ResponseMessage.USER_CREATED
    )


def get_users() -> list[UserSchemaResponse]:
    users = repository.get_users()
    return list(map(
         lambda user: UserSchemaResponse(**user.model_dump()),
         users
    ))