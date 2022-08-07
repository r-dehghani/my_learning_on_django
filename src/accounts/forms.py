from django.forms import ModelForm
from django.core.validators import EmailValidator
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core import validators
from django.contrib.auth.password_validation import validate_password


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "email"]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["title", "location", "about_me", "profile_pic", "telegram",
                  "github", "linkedin", "tweeter", "instagram", "personal_website"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        print("cleaned_data is ====> \n", data)
        # title = data.get('title')
        user_full_name = data.get("user_full_name")

        qs1 = Profile.objects.filter(user_full_name__icontains=user_full_name)
        if qs1.exists():
            self.add_error("user_full_name",
                           'the user name is taken!!! pick another one !!!')
        # qs = MyUser.objects.filter(title__icontains=title)
        # if qs.exists():
        # print("####### ######## The user Exists!!!######### #######")

        # self.add_error(
        #     "title", f"error!!! the {title} is already exists!!!")

        return data

# FIXME: if you don't want all fields to be displayed you can use any field like below. make sure these fields are not reqiured
    # class MyUserForm(forms.Form):
    #     # user_full_name = models.CharField(verbose_name="full name", max_length=100)
    #     # username = forms.CharField(
    #     #     max_length=50, widget=forms.TextInput, label="username", unique=True)
    #     # TODO: widget is clearify the type in HTML input tag <type> TODO:
    #     user_full_name = forms.CharField(
    #         max_length=100, widget=forms.TextInput, label="Full Name")
    #     # title = models.CharField(max_length=256)
    #     title = forms.CharField(
    #         max_length=100, widget=forms.TextInput, label="Your Title")
    #     # user_email = models.EmailField(verbose_name="email address",
    #     #                                editable=True, max_length=254, unique=True)
    #     user_email = forms.EmailField(
    #         widget=forms.EmailInput, validators=EmailValidator, unique=True, label="Email Address")
    #     # location = models.CharField(verbose_name="address", max_length=100)
    #     location = forms.CharField(
    #         max_length=100, widget=forms.TextInput, label="Your Location")
    #     # about_me = models.TextField(
    #     #     verbose_name="a little about about your profile!", max_length=1000)
    #     about_me = forms.CharField(
    #         widget=forms.Textarea, max_length=500, label="About Me")

    #     # profile_pic = models.ImageField(
    #     #     upload_to='./images/profile_pictures',
    #     #     blank=True)
    #     profile_pic = forms.ImageField(required=False)
    #     # ------- Social media accounts! -------
    #     # telegram = models.URLField(
    #     # verbose_name="telegram", unique=True, editable=True, max_length=100)
    #     telegram = forms.URLField(initial='http://www.t.me/',
    #                               max_length=100, widget=forms.URLInput, unique=True, label="Telegram account", required=False)
    #     # github = models.URLField(
    #     # verbose_name="github", unique=True, editable=True, max_length=100)
    #     github = forms.URLField(initial="https://github.com/",
    #                             max_length=100, widget=forms.URLInput, unique=True, label="github account", required=False)
    #     # linkedin = models.URLField(
    #     # verbose_name="linkedin", unique=True, editable=True, max_length=100)
    #     linkedin = forms.URLField(initial="https://www.linkedin.com/",
    #                               max_length=100, widget=forms.URLInput, unique=True, label="linkedin account", required=False)
    #     # tweeter = models.URLField(
    #     # verbose_name="tweeter", unique=True, editable=True, max_length=100)
    #     tweeter = forms.URLField(initial="https://www.twitter.com/",
    #                              max_length=100, widget=forms.URLInput, unique=True, label="tweeter account", required=False)
    #     # instagram = models.URLField(
    #     # verbose_name="instagram", unique=True, editable=True, max_length=100)
    #     instagram = forms.URLField(initial="https://www.instagram.com/",
    #                                max_length=100, widget=forms.URLInput, unique=True, label="instagram account", required=False)
    #     # personal_website = models.URLField(
    #     # verbose_name="personal website", unique=True, editable=True, max_length=100)
    #     personal_website = forms.URLField(initial='http://',
    #                                       max_length=100, widget=forms.URLInput, unique=True, label="personal_website", required=False)
# FIXME:


class LoginForm(AuthenticationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
        data = self.cleaned_data
        # email = data.get("email")

        qs = User.objects.filter(email__icontains=email)
        if not qs.exists():
            self.add_error(
                "email", "this Email is not valid! Do you register ???")


class Register_form(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "username",
                  "email", "password1", "password2"]

    def clean(self):
        data = self.cleaned_data
        print("cleaned_data is ====> \n", data)
        username = data.get('username')
        email = data.get("email")

        qs = User.objects.filter(username__icontains=username)
        qs1 = User.objects.filter(email__icontains=email)
        if qs.exists():
            self.add_error("username",
                           'the user name is taken!!! pick another one !!!')
        if qs1.exists():
            self.add_error(
                "email", "this email adrress is taken!!! pick another one!!!")
