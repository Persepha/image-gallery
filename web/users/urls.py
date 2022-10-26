from django.urls import path, include

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView


urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
