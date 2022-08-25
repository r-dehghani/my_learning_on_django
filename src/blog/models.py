from django.db import models
from PIL import Image
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.auth.models import User


class ArticleManager(models.Manager):
    def search(self, query=None):
        if query is None or query == "":
            return self.get_queryset().none()
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.get_queryset().filter(lookup)
        return qs


class Article(models.Model):
    auther = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    content = models.TextField()
    time_to_read = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="static/assets/images/article_pictures/")

    objects = ArticleManager()

    def __str__(self):
        return self.title

    def get_absulote_url(self):
        return f'/blog/article/{self.slug}'

    def get_absulote_hx_url(self):
        return f'/blog/article/hx/{self.slug}'

    def save(self, *args, **kwargs):  # برای سیو کردن عکس با تغییر سایز

        # Article.objects.getattr(id=1)
        # set something!
        super().save(*args, **kwargs)
        # obj.save()
        # do something else
        img = Image.open(self.image.path)

        if img.height > 348 or img.width > 225:
            output_size = (348, 225)
            img.thumbnail(output_size)
            img.save(self.image.path)

        elif img.height < 348 or img.width < 225:
            output_size = (348, 225)
            img.thumbnail(output_size)
            img.save(self.image.path)
