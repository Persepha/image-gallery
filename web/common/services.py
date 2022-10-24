from datetime import datetime
from typing import List, Dict, Any, Tuple

from slugify import slugify

from common.types import DjangoModelType


def generate_slug(name: str) -> str:
    return f'{str(int(datetime.now().timestamp()))}-{slugify(name)}'


def model_update(
    *,
    instance: DjangoModelType,
    fields: List[str],
    data: Dict[str, Any],
) -> Tuple[DjangoModelType, bool]:
    has_updated = False

    for field in fields:
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    if has_updated:
        instance.full_clean()
        instance.save(update_fields=fields)

    return instance, has_updated
