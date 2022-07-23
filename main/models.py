from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    snippet = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    body = RichTextField()

    #def get_absolute_url(self):
    #return reverse('index')

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    posted_at = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.TextField()