from django.urls import path, include
from .views import create_article_view, articles_view, detail_article_view
urlpatterns = [
    path('', articles_view, name="blog_url"),
    path('create/', create_article_view, name="new_aricle_path"),
    path('article/dariush-<int:num>', detail_article_view, name="article_path")
]
