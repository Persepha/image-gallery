from django.contrib import admin

from .models.image import Image


@admin.register(Image)
class ImageItemAdmin(admin.ModelAdmin):
    pass
