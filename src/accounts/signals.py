from django.contrib.auth.models import User  # this is sender
# this will fire when a User model is created!!
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

# بعد ساختن سیگنال هامون باید اون ها رو دارد فایل apps.py بکنیم


@receiver(post_save, sender=User)
# ما میخواهیم هر بار که یوزر ایجاد شد این تابع فراخوانی بشه
def create_user_profile(sender, instance, created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, *args, **kwargs):
    instance.profile.save()
