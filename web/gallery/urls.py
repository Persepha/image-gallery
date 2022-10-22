from django.urls import path

from .views import (
    ImageListApi,
    ImageCreateApi,
)

urlpatterns = [
    path('', ImageListApi.as_view(), name='image-list'),
    path('create/', ImageCreateApi.as_view(), name='image-create'),
]
