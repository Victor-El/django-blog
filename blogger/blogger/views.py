from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import SignInForm, SignUpForm

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


def sign_up_page(request, *args, **kwargs):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(email=email, password=password, username=email)
        print(user)
        return redirect("/signin")

    context['form'] = form
    return render(request, "signup.html", context)