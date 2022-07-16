"""to render the html web pages
"""
from django.http import HttpResponse


def home_view(request):
    """Take in a request(Django sends the request)
    return HTML as a response (We pick to return a response!)

    Args:
        request (http request): quest that is sent from the user

    Returns:
        HTML web page: the desired html is returned!
    """
    name = "dariush"
    html_text = f"""
    hello {name}
    """
    return HttpResponse(html_text)
