from apps.users.api.serializers.users import user_serializer
from apps.users.exceptions import data as exception_data
from apps.users.exceptions import users as user_error
from apps.users.services.users import create_user, login_user
from apps.utils.exceptions import classes as exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserSigninAction(APIView):
    """user signin view"""

    authentication_classes = ()

    def post(self, request, *args, **kwargs) -> Response:
        try:
            user, token = login_user(
                email=self.request.data.get("email"),
                password=self.request.data.get("password"),
            )
        except user_error.RequiredUserSigninFieldError:
            raise exceptions.BadRequest(
                **exception_data.HTTP_400_INVALID_USER_SIGNIN_BODY
            )
        except user_error.IsDormantUserError:
            raise exceptions.BadRequest(**exception_data.HTTP_400_IS_DORMANT_USER)
        except (
            user_error.InvalidSigninCredentialsError,
            user_error.NotActiveUserError,
            user_error.NotFoundUserError,
        ):
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_AUTHENTICATION_FAILED
            )
        return Response(
            status=status.HTTP_200_OK,
            data={"token": token, "user": user_serializer(user=user)},
        )


class UserSignupAction(APIView):
    """user signup view"""

    authentication_classes = ()

    def post(self, request, *args, **kwargs) -> Response:
        try:
            user, token = create_user(
                email=self.request.data.get("email"),
                password=self.request.data.get("password"),
            )
        except user_error.RequiredUserSignupFieldError:
            raise exceptions.BadRequest(
                **exception_data.HTTP_400_INVALID_USER_SIGNUP_BODY
            )
        except user_error.IsAlreadyExistUserEmailError:
            raise exceptions.BadRequest(
                **exception_data.HTTP_400_IS_ALREADY_EXIST_USER_EMAIL
            )
        return Response(
            status=status.HTTP_201_CREATED,
            data={"token": token, "user": user_serializer(user=user)},
        )
