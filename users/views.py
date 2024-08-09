from rest_framework.viewsets import generics
from users.serializers import UserSerializer
from django.contrib.auth.models import Group


class UserRegisterApiView(generics.CreateAPIView):
    """
    Контроллер для регистрации (создания) пользователя
    """

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """
        Метод переопределяет стандартное поведение метода `create` и позволяет
        дополнительно настраивать процесс создания объекта. Вызывается при
        успешной валидации данных и готовности к созданию нового пользователя через
        заданный сериализатор

        Args:
            serializer (Serializer): Сериализатор, содержащий проверенные данные для
            создания нового пользователя.

        Returns:
            None
        """

        user = serializer.save()
        group, created = Group.objects.get_or_create(name='subscriber')
        user.groups.add(group)
        user.save()
