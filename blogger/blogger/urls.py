"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import index_page, contact_page, about_page, sign_in_page, sign_up_page, logout_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('blog/', include("blog.urls")),
    path('ticket/', include('ticket.urls')),
    path('contact', contact_page),
    path('about', about_page),
    path('signin', sign_in_page),
    path('signup', sign_up_page),
    path('logout', logout_route),
]
