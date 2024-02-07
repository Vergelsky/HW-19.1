from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, VersionCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('new/', BlogCreateView.as_view(), name='new'),
    path('blog', BlogListView.as_view(), name='blog'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
    path('new_ver/', VersionCreateView.as_view(), name='new_ver')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

