from django.db import models

# Create your models here.

class Students(models.Model):

    Name = models.CharField(max_length=100, default=None)
    RegNumber = models.IntegerField(blank=True, null=True, default=None)
    Email = models.EmailField(max_length=100, default=None)
    Mob = models.CharField(max_length=13, default=None)
    Semester = models.IntegerField(default=None)
    Photo = models.ImageField(upload_to='pics')



