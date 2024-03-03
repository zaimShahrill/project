from django.db import models

# Create your models here.
class Hobbies(models.Model):
   name = models.TextField()
   hobby = models.TextField()
   gender = models.CharField(max_length=1)