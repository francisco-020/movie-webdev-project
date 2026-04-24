from django.shortcuts import render
from .models import SocialLink, Slider, MovieTheater


def home(request):
    social_links = SocialLink.objects.all()
    sliders = Slider.objects.all()
    theater_popular = MovieTheater.objects.filter(type='popular')
    theater_coming_soon = MovieTheater.objects.filter(type='coming_soon')

    context = {
        'social_links': social_links,
        'sliders': sliders,
        'theater_popular': theater_popular,
        'theater_coming_soon': theater_coming_soon,
    }

    return render(request, 'index.html', context)


def movie_single(request):
    return render(request, 'moviesingle.html')