from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    time_to_read = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="static/assets/images/article_pictures/")

    def __str__(self):
        return self.title
