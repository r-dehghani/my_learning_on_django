from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from courses.models import Course
from .forms import MyUserForm


@require_http_methods(["GET", "POST"])
def course_view(request, id, *args, **kwargs):
    context = {
        "id": id,

    }
    if id == 0:
        return HttpResponse(status=403)
    else:
        return render(request, "course_view.html", context=context)


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


def my_user_view(request):
    form = MyUserForm()

    if request.method == "POST":
        print("request.post is \n", request.POST)
        print("request.FILES is \n", request.FILES)
        # TODO: !!!important hint!!!
        # when you work with photo or file you need to call request.FILES
        form = MyUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # context["form"] = MyUserForm()
        else:
            print(form.errors)
    context = {
        "form": form,
    }
    return render(request, 'courses/my_user_view.html', context=context)
