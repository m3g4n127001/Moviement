from django.db import models
from django.db.models.fields import DurationField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    year = models.DateField(auto_now_add=True)
    thumb = models.ImageField()
    slug = models.SlugField()
    story = models.TextField()
    video = models.FileField()

    def __str__(self):
        return self.title