from typing import Iterable
import django_filters

from .models.image import Image


class BaseImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = ('id', 'name')


def image_list_with_tags(*, filters=None) -> Iterable[Image]:
    filters = filters or {}

    qs = Image.objects.all()\
        .select_related('owner').prefetch_related('tags')

    return BaseImageFilter(filters, qs).qs
