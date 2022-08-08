from django.contrib import admin
from .models import Profile, ContactUs


# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ["user_full_name", "user_email", "telegram"]


# admin.site.register(MyUser, MyUserAdmin)


class MyUserAdmin(admin.ModelAdmin):
    list_display = ["user"]


admin.site.register(Profile, MyUserAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]


admin.site.register(ContactUs, ContactUsAdmin)
