"""to render the html web pages
"""
from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course
from django.template.loader import render_to_string, get_template
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_http_methods(["GET", "POST"])
def home_view(request):
    dict_courses = Course.objects.all()

    context = {
        "course_obj": dict_courses,
    }
    return render(request, 'home-view.html', context=context)
