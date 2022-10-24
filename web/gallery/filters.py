from django.db.models import Q

import django_filters

from gallery.models.image import Image


class BaseImageFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(method='custom_in_filter', field_name='tags__title')

    def custom_in_filter(self, queryset, name, value):
        query = Q()
        for position in value.split(','):
            query |= Q(**{f'{name}__icontains': position})
        return queryset.filter(query)

    class Meta:
        model = Image
        fields = ('id', 'name')
