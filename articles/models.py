from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    """
        Модель статьи, которая включает себя набор полей, таких как: название, содержание,
        автор, дата публикации и признак публичности, который при значении True позволяет
        неавторизованным пользователем видеть данную статью и при значении False ограничивает
        видимость статьи только для пользователей с ролью подписчика
        """

    title = models.CharField(max_length=100, verbose_name='название')
    content = models.TextField(max_length=1000, verbose_name='содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    published_date = models.DateField(verbose_name='дата публикации', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='публичность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
