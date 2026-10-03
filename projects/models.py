from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year =  models.IntegerField()
    image = models.ImageField(upload_to='projectsimg/')
    repository = models.URLField()
    skills = models.ManyToManyField("Skills")

    def __str__(self):
        return self.name