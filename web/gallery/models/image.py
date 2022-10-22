from django.conf import settings
from django.db import models

from common.models import TimeStampedModel
from common.services import generate_slug


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(str(self.name))
        super().save(*args, **kwargs)
