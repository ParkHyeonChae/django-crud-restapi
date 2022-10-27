from apps.boards.models.comments import Comment
from django.db.models import QuerySet
from typing import Optional


def get_comment_queryset() -> QuerySet[Optional[Comment]]:
    """comment queryset selector"""

    return Comment.objects.defer("updated_at").filter(deleted_at__isnull=True)
