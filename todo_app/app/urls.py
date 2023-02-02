from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("news/", news, name="news"),
    path("news/<int:id>", news_detail, name="news_detail"),
]
