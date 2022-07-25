from django.urls import path, include
from .views import create_article_view
urlpatterns = [
    path('create/', create_article_view, name="aricle_path"),
]
