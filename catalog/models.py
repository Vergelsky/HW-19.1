
from django.db import models
from django.utils import timezone, text

from users.models import User


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=120, verbose_name='Название')
    product_description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)
    changed_at = models.DateTimeField(verbose_name='Изменено', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_name = models.CharField(max_length=120, verbose_name='Название')
    category_description = models.TextField(max_length=600, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)

    def __str__(self):
        return self.category_name
