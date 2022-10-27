from apps.boards.api.views.boards import BoardList
from django.urls import path

urlpatterns = [
    path("api/v1/boards", BoardList.as_view()),
]
