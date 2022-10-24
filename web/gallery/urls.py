from django.urls import path

from .views import (
    ImageListApi,
    ImageCreateApi,
    ImageDetailApi,
)

urlpatterns = [
    path('', ImageListApi.as_view(), name='image-list'),
    path('<slug:slug>/', ImageDetailApi.as_view(), name='image-detail'),
    path('create/', ImageCreateApi.as_view(), name='image-create'),
]
