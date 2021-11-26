from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Movie
from django.db.models import Q
from django.views.generic import TemplateView, ListView


# Create your views here.

def movies_list(request):
    movies = Movie.objects.all().order_by('year')
    return render(request,'movies_list.html',{'movies': movies})

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request,'movie_detail.html',{'movie':movie})


class search_results(ListView):
    model = Movie
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('que')
        object_list = Movie.objects.filter(
            Q(title__icontains=query) | Q(slug__icontains=query)
        )
        return object_list
