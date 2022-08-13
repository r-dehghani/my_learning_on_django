from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from .models import Course
# بعد ساختن سیگنال هامون باید اون ها رو دارد فایل apps.py بکنیم
from .utils import slugify_instance_course_name

#  ====================================================================


def course_pre_save(sender, instance, *args, **kwargs):
    # print('pre_save')
    if instance.slug is None:
        slugify_instance_course_name(instance, save=False)


pre_save.connect(course_pre_save, sender=Course)


def course_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        slugify_instance_course_name(instance, save=True)


post_save.connect(course_post_save, sender=Course)
