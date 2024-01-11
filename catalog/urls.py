from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import index, contacts, items

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('items', items)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




