from typing import Tuple

from apps.users.exceptions import users as user_error
from apps.users.models.users import User
from apps.users.selectors.users import check_is_exist_user_by_email, get_user_by_email
from apps.users.services.auth import check_password, make_password
from django.utils import timezone
from rest_auth.utils import jwt_encode


def login_user(email: str, password: str) -> Tuple[User, str]:
    """login user service"""

    if not email or not password:
        raise user_error.RequiredUserSigninFieldError
    user = get_user_by_email(email=email)
    if check_password(password=password, encoded=user.password) is False:
        raise user_error.InvalidSigninCredentialsError
    if user.is_active is False:
        raise user_error.NotActiveUserError
    if user.dormanted_at is not None:
        raise user_error.IsDormantUserError

    user.last_login = timezone.now()
    user.save()

    token = jwt_encode(user=user)
    return user, token


def create_user(email: str, password: str) -> Tuple[User, str]:
    """create user service"""

    if not email or not password:
        raise user_error.RequiredUserSignupFieldError
    if check_is_exist_user_by_email(email=email) is True:
        raise user_error.IsAlreadyExistUserEmailError
    current_time = timezone.now()
    user = User.objects.create(
        email=email,
        password=make_password(password=password),
        last_login=current_time,
        created_at=current_time,
    )
    token = jwt_encode(user=user)
    return user, token
