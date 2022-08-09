from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_full_name = models.CharField(verbose_name="full name", max_length=100)
    title = models.CharField(max_length=256, blank=True, null=True)
    # user_email = models.EmailField(verbose_name="email address",
    #                                editable=True, max_length=254, unique=True, blank=True, null=True)
    location = models.CharField(
        verbose_name="address", max_length=100, blank=True, null=True)
    about_me = models.TextField(
        verbose_name="a little about about your profile!", max_length=1000, blank=True, null=True)
    profile_pic = models.ImageField(default='static/assets/images/profile_pictures/default.png',
                                    upload_to='static/assets/images/profile_pictures', blank=True, null=True)
    # ------- Social media accounts! -------
    telegram = models.URLField(
        verbose_name="telegram", unique=True, editable=True, max_length=100, blank=True, null=True)
    github = models.URLField(
        verbose_name="github", unique=True, editable=True, max_length=100, blank=True, null=True)
    linkedin = models.URLField(
        verbose_name="linkedin", unique=True, editable=True, max_length=100, blank=True, null=True)
    tweeter = models.URLField(
        verbose_name="tweeter", unique=True, editable=True, max_length=100, blank=True, null=True)
    instagram = models.URLField(
        verbose_name="instagram", unique=True, editable=True, max_length=100, blank=True, null=True)
    personal_website = models.URLField(
        verbose_name="personal website", unique=True, editable=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.user.first_name)

    #  برای تغییر سایز عکس ها موقع سیو شدن باید متد سیو را بازنویسی کنیم!
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class ContactUs(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)
