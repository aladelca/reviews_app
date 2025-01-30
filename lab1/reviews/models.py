from django.db import models

# Review model

class Review(models.Model):
    review = models.TextField(max_length=4000)