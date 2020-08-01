from django.urls import path

from .views import BlogIndex

urlpatterns = [
    path("", BlogIndex.as_view()),
]
