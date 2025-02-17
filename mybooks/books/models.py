from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 50)
    pages = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(500)])
    author = models.CharField(null = True, max_length = 80)
    is_bestseller = models.BooleanField(default = False)

    def __str__(self):
        return f'Nazev knihy: {self.title}, pocet stran: {self.pages}, autor: {self.author}'