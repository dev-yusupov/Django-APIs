from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)