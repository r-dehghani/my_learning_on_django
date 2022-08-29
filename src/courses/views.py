from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from courses.models import Course
from accounts.models import Profile
# from .forms import MyUserForm
from django.utils.text import slugify
from django.db.models import Q


@require_http_methods(["GET", "POST"])
def course_view(request, slug):
    qs = Course.objects.get(slug=slug)
    if request.user.is_authenticated:
        qs_1 = Profile.objects.get(user=request.user)
        # qs_ = Profile.objects.all()
    else:
        qs_1 = "Guest"
    print("qs is ", qs)
    print("qs_1", qs_1)
    print("qs_1.list_of_registered_courses", qs_1.list_of_registered_courses)
    context = {
        "course": qs,
        "qs_1": qs_1,

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

        lookup = Q(course_name__icontains=query) | Q(
            course_description__icontains=query)
        course_object = Course.objects.filter(lookup)
    else:
        return redirect("/")
    context = {
        "course_object": course_object
    }
    return render(request, "courses/search.html", context=context)
