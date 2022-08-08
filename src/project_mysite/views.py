"""to render the html web pages
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from courses.models import Course
from django.template.loader import render_to_string, get_template
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from accounts.forms import ContactUsForm


@require_http_methods(["GET", "POST"])
def home_view(request):
    dict_courses = Course.objects.all()

    context = {
        "course_obj": dict_courses,
    }
    return render(request, 'home-view.html', context=context)


def contact_us_view(request):
    form = ContactUsForm()
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, 'contact-us.html', context=context)
