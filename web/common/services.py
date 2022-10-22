from datetime import datetime

from slugify import slugify


def generate_slug(name: str) -> str:
    return f'{str(int(datetime.now().timestamp()))}-{slugify(name)}'
