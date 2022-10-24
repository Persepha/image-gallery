from django.urls import path

from .views import (
    ImageListApi,
    ImageCreateApi,
    ImageDetailApi,
    ImageDeleteApi,
)

urlpatterns = [
    path('', ImageListApi.as_view(), name='image-list'),
    path('<slug:slug>/', ImageDetailApi.as_view(), name='image-detail'),
    path('create/', ImageCreateApi.as_view(), name='image-create'),
    path('<slug:slug>/delete/', ImageDeleteApi.as_view(), name='image-delete'),
]
