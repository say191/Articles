from articles.apps import ArticlesConfig
from django.urls import path
from articles import views

app_name = ArticlesConfig.name

urlpatterns = [
    path('create/', views.ArticleCreateAPIView.as_view(), name='artile_create'),
    path('', views.ArticleListApiView.as_view(), name='List_article'),
    path('<int:pk>/', views.ArticleRetrieveApiView.as_view(), name='get_article'),
    path('update/<int:pk>/', views.ArticleUpdateAPIView.as_view(), name='update_article'),
    path('delete/<int:pk>/', views.ArticleDeleteAPIView.as_view(), name='delete_article')
]