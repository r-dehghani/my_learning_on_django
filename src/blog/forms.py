from django import forms
from django.forms import ModelForm
from .models import Article


class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
    # title = forms.CharField(max_length=150)
    # content = forms.CharField(widget=forms.Textarea)
    # time_to_read = forms.CharField(max_length=50)
    # image = forms.ImageField()
    # title = models.CharField(max_length=150)
    # content = models.TextField()
    # time_to_read = models.CharField(max_length=50)
    # image = models.ImageField(
    #     upload_to="static/assets/images/article_pictures/")

    def __str__(self):
        return self.title
