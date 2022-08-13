from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):

    list_display = ["id", "course_name", "slug",
                    "course_description", "Course_data"]
    search_fields = ["course_name", "course_description"]
    # prepopulated_fields = {"slug": ("course_name",)}


admin.site.register(Course, CourseAdmin)
