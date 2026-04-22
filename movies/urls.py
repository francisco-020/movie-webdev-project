from django.urls import path
from .views import home, movie_single

urlpatterns = [
    path('', home, name='home'),
    path('moviesingle/', movie_single, name='movie_single'),
]