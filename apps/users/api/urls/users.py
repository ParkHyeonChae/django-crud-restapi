from apps.users.api.views.users import UserSigninAction, UserSignupAction
from django.urls import path

urlpatterns = [
    path("api/v1/users/signin", UserSigninAction.as_view()),
    path("api/v1/users/signup", UserSignupAction.as_view()),
]
