from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.movies_list,name="list"),
    path('search/',views.search_results.as_view(),name="search_results"),
    path('<slug:slug>/',views.movie_detail,name="detail"),
]