from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import LimitOffsetPagination, get_paginated_response
from gallery.selectors import image_list_with_tags
from gallery.serializers import ImageInputSerializer, ImageOutputSerializer, ImageOutputFilterSerializer
from gallery.services import image_create


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
