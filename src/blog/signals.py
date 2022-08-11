from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from .models import Article
# بعد ساختن سیگنال هامون باید اون ها رو دارد فایل apps.py بکنیم

#  ====================================================================


def article_slug_pre_save(sender, instance, *args, **kwargs):
    print("pre save!")
    if instance.slug is None:
        print("<<<<<<<<<<<<<<<<<<<<<<<None")
        instance.slug = slugify(instance.title)


pre_save.connect(article_slug_pre_save, sender=Article)

#  ====================================================================

#  ====================================================================


def article_slug_post_save(sender, instance, created, *args, **kwargs):
    print("post save!")
    if created:
        print("<<<<<<<<<<<<<<<<<<<<<<<created")
        instance.slug = slugify(instance.title)
        instance.save()


post_save.connect(article_slug_post_save, sender=Article)

#  ====================================================================
