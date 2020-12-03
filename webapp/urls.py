from django.urls import path, include
from . import views

urlpatterns = [
    path('api/movies', views.movie_list),
    path('api/scrape', views.scrape),
    path('api/name', views.movie_name),
    #url(r'^api/movie/(?P<pk>[0-9]+)$', views.movie_detail),
]
