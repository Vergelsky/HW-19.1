from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, items

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts', contacts, name='contacts'),
    path('items', items, name='items'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




