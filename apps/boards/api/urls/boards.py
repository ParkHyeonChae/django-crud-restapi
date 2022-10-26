from django.urls import path
from apps.boards.api.views.boards import BoardList

urlpatterns = [
    path("api/v1/boards", BoardList.as_view()),
]
