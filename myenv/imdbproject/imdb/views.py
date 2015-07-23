# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from imdb.models import Movieinfo
import django_filters

# Create your views here.
def home(request):
	context = locals()
	return render(request, 'home.html', context)

def movieinfo(request):
	movies = Movieinfo.objects.all()
	return render(request, 'movieinfo.html', {'movies': movies})

@login_required
def profile(request):
	user = request.user
	context = {'user':user}
	return render(request, 'profile.html', context)



class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movieinfo
        fields = ['name', 'director']
        order_by = ['popularity', 'imdb_score']

def moviefilter(request):
	m = MovieFilter(request.GET, queryset=Movieinfo.objects.all())
	return render_to_response('moviefilter.html', {'filters': m})