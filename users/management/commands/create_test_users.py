from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user1@sky.pro',
            first_name='user',
            last_name='1',
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('1qaz2wsx')
        user.save()

        user = User.objects.create(
            email='moder1@sky.pro',
            first_name='moder',
            last_name='1',
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('1qaz2wsx')
        user.save()


