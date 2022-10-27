from typing import Optional

from apps.boards.exceptions import posts as post_error
from apps.boards.models.posts import Post
from django.db.models import QuerySet


def get_post_queryset_by_board_id(board_id: int) -> QuerySet[Optional[Post]]:
    """post queryset selector"""

    return Post.objects.defer("updated_at").filter(
        board_id=board_id, deleted_at__isnull=True
    )


def get_post_by_id_and_board_id(post_id: int, board_id: int) -> Post:
    """post selector"""

    try:
        post = Post.objects.defer("updated_at").filter(
            id=post_id, board_id=board_id, deleted_at__isnull=True
        ).get()
    except Post.DoesNotExist:
        raise post_error.NotFoundPostError
    return post


def get_post_by_id_and_user_id_and_board_id(
    post_id: int, user_id: int, board_id: int
) -> Post:
    """post by user_id selector"""

    try:
        post = Post.objects.defer("updated_at").filter(
            id=post_id, user_id=user_id, board_id=board_id, deleted_at__isnull=True
        ).get()
    except Post.DoesNotExist:
        raise post_error.NotFoundPostError
    return post
