
from django.urls import path, include
from .views import course_view
urlpatterns = [
    path('your_course/<int:id>/', course_view, name='your_course'),

]
