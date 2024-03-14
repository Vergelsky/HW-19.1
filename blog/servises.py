from django.conf import settings
from django.core import cache

from blog.models import Version


def get_versions():
    key = 'versions'

    if settings.CACHE_ENABLED:
        versions = cache.get('key')
        if versions:
            return versions
        else:
            versions = Version.objects.all()
            cache.set(key, versions)
            return versions
    else:
        return Version.objects.all()
