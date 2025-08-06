from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categories (models.Model):
    title = models.CharField(max_length= 100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Post (models.Model):

    author = models.ForeignKey(User , on_delete= models.CASCADE)
    category = models.ManyToManyField(Categories)
    title = models.CharField(max_length=80)
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"{self.title} - {self.pub_date}"