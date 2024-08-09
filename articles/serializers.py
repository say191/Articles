from articles.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели статьи
    """

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'published_date', 'author', 'is_public')
