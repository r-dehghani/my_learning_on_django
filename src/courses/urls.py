
from django.urls import path, include
from .views import course_view, search_courses_view, courses_view, test_view
urlpatterns = [
    path('', courses_view, name="courses_view"),
    path('search/', search_courses_view, name="search_courses"),
    path('<slug:slug>', course_view, name="course_view"),
    path('test/', test_view, name="test_view"),

]
