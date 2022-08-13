from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm
from django.urls import reverse


def detail_article_view(request, slug):
    dict_article = Article.objects.get(slug=slug)
    context = {
        "article_title": dict_article.title,
        "article_content": dict_article.content,
        "article_image": dict_article.image,
        "article_time_to_read": dict_article.time_to_read,
    }
    return render(request, 'blog/detail_article.html', context=context)


def articles_view(request):
    dict_articles = Article.objects.all()
    context = {"articles": dict_articles}
    return render(request, "blog/articles.html", context=context)


@login_required
def create_article_view(request):
    form = CreateArticleForm()
    context = {}
    if request.method == "POST":
        form = CreateArticleForm(request.POST, request.FILES)
        # dict_request = request.POST
        # form.title = dict_request.get("title")
        # form.content = dict_request.get("content")
        # form.time_to_read = dict_request.get("time_to_read")
        # form.image = request.FILES['image']
        if form.is_valid():
            form.save()
            # return redirect('/blog/')
            return redirect(reverse("blog_url"))
    # if request.method == "POST":
    #     dict_request = request.POST
    #     form = Article.objects.create(
    #         title=dict_request.get("title"), content=dict_request.get("content"),
    #         image=dict_request.get("image"), time_to_read=dict_request.get("time_to_read"))
        context = {
            "form": form,
            "created": True,
        }
    context = {
        "form": form
    }
    return render(request, 'blog/create_article.html', context=context)
