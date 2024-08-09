from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс UserAdmin для отображения  всех пользователей в панеле администратора
    с возможностью поиска пользователя по емейлу
    """

    list_display = ['email', 'is_active', 'first_name', 'last_name']
    search_fields = ['email']
