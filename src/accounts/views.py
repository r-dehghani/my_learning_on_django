from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm, Register_form, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages


# ============================================================================


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
# ============================================================================

# TODO: using authenticate module to verify logging in users


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, 'accounts/login.html', context=context)
    form = AuthenticationForm(request)
# ============================================================================


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        context = {
            "message": "We miss you :("
        }
        return render(request, 'accounts/logout.html', context=context)
    else:
        form = AuthenticationForm(request)
        return render(request, 'accounts/login.html', context={"form": form})
# ============================================================================


def profile_view(request):
    if request.method == "POST":
        print(request.user)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "your profile is updated successfully!!")
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, 'accounts/profile_view.html', context=context)


# ============================================================================
# def profile_view(request):
#     active_user = request.user

#     form = ProfileForm()

#     if request.method == "POST":
#         print("request.post is \n", request.POST)
#         print("request.FILES is \n", request.FILES)
#         print(request.user)
#         # TODO: !!!important hint!!!
#         # when you work with photo or file you need to call request.FILES
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # context["form"] = MyUserForm()
#         else:
#             print(form.errors)
#     context = {
#         "form": form,
#     }
#     return render(request, 'accounts/profile_view.html', context=context)
# ============================================================================

# def login_view(request):
#     form = LoginForm()
#     if request.user.is_authenticated:
#         return render(request, "accounts/already_loged_in.html", {})

#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         # _ = User.objects.filter(email=email).exists()
#         if User.objects.filter(email=email).exists():
#             user = authenticate(request, username=User.objects.get(
#                 email=email).username, password=password)
#             print("user object is ", User.objects.filter(email=email))
#             print("user authenticate is ", user)
#             if user is None:
#                 context = {
#                     "form": LoginForm(),
#                     # "error": "invalid password!!!",
#                 }

#                 return render(request, "accounts/login.html", context=context)
#             login(request, user)
#             return redirect("/")
#     context = {
#         "form": form
#     }
#     return render(request, 'accounts/login.html', context=context)


# def login_view(request):
#     form = LoginForm()
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

#         form = LoginForm(request.POST or None)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print("REQQQQQ POST is : ", request.POST)
#         print("email is ", email)
#         print("password is ", password)

#         if User.objects.filter(email=email).exists():
#             username = User.objects.filter(email=email)
#             print("1")
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 print("2")
#                 login(request, )
#             if user is None:
#                 context = {
#                     "error": "invalid email or password!!!", }
#                 return render(request, "accounts/login.html", context=context)
#                 login(request, user)
#                 return redirect('/')

#             # user = authenticate(request, username=User.objects.get(
#             #     email=email).username, password=password)

#             # if user is None:
#             #     context = {
#             #         "error": "invalid email or password!!!", }
#             #     return render(request, "accounts/login.html", context=context)
#             # login(request, user)
#             # return redirect("/")
#         # else:
#         #     print(form.errors)
#     context = {"form": form}
#     return render(request, 'accounts/login.html', context=context)
