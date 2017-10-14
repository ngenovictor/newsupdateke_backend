from django.db import models

# Create your models here.
class NewsItem(models.Model):
    source_id = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=500)
    summary = models.TextField()
    story = models.TextField()
    article_url = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class NewsSource(models.Model):
    source_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)