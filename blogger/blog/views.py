from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Article
from .forms import AddArticleForm

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


class AddArticle(FormView):
    form_class = AddArticleForm
    success_url = "/"
    template_name = "article_add"


class CreateArticle(CreateView):
    model = Article
    fields = ['author', 'title', 'content']


class UpdateArticle(UpdateView):
    model = Article
    fields = ['author', 'title', 'content']
    template_name_suffix = "_update"


class DeleteArticle(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:index")