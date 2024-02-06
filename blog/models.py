from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=200, verbose_name='название')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(verbose_name='изображение', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', null=True, blank=True, auto_now_add=True)
    views_count = models.IntegerField(default=0, verbose_name='просмотров')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return f'Публикация \"{self.blog_title}\"'


class Version(models.Model):
    version_title = models.CharField(max_length=200, verbose_name='название')
    product = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='содержимое')
    version_number = models.IntegerField(default=0, verbose_name='просмотров')
    is_current = models.BooleanField(default=True, verbose_name='опубликовано')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'Версия №{self.version_number}, \"{self.blog_title}\"'
