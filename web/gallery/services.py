from typing import Iterable

from django.conf import settings

from .models.image import Image
from .models.tag import Tag


def tags_create(*, tags: str) -> Iterable[Tag]:
    tags = tags.strip(',').split(',')

    tag_items = []

    for tag in tags:
        tag = tag.strip()
        obj, _ = Tag.objects.get_or_create(title=tag)
        tag_items.append(obj)

    return tag_items


def image_create(
    *,
    name: str,
    slug: str = '',
    owner: settings.AUTH_USER_MODEL,
    tags: str = None,
) -> Image:
    image = Image(name=name, slug=slug, owner=owner)
    image.full_clean()
    image.save()

    if tags is not None:
        tag_list: Iterable[Tag] = tags_create(tags=tags)
        image.tags.add(*tag_list)

    return image
