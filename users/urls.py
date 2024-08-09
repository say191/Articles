from users.apps import UsersConfig
from django.urls import path
from users.views import UserRegisterApiView

app_name = UsersConfig.name

urlpatterns = [
    path('sign/', UserRegisterApiView.as_view(), name='user_register'),
]