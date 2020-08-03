from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=120)
    message = models.TextField()