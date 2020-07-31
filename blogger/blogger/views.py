from django.shortcuts import render


def index_page(request, *args, **kwargs):
    context = {
        "app_name": "Blogger"
    }
    return render(request, "index.html", context)