from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.serializers import ImageInputSerializer
from gallery.services import image_create


class ImageCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ImageInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        created_image = image_create(**serializer.validated_data,
                                     owner=user)

        return Response(status=status.HTTP_201_CREATED)
