
from django.db import models
from django.utils import timezone, text

def rus_to_slug(rus_string):
    """
    Превращает текст в слаг, переводя русские буквы в транслит
    :param rus_string: текст для слагирования
    :return: слаг, готовый для вставки в url
    """

    rus_abc = ('абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
    slug_abc = ('a', 'b', 'v', 'g', 'd', 'e', 'jo', 'zh', 'z', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f',
                'h', 'c', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'ju', 'ja')
    trance_table = {}
    for num in range(len(rus_abc)):
        letter = rus_abc[num]
        trance_table[ord(letter)] = slug_abc[num]

    result = rus_string.lower().translate(trance_table)

    return text.slugify(result)


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=120, verbose_name='Название')
    product_description = models.CharField(max_length=600, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)
    changed_at = models.DateTimeField(verbose_name='Изменено', default=timezone.now)

    def __str__(self):
        return self.product_name


class Category(models.Model):
    category_name = models.CharField(max_length=120, verbose_name='Название')
    category_description = models.TextField(max_length=600, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)

    def __str__(self):
        return self.category_name
