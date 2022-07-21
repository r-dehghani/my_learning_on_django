"""to render the html web pages
"""
from django.http import HttpResponse
from courses.models import Course
from django.template.loader import render_to_string, get_template


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

    html_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(html_STRING)
