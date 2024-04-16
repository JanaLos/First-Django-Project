from django.db import models

#tridy musime proparovat s admin.py, aby se v prihlaseni pres admina zobrazila nova polozka!!!
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    on_stock = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author)


class Gendr(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
