from django.urls import path

from .views import BlogIndex, ArticleDetail, CreateArticle, UpdateArticle

app_name = "blog"

urlpatterns = [
    path("", BlogIndex.as_view()),
    path("<int:pk>", ArticleDetail.as_view(), name="article_detail"),
    path("create", CreateArticle.as_view()),
    path("update/<int:pk>", UpdateArticle.as_view(), name="article_update"),
]
