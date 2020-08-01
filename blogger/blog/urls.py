from django.urls import path

from .views import BlogIndex, ArticleDetail

urlpatterns = [
    path("", BlogIndex.as_view()),
    path("<int:pk>", ArticleDetail.as_view(), name="article_detail")
]
