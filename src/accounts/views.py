from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "invalid username or password!!!",
            }
            return render(request, "accounts/login.html", context=context)
        login(request, user)
        return redirect("/")
        # context = {
        #     "username": username,
        #     "password": password,
        # }
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    logout(request)
    context = {

    }
    return render(request, 'accounts/logout.html', context=context)


def register_view(request):
    context = {

    }
    return render(request, 'accounts/register.html', context=context)
