from django.db import models

# Create your models here.


class User_(models.Model):
    reader = models.CharField(max_length=100)
    reader_email = models.EmailField(
        editable=True, max_length=254, unique=True)
    profile_pic = models.ImageField(
        upload_to='./images/profile_pictures',
        blank=True)


# class Writer(models.Model):
#     writer = models.CharField(max_length=100)


class Articles(models.Model):  # Hint: evry single model in Django inherite from models.Model1!!
    writer_name = models.ForeignKey(User_, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    writing_date = models.DateTimeField()


class FavoriteBook(models.Model):
    fav_book_name = models.TextField(max_length=500)
