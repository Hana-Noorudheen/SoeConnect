
from django.shortcuts import render,redirect
from adminside.models import Students
# Create your views here.

def index(request):
    return (render(request,'User/reg.html'))



def register(request):
    if request.method == 'POST':
            Name = request.POST['Name']
            RegNum = request.POST['RegNum']
            Semester = request.POST['Semester']
            Mob = request.POST['Mob']


            Email = request.POST['Email']

            user_obj = Students()
            user_obj.Name = Name
            user_obj.RegNumber = RegNum
            user_obj.Semester = Semester
            user_obj.Mob = Mob
            user_obj.Email = Email

            user_obj.save()

            return redirect('/user/regSuccess')