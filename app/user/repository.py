from app.user.user import UserDB


database = []


def create_user(user: UserDB) -> UserDB:
    database.append(user)
    return user


def get_users() -> list[UserDB]: return database