from users.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
import re


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        """
        Переопределение метода создания пользователя с зашифрованным паролем
        для обеспечения безопасности

        Args:
            validated_data (dict): Проверенные данные, содержащие информацию о новом пользователе,
                                   включая незашифрованный пароль

        Returns:
            User: Созданный пользовательский объект с зашифрованным паролем
        """

        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def validate(self, data):
        """
        Метод для осуществления валидации пароля при создании пользователя, пароль
        должен быть не менее 8 символов и содержать хотябы одну букву и хотя бы одну цифру

        Args:
            data (dict): Словарь, содержащий данные пользователя,
                     включая пароль, который подлежит валидации

        Raises:
            ValidationError: Если пароль не соответствует одним из критериев:
                - Если длина пароля меньше 8 символов.
                - Если пароль не содержит хотя бы одной буквы и
                  хотя бы одной цифры

        Returns:
            dict: Словарь с валидационными данными,
                  если пароль проходит проверки
        """
        password = data.get('password')

        if len(password) < 8:
            raise ValidationError('Длина пароля должна составлять не менее 8 символов')

        if not re.search(r'\d', password) or not re.search(r'[A-Za-z]', password):
            raise ValidationError('Пароль должен содержать хотя бы одну цифру и хотя бы одну букву')

        return data
