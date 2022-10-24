from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import LimitOffsetPagination, get_paginated_response
from gallery.models.image import Image
from gallery.permissions import IsOwner
from gallery.selectors import image_list_with_tags
from gallery.serializers import ImageInputSerializer, ImageOutputSerializer, ImageOutputFilterSerializer, \
    ImageUpdateInputSerializer
from gallery.services import image_create, image_delete, image_update


class ImageListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 5

    def get(self, request):
        filters_serializer = ImageOutputFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        images = image_list_with_tags(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=ImageOutputSerializer,
            queryset=images,
            request=request,
            view=self,
        )


class ImageCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ImageInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        tags = None
        if 'tags' in request.data:
            tags = serializer.validated_data.pop('tags')

        created_image = image_create(**serializer.validated_data,
                                     owner=user, tags=tags)

        return Response(status=status.HTTP_201_CREATED)


class ImageDetailApi(APIView):
    def get(self, request, slug):
        image = get_object_or_404(Image, slug=slug)
        serializer = ImageOutputSerializer(image)

        return Response(serializer.data)


class ImageDeleteApi(APIView):
    def delete(self, request, slug):
        image = get_object_or_404(Image, slug=slug)
        image_delete(image=image)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageUpdateApi(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def post(self, request, slug):
        serializer = ImageUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = get_object_or_404(Image, slug=slug)

        self.check_object_permissions(request, image)

        updated_image = image_update(image=image, data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
