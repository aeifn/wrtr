from django.db import models

# Create your models here.

class Article(models.Model):
    text=models.TextField(blank=False)
