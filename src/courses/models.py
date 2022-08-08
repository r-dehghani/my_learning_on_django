from django.db import models
from accounts.models import Profile
# Create your models here.


class Course(models.Model):  # Hint: evry single model in Django inherite from models.Model!!
    students = models.ManyToManyField(Profile)
    course_name = models.CharField(max_length=256, unique=True, blank=False)
    course_description = models.TextField(
        verbose_name="Description about course!")
    course_image = models.ImageField(
        verbose_name="image of course", upload_to='static/assets/images/course_picture')  # may be i should add media to the uploaded_to!!!
    course_link_to_zoom = models.URLField(
        verbose_name="zoom link", editable=True, max_length=256)
    Course_data = models.DateTimeField()

    def __str__(self):
        return self.course_name
