from django.shortcuts import redirect, render

from .models import Ticket

# Create your views here.

def submit_ticket(request, *args, **kwargs):
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        message = request.POST['message']

        Ticket.objects.create(name=name, title=title, message=message)
        return redirect('/ticket_success')


def ticket_success(request, *args, **kwargs):
    return render(request, 'ticket_success.html', {})