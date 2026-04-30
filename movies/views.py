from django.shortcuts import render
from .models import (
    Slider,
    Advertisement,
    SocialLink,
    Celebrity,
    Trailer,
    TrailerItem,
    News,
    Tweet,
    MovieTheater,
    MovieTV,
)


def home(request):
    context = {
        "social_links": SocialLink.objects.all(),
        "sliders": Slider.objects.all(),
        "theater_popular": MovieTheater.objects.filter(type="popular"),
        "theater_coming_soon": MovieTheater.objects.filter(type="coming_soon"),
        "tv_popular": MovieTV.objects.filter(type="popular"),
        "tv_coming_soon": MovieTV.objects.filter(type="coming_soon"),
        "sidebar_ad": Advertisement.objects.filter(section="sidebar").first(),
        "latestnews_ad": Advertisement.objects.filter(section="latestnews").first(),
        "celebrities": Celebrity.objects.all(),
        "trailer": Trailer.objects.first(),
        "trailer_items": TrailerItem.objects.all(),
        "featured_news": News.objects.filter(section="featured").first(),
        "more_left_news": News.objects.filter(section="more_left"),
        "more_right_news": News.objects.filter(section="more_right"),
        "tweets": Tweet.objects.all(),
    }

    return render(request, 'index.html', context)


def movie_single(request):
    return render(request, 'moviesingle.html')