from django.db import models

# Create your models here.
class Photorecorder(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField()
    about=models.TextField(max_length=100)

    def __str__(self):
        return self.name