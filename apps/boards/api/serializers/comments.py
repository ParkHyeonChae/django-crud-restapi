from apps.boards.models.comments import Comment


def comment_serializer(comment: Comment) -> dict:
    """comment serializer"""

    return {
        "id": comment.id,
        "content": comment.content,
        "createdAt": comment.created_at,
    }


def comment_list_serializer(comment: Comment) -> dict:
    """comment list serializer"""

    return {
        "id": comment.id,
        "content": comment.content,
        "createdAt": comment.created_at,
    }


def comment_detail_serializer(comment: Comment) -> dict:
    """comment detail serializer"""

    return {
        "id": comment.id,
        "content": comment.content,
        "createdAt": comment.created_at,
    }
