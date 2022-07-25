from django.shortcuts import render


def create_article_view(request):
    context = {

    }
    return render(request, 'blog/create_article.html', context=context)
