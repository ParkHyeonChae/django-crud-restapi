from apps.boards.api.serializers.posts import (
    post_detail_serializer,
    post_list_serializer,
    post_serializer,
)
from apps.boards.exceptions import data as exception_data
from apps.boards.exceptions import posts as post_error
from apps.boards.selectors.posts import (
    get_post_queryset_by_board_id,
    get_post_with_comment_by_id_and_board_id,
)
from apps.boards.services.posts import (
    async_update_post_view_count,
    create_post,
    delete_post,
    update_post,
)
from config import exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PostListCreate(APIView):
    """post list create view"""

    authentication_classes = [JSONWebTokenAuthentication]

    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_NOT_AUTHENTICATED
            )

    def get(self, request, *args, **kwrags) -> Response:
        """
        해당 게시판에 해당하는 게시글 목록을 반환합니다.
        QueryStrings:
            page: default 1
            limit: default 10
        Returns:
            200: success
        """
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        post_queryset = get_post_queryset_by_board_id(
            board_id=int(self.kwargs.get("board_id"))
        )[(page * limit) - limit:limit * page]
        return Response(
            status=status.HTTP_200_OK,
            data={"posts": [post_list_serializer(post=post) for post in post_queryset]},
        )

    def post(self, request, *args, **kwargs) -> Response:
        """
        해당 게시판에 게시글을 작성하고 작성된 게시글을 반환합니다.
        Returns:
            201: success
            400: title, content 바디 값이 None일 시
        """
        try:
            post = create_post(
                board_id=int(self.kwargs.get("board_id")),
                user_id=self.request.user.id,
                title=self.request.data.get("title", None),
                content=self.request.data.get("content", None),
            )
        except (post_error.RequiredPostTitleError, post_error.RequiredPostContentError):
            raise exceptions.BadRequest(**exception_data.HTTP_400_INVALID_POST_BODY)
        return Response(status=status.HTTP_201_CREATED, data=post_serializer(post=post))


class PostRetrieveUpdateDestroy(APIView):
    """post retrieve update destroy view"""

    authentication_classes = [JSONWebTokenAuthentication]

    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                **exception_data.HTTP_401_NOT_AUTHENTICATED
            )

    def get(self, request, *args, **kwrags) -> Response:
        """
        해당 게시판과 게시글 아이디에 해당하는 게시글을 반환하고 조회수를 증가시킵니다.
        Returns:
            200: success
            404: NotFound
        """
        try:
            post = get_post_with_comment_by_id_and_board_id(
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
            )
            async_update_post_view_count.apply_async([post.id])
        except post_error.NotFoundPostError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_POST)
        return Response(
            status=status.HTTP_200_OK, data=post_detail_serializer(post=post)
        )

    def put(self, request, *args, **kwrags) -> Response:
        """
        본인의 게시글을 수정합니다.
        Returns:
            200: success
            400: title, content 바디 값이 None일 시
            404: Not Found
            403: 본인의 게시글이 아닌 경우
        """
        try:
            post = update_post(
                user_id=self.request.user.id,
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
                title=self.request.data.get("title", None),
                content=self.request.data.get("content", None),
            )
        except post_error.NotFoundPostError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_POST)
        except post_error.PermissionDeniedUpdatePostError:
            raise exceptions.PermissionDenied(
                **exception_data.HTTP_403_PERMISSION_DENIED_UPDATE_POST
            )
        except (post_error.RequiredPostTitleError, post_error.RequiredPostContentError):
            raise exceptions.BadRequest(**exception_data.HTTP_400_INVALID_POST_BODY)
        return Response(status=status.HTTP_200_OK, data=post_serializer(post=post))

    def delete(self, request, *args, **kwrags) -> Response:
        """
        본인의 게시글을 삭제합니다.
        Returns:
            204: success
            404: Not Found
            403: 본인의 게시글이 아닌 경우
        """
        try:
            delete_post(
                user_id=self.request.user.id,
                post_id=int(self.kwargs.get("post_id")),
                board_id=int(self.kwargs.get("board_id")),
            )
        except post_error.NotFoundPostError:
            raise exceptions.NotFound(**exception_data.HTTP_404_NOT_FOUND_POST)
        except post_error.PermissionDeniedDeletePostError:
            raise exceptions.PermissionDenied(
                **exception_data.HTTP_403_PERMISSION_DENIED_DELETE_POST
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
