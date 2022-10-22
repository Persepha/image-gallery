from rest_framework import serializers

from .models.image import Image


class TagOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class ImageOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.SlugField()
    owner_username = serializers.CharField(source='owner.username',
                                           read_only=True)

    tags = TagOutputSerializer(many=True, read_only=True)


class ImageInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField(required=False)

    def validate_slug(self, value):
        if value == 'create':
            raise serializers.ValidationError('Slug cannot be create')

        if Image.objects.filter(slug__iexact=value).exists():
            raise serializers.ValidationError('Slug already exists')

        return value
