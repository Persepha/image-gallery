from django.urls import path

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

from users.views import UserDetailApi, UserListApi

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user/', UserDetailsView.as_view()),
    path('users/', UserListApi.as_view()),
    path('users/<str:username>/', UserDetailApi.as_view()),
]
