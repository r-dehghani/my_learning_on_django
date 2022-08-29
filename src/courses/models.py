from django.db import models
# from accounts.models import Profile
# Create your models here.
from PIL import Image
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Course(models.Model):  # Hint: evry single model in Django inherite from models.Model!!
    # students = models.ManyToManyField(Profile, null=True, blank=True)
    course_name = models.CharField(max_length=256, unique=True, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    course_description = models.TextField(
        verbose_name="Description about course!")
    course_image = models.ImageField(
        verbose_name="image of course", upload_to='static/assets/images/course_picture')  # may be i should add media to the uploaded_to!!!
    course_link_to_zoom = models.URLField(
        verbose_name="zoom link", editable=True, max_length=256)
    Course_data = models.DateTimeField()
    price = models.FloatField()
    digital = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.course_image.path)

        if img.height > 348 or img.width > 225:
            output_size = (348, 225)
            img.thumbnail(output_size)
            img.save(self.course_image.path)

        elif img.height < 348 or img.width < 225:
            output_size = (348, 225)
            img.thumbnail(output_size)
            img.save(self.course_image.path)


# class Order(models.Model):
#     user = models.ForeignKey(get_user_model, on_delete=models.SET_NULL)
#     product = models.ManyToManyField(Course, on_delete=models.SET_NULL)
