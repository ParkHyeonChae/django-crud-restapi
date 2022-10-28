from typing import Optional

from apps.boards.exceptions import comments as comment_error
from apps.boards.models.comments import Comment
from django.db.models import QuerySet


def get_comment_queryset() -> QuerySet[Optional[Comment]]:
    """comment queryset selector"""

    return Comment.objects.defer("updated_at").filter(deleted_at__isnull=True)


def get_comment_queryset_by_board_id_and_post_id(
    board_id: int, post_id: int
) -> QuerySet[Optional[Comment]]:
    """comment queryset by board id and post id selector"""

    return Comment.objects.defer("updated_at").filter(
        post__board_id=board_id, post_id=post_id, deleted_at__isnull=True
    )


def get_comment_by_id_and_post_id(
    comment_id: int, post_id: int, board_id: int
) -> Comment:
    """comment by id and post id selector"""

    try:
        comment = (
            Comment.objects.defer("updated_at")
            .filter(
                id=comment_id,
                post_id=post_id,
                post__board_id=board_id,
                deleted_at__isnull=True,
            )
            .get()
        )
    except Comment.DoesNotExist:
        raise comment_error.NotFoundCommentError
    return comment
