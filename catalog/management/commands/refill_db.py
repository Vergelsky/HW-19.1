from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        new_fill = [
            {'category_name': 'Категория11', 'category_description': 'Описание категории11'},
            {'category_name': 'Категория111', 'category_description': 'Описание категории111'},
            {'category_name': 'Категория1111', 'category_description': 'Описание категории1111'},
            {'category_name': 'Категория11111', 'category_description': 'Описание категории11111'},
            {'category_name': 'Категория111111', 'category_description': 'Описание категории111111'},
        ]

        Category.objects.all().delete()

        for string in new_fill:
            Category.objects.create(**string)

