from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:article_title>", views.wiki, name="article_title"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("save_article", views.save_article, name="save_article")
]
