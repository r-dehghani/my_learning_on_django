
from django.urls import path, include
from .views import course_view, search_courses_view
urlpatterns = [

    path('', search_courses_view, name="search_courses"),

]
