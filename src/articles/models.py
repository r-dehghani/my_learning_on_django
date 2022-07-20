from django.db import models

# Create your models here.


class User(models.Model):
    user_full_name = models.CharField(verbose_name="full name", max_length=100)
    title = models.CharField(max_length=256)
    user_email = models.EmailField(verbose_name="email address",
                                   editable=True, max_length=254, unique=True)
    location = models.CharField(verbose_name="address", max_length=100)
    about_me = models.TextField(
        verbose_name="a little about about your profile!", max_length=1000)
    profile_pic = models.ImageField(
        upload_to='./images/profile_pictures',
        blank=True)
    # ------- Social media accounts! -------
    telegram = models.URLField(
        verbose_name="telegram", unique=True, editable=True, max_length=100)
    github = models.URLField(
        verbose_name="github", unique=True, editable=True, max_length=100)
    linkedin = models.URLField(
        verbose_name="linkedin", unique=True, editable=True, max_length=100)
    tweeter = models.URLField(
        verbose_name="tweeter", unique=True, editable=True, max_length=100)
    instagram = models.URLField(
        verbose_name="instagram", unique=True, editable=True, max_length=100)
    personal_website = models.URLField(
        verbose_name="personal website", unique=True, editable=True, max_length=100)


class Course(models.Model):  # Hint: evry single model in Django inherite from models.Model1!!
    # اگر کورس دیلیت بشه یوزر دیلیت نمیسشه
    course_name = models.ManyToManyField(User)
    course_description = models.CharField(
        verbose_name="Description about course!", max_length=500)
    course_image = models.ImageField(
        verbose_name="image of course", upload_to='../images/course_pictures')
    course_link_to_zoom = models.URLField(
        verbose_name="zoom link", editable=True, max_length=256)
    Course_data = models.DateTimeField()
