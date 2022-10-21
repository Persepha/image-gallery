from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Image(TimeStampedModel):
    name = models.CharField(
        db_index=True,
        max_length=200,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text='Optional field. If the field is empty, it will be generated automatically based on the image name',
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='my_images',
    )

    def __str__(self):
        return self.name
