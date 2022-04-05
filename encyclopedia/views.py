import markdown2
import random

from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_article(request, article_title):
    if article_title in util.list_entries():
        article_content = _get_article_content(article_title)
        return render(request, "encyclopedia/article.html", {
            "article_title": article_title,
            "article_content": article_content
        })
    else:
        error_code = "404 Not found"
        return render(request, "encyclopedia/error.html", {
            "article_title": article_title,
            "error_code": error_code,
            "error_message": f"Requested page with article title '{article_title}' does not exist"
        })


def search(request):
    query_string = request.GET.get('q', None)
    if query_string.lower() in list(map(str.lower, util.list_entries())):
        article_content = _get_article_content(query_string)
        return render(request, "encyclopedia/article.html", {
            "article_title": query_string,
            "article_content": article_content
        })
    else:
        matching_articles = []
        for article_name in util.list_entries():
            if query_string.lower() in article_name.lower():
                matching_articles.append(article_name)
        if matching_articles:
            return render(request, "encyclopedia/matching_articles.html", {
                "entries": matching_articles,
            })
        else:
            error_code = "Nothing found"
            return render(request, "encyclopedia/error.html", {
                "error_code": error_code,
                "error_message": f"Nothing was found for query '{query_string}'"
            })


def new(request):
    return render(request, "encyclopedia/new_article.html")


def save_article(request):
    article_title = request.GET.get('title', None)
    if article_title.lower() in list(map(str.lower, util.list_entries())):
        error_code = "409 Conflict"
        return render(request, "encyclopedia/error.html", {
            "error_code": error_code,
            "error_message": f"Article with provided title '{article_title}' is already exists"
        })
    else:
        article_content = request.GET.get('content', None)
        util.save_entry(article_title, article_content)

        article_content = _get_article_content(article_title)
        return render(request, "encyclopedia/article.html", {
            "article_title": article_title,
            "article_content": article_content
        })


def edit_page(request):
    article_title = request.GET.get('article_title')
    article_content = _get_raw_article_content(article_title)
    return render(request, "encyclopedia/edit_page.html", {
        "article_title": article_title,
        "article_content": article_content
    })


def save_edited_article(request):
    article_title = request.GET.get('title', None)
    article_content = request.GET.get('content', None)
    util.save_entry(article_title, article_content)
    article_content = _get_article_content(article_title)
    return render(request, "encyclopedia/article.html", {
        "article_title": article_title,
        "article_content": article_content
    })


def random_article(request):
    article_title = random.choice(util.list_entries())
    article_content = _get_article_content(article_title)
    return render(request, "encyclopedia/article.html", {
        "article_title": article_title,
        "article_content": article_content
    })


def _get_article_content(article_title):
    article_content_md = util.get_entry(article_title)
    return markdown2.markdown(article_content_md)


def _get_raw_article_content(article_title):
    return util.get_entry(article_title)
