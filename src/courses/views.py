from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def course_view(request, id, *args, **kwargs):
    context = {
        "id": id,

    }
    if id == 0:
        return HttpResponse(status=403)
    else:
        return render(request, "course_view.html", context=context)
