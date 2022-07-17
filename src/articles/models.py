from django.db import models

# Create your models here.


class Writer(models.Model):
    writer = models.CharField(max_length=100)


class Articles(models.Model):  # Hint: evry single model in Django inherite from models.Model1!!
    writer_name = models.ForeignKey(Writer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    writinr_date = models.DateTimeField()
