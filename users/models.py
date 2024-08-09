from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя, которая наследуюется от AbstractUser, где поле email
    является уникальным и обязательным, при этом стандартные поля имя и фамилия,
    которые включены в AbstractUser можно оставлять пустыми. Так же поле email
    является основным идентификатором пользователя, что удобно для аутентификации
    """

    username = None
    first_name = models.CharField(max_length=30, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='емейл')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
