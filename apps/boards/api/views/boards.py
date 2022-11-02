from apps.boards.api.serializers.boards import board_serializer
from apps.boards.exceptions import data as exception_data
from apps.boards.selectors.boards import get_board_queryset
from apps.utils.exceptions import classes as exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BoardList(APIView):
    """board list view"""

    authentication_classes = [JSONWebTokenAuthentication]

    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_NOT_AUTHENTICATED
            )

    def get(self, request, *args, **kwrags) -> Response:
        """
        게시판 목록을 반환합니다.
        Returns:
            200: success
        """
        return Response(
            status=status.HTTP_200_OK,
            data={
                "boards": [
                    board_serializer(board=board) for board in get_board_queryset()
                ]
            },
        )
