from django.db import models

# Create your models here.

class Students(models.Model):

    Name = models.CharField(max_length=100, default=None)
    RegNumber = models.IntegerField(blank=True, null=True, default=None)
    Email = models.EmailField(max_length=100, default=None)
    Mob = models.CharField(max_length=13, default=None)
    Semester = models.IntegerField(default=None)
    Photo = models.ImageField(upload_to='pics')

class Requests(models.Model):
    Filename = models.CharField(max_length=100, default=None)
    Desc = models.TextField()

class File(models.Model):
    FileNum = models.ForeignKey(Requests,on_delete=models.CASCADE, default=False)
    StudentNum = models.ForeignKey(Students,on_delete=models.CASCADE, default=False)
    FileType =  models.FileField(upload_to='files',default=None)

class Notification(models.Model):
    Title = models.CharField(max_length=100, default=None)
    Content = models.TextField()

