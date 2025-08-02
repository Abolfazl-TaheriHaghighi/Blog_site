from django.db import models

class Post (models.Model):

    title = models.CharField(max_length=80)
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/post')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} - {self.updated}"