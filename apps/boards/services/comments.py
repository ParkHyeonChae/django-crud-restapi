from apps.boards.exceptions import comments as comment_error
from apps.boards.models.comments import Comment
from apps.boards.selectors.comments import get_comment_by_id_and_post_id
from django.utils import timezone


def create_comment(post_id: int, user_id: int, content: str) -> Comment:
    """create comment service"""

    if content is None:
        raise comment_error.RequiredCommentContentError
    comment = Comment.objects.create(
        post_id=post_id,
        user_id=user_id,
        content=content,
        created_at=timezone.now(),
    )
    return comment


def update_comment(
    user_id: int, comment_id: int, post_id: int, board_id: int, content: str
) -> Comment:
    """update comment service"""

    comment = get_comment_by_id_and_post_id(
        comment_id=comment_id, post_id=post_id, board_id=board_id
    )
    if comment.user_id != user_id:
        raise comment_error.PermissionDeniedUpdateCommentError
    if content is None:
        raise comment_error.RequiredCommentContentError
    comment.content = content
    comment.updated_at = timezone.now()
    comment.save()
    return comment


def delete_comment(user_id: int, comment_id: int, post_id: int, board_id: int) -> None:
    """delete comment service"""

    comment = get_comment_by_id_and_post_id(
        comment_id=comment_id, post_id=post_id, board_id=board_id
    )
    if comment.user_id != user_id:
        raise comment_error.PermissionDeniedDeleteCommentError
    comment.deleted_at = timezone.now()
    comment.save()
    return None
