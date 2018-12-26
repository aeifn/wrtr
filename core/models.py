from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=500, blank=False)
    text=models.TextField(blank=False)
