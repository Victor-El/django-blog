from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk})

    
    def get_update_url(self):
        return reverse("blog:article_update", kwargs={"pk": self.pk})


    def get_delete_url(self):
        return reverse("blog:article_delete", kwargs={"pk": self.pk})
    
