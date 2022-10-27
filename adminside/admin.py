from django.contrib import admin
from .models import Students,Requests,File,Notification
# Register your models here.

admin.site.register(Students)
admin.site.register(Requests)
admin.site.register(File)
admin.site.register(Notification)