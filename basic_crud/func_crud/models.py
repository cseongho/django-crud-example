from django.db import models

# Create your models here.

class Crud(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    src = models.ImageField(blank=True)
