from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import SignInForm

context = {
        "app_name": "Blogger"
    }


def index_page(request, *args, **kwargs):
    return render(request, "index.html", context)


def contact_page(request, *args, **kwargs):
    return render(request, "contact.html", context)


def about_page(request, *args, **kwargs):
    return render(request, "about.html", context)


def sign_in_page(request, *args, **kwargs):
    form = SignInForm(request.POST or None)
    if form.is_valid():
        print(request.POST)
    context['form'] = form
    return render(request, "signin.html", context)