from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


def detail_article_view(request, num):
    dict_article = Article.objects.get(id=num)
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
    context = {}
    if request.method == "POST":
        article_object = Article()
        dict_request = request.POST
        article_object.title = dict_request.get("title")
        article_object.content = dict_request.get("content")
        article_object.time_to_read = dict_request.get("time_to_read")
        article_object.image = request.FILES['image']
        article_object.save()

    # if request.method == "POST":
    #     dict_request = request.POST
    #     article_object = Article.objects.create(
    #         title=dict_request.get("title"), content=dict_request.get("content"),
    #         image=dict_request.get("image"), time_to_read=dict_request.get("time_to_read"))
        context = {
            "object": article_object,
            "created": True,
        }
    return render(request, 'blog/create_article.html', context=context)
