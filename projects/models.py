from django.db import models

# Create your models here.

class Project (models.Model):

    TYPE = (
        ('Website', 'Website'),
        ('Mobile App', 'Mobile App'),
        ('Web App', 'Web App'),
        ('Videogame', 'Videogame'),
        ('3D Model', '3D Model'),
    )

    TAGS = (
        ('Django', 'Django'),
        ('Unity', 'Unity'),
        ('React', 'React'),
        ('Blender', 'Blender'),
        ('Flutter', 'Flutter'),
    )

    title = models.CharField(max_length=100)
    
    project_type = models.CharField(max_length=50, choices=TYPE)  # Use many-to-many relationship
    date_created = models.DateField()
    team = models.BooleanField()
    tags = models.CharField(max_length=50, choices=TAGS) # Use many-to-many relationship

    summary = models.CharField(max_length=200)
    about_project = models.CharField(max_length=500)

    deploy_link = models.URLField()

    def __str__(self):
        return self.title

