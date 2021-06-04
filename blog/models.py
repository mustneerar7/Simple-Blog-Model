from django.db import models
from django.urls import reverse

# Created my models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    time = models.TimeField(default="12:12:00")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')