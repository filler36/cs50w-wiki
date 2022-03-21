import markdown2
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, article_title):
    if article_title in util.list_entries():
        article_content = _get_article_content(article_title)
        return render(request, "encyclopedia/article.html", {
            "article_title": article_title,
            "article_content": article_content
        })
    else:
        return render(request, "encyclopedia/not_found.html", {
            "article_title": article_title
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
            return render(request, "encyclopedia/not_found.html", {
                "article_title": query_string
            })




def _get_article_content(article_title):
    article_content_md = util.get_entry(article_title)
    return markdown2.markdown(article_content_md)

