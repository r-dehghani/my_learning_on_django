from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from courses.models import Course
# from .forms import MyUserForm
from django.utils.text import slugify


@require_http_methods(["GET", "POST"])
def course_view(request, slug):

    qs = Course.objects.get(slug=slug)
    print("qs is ", qs)
    context = {
        "course": qs,

    }
    # if qs.get("id") == 0:
    #     return HttpResponse(status=403)
    # else:
    return render(request, "courses/course_view.html", context=context)


def courses_view(request):
    dict_courses = Course.objects.all()

    context = {
        "course_obj": dict_courses,
    }
    return render(request, 'courses/courses_view.html', context=context)


def search_courses_view(request):
    query_dict = request.GET
    print(query_dict)
    query = query_dict.get("query_search")
    course_object = None
    if query is not None:
        course_object = Course.objects.get(id=query)
    context = {
        "course_object": course_object
    }
    return render(request, "courses/search.html", context=context)
