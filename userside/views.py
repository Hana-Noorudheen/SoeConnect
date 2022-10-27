
from django.shortcuts import render,redirect
from adminside.models import Students,Requests,File,Notification
# Create your views here.

def index(request):
    return (render(request,'User/reg.html'))

def regSuccess(request):
    return (render(request, 'User/regSuccess.html'))



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



            return (render(request, 'User/regSuccess.html'))
            # return redirect('/user/regSuccess')

def homeuser(request):

    return (render(request, 'User/homeuser.html'))

def userupload(request):
    req = Requests.objects.all()
    return render(request,'User/userupload.html',{'reqs':req})

def upload(request,id):
    if request.method == 'POST':
        file = File()
        if len(request.FILES['Filename']) != 0:
            fileDetails = request.FILES['Filename']
            file.FileType =fileDetails
            file.FileNum = id
            file.StudentNum = 1
            file.save()
        return redirect('/user/payment_form')
    else:
        req = Requests.objects.get(id=id)
        return render(request, 'User/upload.html',{'req':req})


def usernoti(request):
    notis = Notification.objects.all()
    return render(request,'User/usernoti.html',{'notis':notis})