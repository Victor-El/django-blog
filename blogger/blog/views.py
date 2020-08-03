from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class AddArticle(LoginRequiredMixin, FormView):
    login_url = '/signin'
    form_class = AddArticleForm
    success_url = "/"
    template_name = 'blog/article_add.html'

    def form_valid(self, form):
        form.persist(self.request.user)
        return super().form_valid(form)


class CreateArticle(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/signin'
    model = Article
    fields = ['author', 'title', 'content']

    def test_func(self):
        return self.request.user.is_superuser


class UpdateArticle(LoginRequiredMixin, UpdateView):
    login_url = '/signin'
    model = Article
    fields = ['author', 'title', 'content']
    template_name_suffix = "_update"


class DeleteArticle(LoginRequiredMixin, DeleteView):
    login_url = '/signin'
    model = Article
    success_url = reverse_lazy("blog:index")