from rest_framework.views import APIView
from rest_framework.response import Response


class UserSigninAction(APIView):
    """user signin view"""

    def post(self, request, *args, **kwargs) -> Response:
        pass


class UserSignupAction(APIView):
    """user signup view"""
    pass
