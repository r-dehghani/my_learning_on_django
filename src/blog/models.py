from django.db import models
from PIL import Image
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    content = models.TextField()
    time_to_read = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="static/assets/images/article_pictures/")

    def __str__(self):
        return self.title

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
