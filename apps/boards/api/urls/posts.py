from apps.boards.api.views.posts import PostListCreate, PostRetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path("api/v1/boards/<board_id>/posts", PostListCreate.as_view()),
    path(
        "api/v1/boards/<board_id>/posts/<post_id>", PostRetrieveUpdateDestroy.as_view()
    ),
]
