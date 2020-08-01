from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Article

# Create your views here.


class BlogIndex(ListView):
    model = Article
