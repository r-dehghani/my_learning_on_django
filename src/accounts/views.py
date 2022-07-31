from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/already_loged_in.html", {})
    else:
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
    if request.user.is_authenticated:
        logout(request)
        context = {

        }
        return render(request, 'accounts/logout.html', context=context)
    else:
        return render(request, 'accounts/login.html', context={})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    print("form user is : ", request.POST)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/accounts/login/")
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context=context)
