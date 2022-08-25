from django.shortcuts import render, redirect, reverse
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse
# ===========================================================================


def detail_article_view(request, slug):
    dict_article = Article.objects.get(slug=slug)
    hx_url = reverse("article_hx_path", kwargs={"slug": slug})
    print(hx_url)
    context = {
        # "object": dict_article,
        # "article_title": dict_article.title,
        # "article_content": dict_article.content,
        # "article_image": dict_article.image,
        # "article_time_to_read": dict_article.time_to_read,
        "hx_url": hx_url,
    }
    return render(request, 'blog/detail_article.html', context=context)


def detail_article_hx_view(request, slug):
    try:
        dict_article = Article.objects.get(slug=slug)
    except:
        dict_article = None

    if dict_article is None:
        return HttpResponse("there is not any thing!")
    context = {
        "article_title": dict_article.title,
        "article_content": dict_article.content,
        "article_image": dict_article.image,
        "article_time_to_read": dict_article.time_to_read,
    }
    return render(request, 'partial/detail_article.html', context=context)

# ===========================================================================


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


def search_article_view(request):

    query = request.GET.get("query_search")
    # qs = Article.objects.filter(title_icontains=query)
    # article_object = None
    # if query_dict is not None:
    # lookup = Q(title__icontains=query) | Q(content__icontains=query)
    # qs = Article.objects.filter(lookup)
    # here we rewrite the objects of model!!! two upper line also is work!
    qs = Article.objects.search(query=query)
    if qs is not None:

        context = {
            "finding": True,
            "article_object": qs,
        }
        return render(request, "blog/search.html", context=context)
    else:
        context = {
            "finding": False,
        }
        return render(request, "blog/search.html", context=context)

    # return render(request, 'blog/search', context=context)


def search_result_view(request):
    dict_articles = Article.objects.all()
    context = {"articles": dict_articles}
