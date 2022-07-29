"""to render the html web pages
"""
from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course
from django.template.loader import render_to_string, get_template
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_http_methods(["GET", "POST"])
def home_view(request):
    """Take in a request(Django sends the request)
    return HTML as a response (We pick to return a response!)

    Args:
        request (http request): quest that is sent from the user

    Returns:
        HTML web page: the desired html is returned!

    """
    context = {
        "name": "dariush",
        "family": "Dehghani",
        "my_list": range(10),
    }
    return render(request, 'home-view.html', context=context)
