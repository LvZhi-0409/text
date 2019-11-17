from django.shortcuts import render
# Create your views here.

def lover_index(request):

    return render(request, 'lover/index.html')
def lover_movie(request):

    return render(request, 'lover/movie.html')
def lover_cake(request):

    return render(request, 'lover/cake.html')
