from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()