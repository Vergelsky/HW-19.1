from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    content = models.TextField(verbose_name='содержимое')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return f'Публикация "{self.title}"'

