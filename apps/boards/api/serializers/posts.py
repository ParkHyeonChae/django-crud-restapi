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
