"""project_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_view
from courses.views import course_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('courses/', include('courses.urls')),
]

# urlpatterns = [
#     path('<page_slug>-<page_id>/', include([
#         path('history/', views.history),
#         path('edit/', views.edit),
#         path('discuss/', views.discuss),
#         path('permissions/', views.permissions),
#     ])),
# ]
