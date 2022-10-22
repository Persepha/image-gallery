from django.contrib import admin

from .models.image import Image
from .models.tag import Tag


@admin.register(Image)
class ImageItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
