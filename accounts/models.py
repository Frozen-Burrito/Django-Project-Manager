from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account (models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    username = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default="default-profile-pic.jpg", null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)