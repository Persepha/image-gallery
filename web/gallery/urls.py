from django.urls import path

from .views import (
    ImageCreateApi,
)

urlpatterns = [
    path('create/', ImageCreateApi.as_view(), name='image-create'),
]
