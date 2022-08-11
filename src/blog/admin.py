from django.contrib import admin
from .models import Article
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    list_display = ["pk", "title", "slug", "content", "image"]
    search_fields = ["title", "content"]


admin.site.register(Article, AdminArticle)
