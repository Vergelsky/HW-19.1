import os

from django import template
from django.core.files.storage import default_storage

from config.settings import MEDIA_ROOT

register = template.Library()


@register.filter
def mediapath(val):
    img_url = os.path.join(MEDIA_ROOT, *str(val).split('/'))
    if default_storage.exists(img_url):
        return val.url
    else:
        return "../static/img_nof_found.png"

