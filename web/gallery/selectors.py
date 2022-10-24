from typing import Iterable

from .filters import BaseImageFilter
from .models.image import Image


def image_list_with_tags(*, filters=None) -> Iterable[Image]:
    filters = filters or {}

    qs = Image.objects.all()\
        .select_related('owner').prefetch_related('tags')

    return BaseImageFilter(filters, qs).qs
