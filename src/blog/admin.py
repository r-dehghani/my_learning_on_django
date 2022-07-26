from django.contrib import admin
from .models import Article
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    list_display = ["title", "content", "image"]
    search_fields = ["title", "content"]


admin.site.register(Article, AdminArticle)
