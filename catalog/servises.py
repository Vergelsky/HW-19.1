from django.conf import settings
from django.core import cache

from catalog.models import Category


def get_category():
    key = 'category'

    if settings.CACHE_ENABLED:
        category = cache.get('key')
        if category:
            return category
        else:
            category = Category.objects.all()
            cache.set(key, category)
            return category
    else:
        return Category.objects.all()
