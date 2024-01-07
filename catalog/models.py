from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=120, verbose_name='Название')
    product_description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Создано')
    changed_at = models.DateTimeField(verbose_name='Изменено', )

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_name = models.CharField(max_length=120, verbose_name='Название')
    category_description = models.TextField(max_length=600, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', null=True)

    def __str__(self):
        return self.category_name
