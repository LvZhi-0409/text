from django.urls import path
from . import views

app_name = 'lover'

urlpatterns = [
    path('lover_index',views.lover_index,name = 'lover_index'),
    path('lover_movie', views.lover_movie,name = 'lover_movie'),
    path('lover_cake', views.lover_cake,name = 'lover_cake'),
]