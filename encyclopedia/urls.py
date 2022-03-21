from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:article_title>", views.wiki, name="article_title"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("save_article", views.save_article, name="save_article"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("save_edited_article", views.save_edited_article, name="save_edited_article"),
    path("random_article", views.random_article, name="random_article")
]
