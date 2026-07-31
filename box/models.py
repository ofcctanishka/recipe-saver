from django.db import models

# Create your models here.
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    process = models.TextField()

    def __str__(self):
        return self.name