from rest_framework.viewsets import generics
from articles.serializers import ArticleSerializer
from articles.models import Article
from users.permissions import IsAuthor, IsOwner
from datetime import datetime
from rest_framework.exceptions import PermissionDenied


class ArticleCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания статьи. Статью может создать только пользователи,
    имеющие роль автора
    """

    serializer_class = ArticleSerializer
    permission_classes = [IsAuthor, ]

    def perform_create(self, serializer):
        """
        Метод переопределяет стандартное поведение метода `create` и позволяет
        дополнительно настраивать процесс создания объекта

        Args:
        - serializer (Serializer): Сериализатор, используемый для
          валидации и создания нового объекта.

        Returns:
        - None
        """

        article = serializer.save()
        article.author = self.request.user
        article.published_date = datetime.now().date()
        article.save()


class ArticleListApiView(generics.ListAPIView):
    """
    Контроллер для отображения списка статьей. В случае если неавторизованный пользователь
    или пользователь, не имеющую роль подписчика сделает запрос, то ему отобразится список из
    публичных статьей. В случае, если запрос сделает пользователь с ролью подписичка - ему
    отобразится список все статьей, включая и привытные (is_public=False)
    """

    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Этот метод переопределяет стандартный метод `get_queryset` в  Django Rest Framework,
        чтобы предоставить различное поведение в зависимости от того, является ли
        текущий пользователь аутентифицированным и входит ли он в группу 'subscriber'

        Returns:
        - QuerySet: Возвращает QuerySet для объектов модели `Article`
        """

        user = self.request.user

        if user.is_authenticated and user.groups.filter(name='subscriber').exists():
            return Article.objects.all()

        return Article.objects.filter(is_public=True)


class ArticleRetrieveApiView(generics.RetrieveAPIView):
    """
    Контроллер для отображения выбранной статьи. У неавторизованного пользователя и пользователя
    без роли подписчика нету доступа на просмотр закрытой статьи статьи, когда наоборот
    пользователь с ролью подписчика может просматривать любую статью в том числе и закрытую
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_object(self):
        """
        Метод переопределяет стандартный метод `get_object` в Django Rest Framework, чтобы
        добавить логику проверки доступа к статье на основе её публичности и статуса
        подписки пользователя
        """

        user = self.request.user
        article = super().get_object()

        if not article.is_public:
            if not (user.is_authenticated and user.groups.filter(name='subscriber').exists()):
                raise PermissionDenied("У вас нету доступа к этой статье, для получения доступа оформите подписку")

        return article


class ArticleUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения статьи. Изменять статью может только ее владелец
    (автор, кто ее написал)
    """

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsOwner, ]


class ArticleDeleteAPIView(generics.DestroyAPIView):
    """
    Контроллер для изменения статьи. Изменять статью может только ее владелец
    (автор, кто ее написал)
    """

    queryset = Article.objects.all()
    permission_classes = [IsOwner, ]
