import django_filters
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class BaseUserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserModel
        fields = ('username', )
