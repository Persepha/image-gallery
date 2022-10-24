from django.urls import path

from .views import (
    ImageListApi,
    ImageCreateApi,
    ImageDetailApi,
    ImageDeleteApi,
    ImageUpdateApi,
)

urlpatterns = [
    path('', ImageListApi.as_view(), name='image-list'),
    path('<slug:slug>/', ImageDetailApi.as_view(), name='image-detail'),
    path('create/', ImageCreateApi.as_view(), name='image-create'),
    path('<slug:slug>/update/', ImageUpdateApi.as_view(), name='image-update'),
    path('<slug:slug>/delete/', ImageDeleteApi.as_view(), name='image-delete'),
]
