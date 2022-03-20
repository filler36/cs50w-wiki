from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, article_title):
    if article_title in util.list_entries():
        article_content = util.get_entry(article_title)
        print(article_content)
        return render(request, "encyclopedia/article.html", {
            "article_title": article_title,
            "article_content": article_content
        })
    else:
        return render(request, "encyclopedia/not_found.html", {
            "article_title": article_title
        })


def search(request, article_title):
    if article_title in list(map(str.lower, util.list_entries())):
        article_content = util.get_entry(article_title)
        return render(request, "encyclopedia/article.html", {
            "article_title": article_title,
            "article_content": article_content
        })

