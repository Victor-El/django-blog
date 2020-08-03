from django.urls import path

from .views import submit_ticket, ticket_success


urlpatterns = [
    path("submit", submit_ticket),
    path("", ticket_success),
]
