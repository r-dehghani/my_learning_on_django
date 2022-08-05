from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm, Register_form, LoginForm
from django.contrib.auth.models import User

# TODO: using authenticate module to verify logging in users


def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return render(request, "accounts/already_loged_in.html", {})
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            _ = User.objects.filter(email=email).exists()
            if _:
                user = authenticate(request, username=User.objects.get(
                    email=email).username, password=password)

                if user is None:
                    context = {
                        "error": "invalid email or password!!!",
                    }
                    return render(request, "accounts/login.html", context=context)
                login(request, user)
                return redirect("/")
        context = {
            "form": form
        }
        return render(request, 'accounts/login.html', context=context)


# def login_view(request):
#     form1 = LoginForm()
#     if request.user.is_authenticated:
#         return render(request, "accounts/already_loged_in.html", {})
#     # elif:
#     #     if request.method == "POST":
#     #         form = AuthenticationForm(request, data=request.POST)
#     #         if form.is_valid():
#     #             user = form.get_user()
#     #             login(request, user)
#     #             return redirect('/')
#     if request.method == "POST":
#         # form = AuthenticationForm(request)

#         form1 = LoginForm(request.POST or None)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         username = User.objects.get(email=email).username

#         print("email is ", email)
#         print("username  is ", username)
#         print("password is ", password)
#         form = AuthenticationForm(
#             request, data={"username": username, "password": password})
#         if form.is_valid():

#             user = form.get_user()
#             login(request, user)
#             return redirect('/')

#             # user = authenticate(request, username=User.objects.get(
#             #     email=email).username, password=password)

#             # if user is None:
#             #     context = {
#             #         "error": "invalid email or password!!!", }
#             #     return render(request, "accounts/login.html", context=context)
#             # login(request, user)
#             # return redirect("/")
#     context = {"form": form1}
#     return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        context = {

        }
        return render(request, 'accounts/logout.html', context=context)
    else:
        return render(request, 'accounts/login.html', context={})


def register_view(request):
    # form = UserCreationForm(request.POST or None)
    form = Register_form(request.POST or None)
    print("form user is : ", request.POST)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/accounts/login/")
    else:
        print(form.errors)
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context=context)


def profile_view(request):
    form = ProfileForm()

    if request.method == "POST":
        print("request.post is \n", request.POST)
        print("request.FILES is \n", request.FILES)
        # TODO: !!!important hint!!!
        # when you work with photo or file you need to call request.FILES
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # context["form"] = MyUserForm()
        else:
            print(form.errors)
    context = {
        "form": form,
    }
    return render(request, 'accounts/profile_view.html', context=context)
