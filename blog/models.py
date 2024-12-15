from django.db import models
from django.utils import timezone
# Create your models here.

#creating the database model for the blog
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.title