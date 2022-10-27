from apps.boards.exceptions import posts as post_error
from apps.boards.models.posts import Post
from apps.boards.selectors.posts import get_post_by_id_and_user_id_and_board_id
from config.celery import app as celery
from django.db.models import F
from django.utils import timezone


def create_post(board_id: int, user_id: int, title: str, content: str) -> Post:
    """create post service"""

    if title is None:
        raise post_error.RequiredPostTitleError
    if content is None:
        raise post_error.RequiredPostContentError
    post = Post.objects.create(
        board_id=board_id,
        user_id=user_id,
        title=title,
        content=content,
        created_at=timezone.now(),
    )
    return post


def update_post(
    user_id: int, post_id: int, board_id: int, title: str, content: str
) -> Post:
    """update post service"""

    post = get_post_by_id_and_user_id_and_board_id(
        post_id=post_id, user_id=user_id, board_id=board_id
    )
    if title is None:
        raise post_error.RequiredPostTitleError
    if content is None:
        raise post_error.RequiredPostContentError
    post.title = title
    post.content = content
    post.updated_at = timezone.now()
    post.save()
    return post


def delete_post(user_id: int, post_id: int, board_id: int) -> None:
    """delete post service"""

    post = get_post_by_id_and_user_id_and_board_id(
        post_id=post_id, user_id=user_id, board_id=board_id
    )
    post.deleted_at = timezone.now()
    post.save()
    return None


@celery.task(bind=True)
def async_update_post_view_count(self, post_id: int) -> None:
    """async update post view count service"""

    Post.objects.filter(id=post_id).update(view_count=F("view_count") + 1)
    return None
