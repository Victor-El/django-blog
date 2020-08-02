from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Article

# Create your views here.


class BlogIndex(ListView):
    model = Article
    paginate_by = 2


class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coder'] = "CodeEnzyme" # Just testing out this feature
        return context


class CreateArticle(CreateView):
    model = Article
    fields = ['author', 'title', 'content']


class UpdateArticle(UpdateView):
    model = Article
    fields = ['author', 'title', 'content']
    template_name_suffix = "_update"