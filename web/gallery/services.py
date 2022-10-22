from django.conf import settings

from .models.image import Image


def image_create(
    *,
    name: str,
    slug: str = '',
    owner: settings.AUTH_USER_MODEL,
) -> Image:
    image = Image(name=name, slug=slug, owner=owner)
    image.full_clean()
    image.save()

    return image
