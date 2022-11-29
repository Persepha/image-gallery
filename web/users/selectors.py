from typing import Iterable

from django.contrib.auth import get_user_model

from users.filters import BaseUserFilter

UserModel = get_user_model()


def user_list(*, filters=None) -> Iterable[UserModel]:
    filters = filters or {}

    qs = UserModel.objects.all().select_related('userprofile')

    return BaseUserFilter(filters, qs).qs
