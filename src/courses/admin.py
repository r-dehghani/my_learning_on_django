from django.contrib import admin
from .models import Course, MyUser
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "course_name", "course_description", "Course_data"]
    search_fields = ["course_name", "course_description"]


class MyUserAdmin(admin.ModelAdmin):
    list_display = ["user_full_name", "user_email", "telegram"]


admin.site.register(Course, CourseAdmin)
admin.site.register(MyUser, MyUserAdmin)
