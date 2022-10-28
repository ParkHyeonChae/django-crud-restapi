from apps.boards.api.serializers.comments import comment_serializer
from apps.boards.models.posts import Post


def post_serializer(post: Post) -> dict:
    """post serializer"""

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "viewCount": post.view_count,
        "createdAt": post.created_at,
    }


def post_list_serializer(post: Post) -> dict:
    """post list serializer"""

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "viewCount": post.view_count,
        "commentCount": post._comment_count,
        "createdAt": post.created_at,
    }


def post_detail_serializer(post: Post) -> dict:
    """post detail serializer"""

    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "viewCount": post.view_count,
        "createdAt": post.created_at,
        "comments": [
            comment_serializer(comment=comment)
            for comment in post.prefetch_post_comments
        ],
    }
