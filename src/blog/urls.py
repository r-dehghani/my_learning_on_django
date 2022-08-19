from django.urls import path, include
from .views import create_article_view, articles_view, detail_article_view, search_article_view
urlpatterns = [
    path('', articles_view, name="blog_url"),
    path('create/', create_article_view, name="new_aricle_path"),
    path('article/<slug:slug>', detail_article_view, name="article_path"),
    path('search/', search_article_view, name="search_article_url"),
]
