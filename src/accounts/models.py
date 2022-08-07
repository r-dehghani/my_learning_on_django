from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_full_name = models.CharField(verbose_name="full name", max_length=100)
    title = models.CharField(max_length=256)
    # user_email = models.EmailField(verbose_name="email address",
    #                                editable=True, max_length=254, unique=True, blank=True, null=True)
    location = models.CharField(
        verbose_name="address", max_length=100, blank=True, null=True)
    about_me = models.TextField(
        verbose_name="a little about about your profile!", max_length=1000, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='static/assets/images/profile_pictures',
        blank=True)
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

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
        