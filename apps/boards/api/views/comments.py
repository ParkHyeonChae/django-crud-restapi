from apps.boards.api.serializers.comments import (
    comment_detail_serializer,
    comment_list_serializer,
    comment_serializer,
)
from apps.boards.exceptions import comments as comment_error
from apps.boards.exceptions import data as exception_data
from apps.boards.selectors.comments import (
    get_comment_by_id_and_post_id,
    get_comment_queryset_by_board_id_and_post_id,
)
from apps.boards.services.comments import create_comment, delete_comment, update_comment
from apps.utils.exceptions import classes as exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class CommentListCreate(APIView):
    """comment list create view"""

    authentication_classes = [JSONWebTokenAuthentication]

    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_NOT_AUTHENTICATED
            )

    def get(self, request, *args, **kwrags) -> Response:
        """
        해당 게시글에 대한 댓글 목록을 반환합니다.
        QueryStrings:
            page: default 1
            limit: default 10
        Returns:
            200: success
        """
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        comment_queryset = get_comment_queryset_by_board_id_and_post_id(
            board_id=int(self.kwargs.get("board_id")),
            post_id=int(self.kwargs.get("post_id")),
        )[(page * limit) - limit:limit * page]
        return Response(
            status=status.HTTP_200_OK,
            data={
                "comments": [
                    comment_list_serializer(comment=comment)
                    for comment in comment_queryset
                ]
            },
        )

    def post(self, request, *args, **kwargs) -> Response:
        """
        해당 게시글에 댓글을 작성하고 작성된 댓글을 반환합니다.
        QueryStrings:
            page: default 1
            limit: default 10
        Returns:
            201: success
            400: content 바디 값이 None일 시
        """
        try:
            comment = create_comment(
                post_id=int(self.kwargs.get("post_id")),
                user_id=self.request.user.id,
                content=self.request.data.get("content", None),
            )
        except comment_error.RequiredCommentContentError:
            raise exceptions.BadRequest(**exception_data.HTTP_400_INVALID_COMMENT_BODY)
        return Response(
            status=status.HTTP_201_CREATED, data=comment_serializer(comment=comment)
        )


class CommentRetrieveUpdateDestroy(APIView):
    """comment retrieve update destroy view"""

    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_NOT_AUTHENTICATED
            )

    def get(self, request, *args, **kwrags) -> Response:
        """
        해당 게시판, 게시글, 댓글 아이디에 해당하는 댓글 반환합니다.
        Returns:
            200: success
            404: NotFound
        """
        try:
            comment = get_comment_by_id_and_post_id(
                comment_id=int(self.kwargs.get("comment_id")),
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
            )
        except comment_error.NotFoundCommentError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_COMMENT)
        return Response(
            status=status.HTTP_200_OK, data=comment_detail_serializer(comment=comment)
        )

    def put(self, request, *args, **kwrags) -> Response:
        """
        본인의 댓글을 수정합니다.
        Returns:
            200: success
            400: title, content 바디 값이 None일 시
            404: Not Found
            403: 본인의 댓글이 아닌 경우
        """
        try:
            comment = update_comment(
                user_id=self.request.user.id,
                comment_id=int(self.kwargs.get("comment_id")),
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
                content=self.request.data.get("content", None),
            )
        except comment_error.NotFoundCommentError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_COMMENT)
        except comment_error.PermissionDeniedUpdateCommentError:
            raise exceptions.PermissionDenied(
                **exception_data.HTTP_403_PERMISSION_DENIED_UPDATE_COMMENT
            )
        except comment_error.RequiredCommentContentError:
            raise exceptions.BadRequest(**exception_data.HTTP_400_INVALID_COMMENT_BODY)
        return Response(
            status=status.HTTP_200_OK, data=comment_serializer(comment=comment)
        )

    def delete(self, request, *args, **kwrags) -> Response:
        """
        본인의 댓글을 삭제합니다.
        Returns:
            204: success
            404: Not Found
            403: 본인의 댓글이 아닌 경우
        """
        try:
            delete_comment(
                user_id=self.request.user.id,
                comment_id=int(self.kwargs.get("comment_id")),
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
            )
        except comment_error.NotFoundCommentError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_COMMENT)
        except comment_error.PermissionDeniedDeleteCommentError:
            raise exceptions.PermissionDenied(
                **exception_data.HTTP_403_PERMISSION_DENIED_DELETE_COMMENT
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
