from django.urls import path
from .views import home, movie_single, newsletter_subscribe

urlpatterns = [
    path('', home, name='home'),
    path('moviesingle/', movie_single, name='movie_single'),
    path('newsletter/', newsletter_subscribe, name='newsletter_subscribe'),
]