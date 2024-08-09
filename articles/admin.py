from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Класс ArticleAdmin для отображения всех статьей в панеле администратора
    с возможностью поиска статьи по названию
    """

    list_display = ['title', 'author', 'published_date', 'is_public']
    search_fields = ['title']
