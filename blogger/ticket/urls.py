from django.urls import path

from .views import submit_ticket


urlpatterns = [
    path("", submit_ticket)
]
