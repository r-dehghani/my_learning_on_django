from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "user_email", "telegram"]


admin.site.register(MyUser, MyUserAdmin)
