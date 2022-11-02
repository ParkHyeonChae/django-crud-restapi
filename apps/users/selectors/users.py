from apps.users.exceptions import users as user_error
from apps.users.models.users import User


def get_user_by_email(email: str) -> User:
    """user by email selector"""

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise user_error.NotFoundUserError
    return user


def check_is_exist_user_by_email(email: str) -> bool:
    """check is exist user by email selector"""

    return User.objects.filter(email=email).exists()
