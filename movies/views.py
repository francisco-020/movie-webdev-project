from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def movie_single(request):
    return render(request, 'moviesingle.html')