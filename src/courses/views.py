from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def course_view(request, id, *args, **kwargs):

    return render(request, "course_view.html", context={"id": id})
