from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from common.pagination import LimitOffsetPagination, get_paginated_response
from users.selectors import user_list
from users.serializers import UserOutputFilterSerializer, UserOutputSerializer, \
    UserDetailOutputSerializer

UserModel = get_user_model()


class UserListApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 16

    def get(self, request):
        filters_serializer = UserOutputFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=UserOutputSerializer,
            queryset=users,
            request=request,
            view=self,
        )


class UserDetailApi(APIView):
    def get(self, request, username):
        user = get_object_or_404(UserModel, username=username)
        serializer = UserDetailOutputSerializer(user)

        return Response(serializer.data)
