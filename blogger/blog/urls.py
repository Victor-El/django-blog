from django.urls import path

from .views import BlogIndex, ArticleDetail, CreateArticle, UpdateArticle, DeleteArticle

app_name = "blog"

urlpatterns = [
    path("", BlogIndex.as_view(), name="index"),
    path("<int:pk>", ArticleDetail.as_view(), name="article_detail"),
    path("create", CreateArticle.as_view()),
    path("update/<int:pk>", UpdateArticle.as_view(), name="article_update"),
    path("delete/<int:pk>", DeleteArticle.as_view(), name="article_delete"),
]
