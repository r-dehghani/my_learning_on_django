from django.shortcuts import render
from .models import Article


def detail_article_view(request):
    dict_article = Article.objects.get(id=num)


def articles_view(request):
    dict_articles = Article.objects.all()
    print(dict_articles)
    context = {"articles": dict_articles}
    return render(request, "blog/articles.html", context=context)


def create_article_view(request):
    context = {}
    if request.method == "POST":
        dict_request = request.POST

        article_object = Article.objects.create(
            title=dict_request.get("title"), content=dict_request.get("content"), image=dict_request.get("image"))
        context = {
            "object": article_object,
            "created": True,
        }
    return render(request, 'blog/create_article.html', context=context)
