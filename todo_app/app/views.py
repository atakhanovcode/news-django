from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    front_new = News.objects.all()[:3]

    context = {
        "front_new": front_new,
    }
    return render(request, "news/home.html", context)


def news(request):
    news = News.objects.all()

    context = {
        "news": news,
    }
    return render(request, "news/news.html", context)


def news_detail(request, id):
    news_detail = News.objects.get(id=id)
    context = {
        "news_detail": news_detail,
    }
    return render(request, "news/news_detail.html", context)
