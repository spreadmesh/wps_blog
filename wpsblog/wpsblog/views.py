import json
import requests

from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        {"site_name": "wps_blog"},
    )


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
    )


def news(request):
    search = request.GET.get("search")  # title 에 search 가 포함되어 있는가

    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
    news_dict = json.loads(response.text)
    news_list = news_dict.get("news")

    if search:
        news_list = list(filter(
            lambda news: search in news.get('title'),
            news_list,
        ))

    return render(
        request,
        "news.html",
        {"news_list": news_list},
    )
