from rest_framework import serializers

from .models.image import Image


class ImageInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField(required=False)

    def validate_slug(self, value):
        if value == 'create':
            raise serializers.ValidationError('Slug cannot be create')

        if Image.objects.filter(slug__iexact=value).exists():
            raise serializers.ValidationError('Slug already exists')

        return value
