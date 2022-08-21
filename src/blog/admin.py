from django.contrib import admin
from .models import Article
from django.contrib.auth import get_user_model
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    # inlines = [UserInline]
    list_display = ["pk", "auther", "title", "slug", "content", "image"]
    search_fields = ["title", "content", "author"]
    raw_id_fields = ["auther"]  # TODO: this is important!!!


admin.site.register(Article, AdminArticle)
