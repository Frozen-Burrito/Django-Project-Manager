from django.db import models

from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

class Account (models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    username = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField(null=True)
    site = models.URLField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=300, blank=True, null=True)

    profile_pic = models.ImageField(default="default-profile-pic.jpg", null=True, blank=True)
    backdrop = models.ImageField(default="home_backdrop.jpg", null=True, blank=True)

    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return str(self.username)