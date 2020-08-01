from django.shortcuts import render

context = {
        "app_name": "Blogger"
    }


def index_page(request, *args, **kwargs):
    return render(request, "index.html", context)


def contact_page(request, *args, **kwargs):
    return render(request, "contact.html", context)


def about_page(request, *args, **kwargs):
    return render(request, "about.html", context)