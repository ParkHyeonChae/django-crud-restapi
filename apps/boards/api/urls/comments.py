from apps.boards.api.views.comments import (
    CommentListCreate,
    CommentRetrieveUpdateDestroy,
)
from django.urls import path

urlpatterns = [
    path(
        "api/v1/boards/<board_id>/posts/<post_id>/comments", CommentListCreate.as_view()
    ),
    path(
        "api/v1/boards/<board_id>/posts/<post_id>/comments/<comment_id>",
        CommentRetrieveUpdateDestroy.as_view(),
    ),
]
