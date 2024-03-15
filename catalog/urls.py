from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryCreateView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', index, name='index'),
                  path('contacts', contacts, name='contacts'),
                  path('catalog', ProductListView.as_view(), name='catalog'),
                  path('new/', ProductCreateView.as_view(), name='new'),
                  path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
                  path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
                  path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
                  path('new_ver/', CategoryCreateView.as_view(), name='new_category')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
