from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def app_list(request):
    articles = Article.objects.all()
    return render(request, "article/index.html", {'article': articles})


def details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, "article/article_detail.html", {'article': article})
