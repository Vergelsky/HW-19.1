from django.contrib import admin

from blog.models import Version


# Register your models here.

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'product', 'version_number', 'is_current')