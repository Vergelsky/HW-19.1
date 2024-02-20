from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    country = models.CharField(max_length=70, verbose_name='страна', null=True, blank=True)
    verification_code = models.CharField(max_length=50, verbose_name='код верификации пользователя', null=True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


