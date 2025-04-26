from django.db import models

# Create your models here.
class Jokes(models.Model):
    user_name = models.CharField(max_length = 100)
    joke_text = models.TextField()
    rating = models.IntegerField()