from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    phone = models.CharField(max_length=15)
    id_card = models.IntegerField(max_length=15)
    image = models.ImageField(upload_to="Profile/images" , blank=True , null=True)

    def __str__(self):
        return f"{self.user.email} - {self.user.username}"
