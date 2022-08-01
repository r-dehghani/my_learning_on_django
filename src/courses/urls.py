
from django.urls import path, include
from .views import course_view, search_courses_view, courses_view, my_user_view
urlpatterns = [
    path('', courses_view, name="courses_view"),
    path('search/', search_courses_view, name="search_courses"),
    path('<int:course_id>', course_view, name="course_view"),
    path('user_courses', my_user_view, name="my_user_view"),

]
