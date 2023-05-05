from django.shortcuts import render
from django.views import generic
from .models import Musician


class PostList(generic.ListView):
    model = Musician
    queryset = Musician.objects.filter(status=1).order.by("-created_on")
    temnplate_name = 'index.html'
    paginate_by = 8
