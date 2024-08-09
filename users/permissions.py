from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    """
    класс представляет собой пользовательский пермишен на основе базового пермишена
    BasePermission из Django REST Framework. Его цель - проверка, является ли
    текущий пользователь членом группы 'author'
    """

    def has_permission(self, request, view):
        """
        Метод проверяет, принадлежит ли текущий пользователь группе 'author'

        Args:
        - request: текущий HTTP запрос
        - view: текущее представление

        Returns:
        - bool: True, если пользователь принадлежит группе 'author', иначе False
        """

        return request.user.groups.filter(name='author').exists()


class IsOwner(BasePermission):
    """
    Класс представляет собой пользовательский пермишен на основе базового пермишена
    BasePermission из Django REST Framework. Его цель - проверка, является ли
    текущий пользователь владельцем статьи
    """

    def has_object_permission(self, request, view, obj):
        """
        Метод проверяет, обладает ли текущий пользователь разрешением на доступ к
        выбранной статье

        Args:
        - request: HttpRequest объект, представляющий текущий запрос
        - view: Представление, для которого проверяется доступ
        - obj: Объект, для которого проверяется разрешение

        Returns:
        - bool: Возвращает True, если текущий пользователь является
          владельцем статьи, иначе возвращает False.
        """
        return request.user == obj.author
