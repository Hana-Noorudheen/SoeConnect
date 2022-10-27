from django.shortcuts import render,redirect
from .models import Requests,Notification
# Create your views here.

def index(request):
    return (render(request,'abcd/index.html'))

def req(request):
    if request.method == 'POST':
        Filename = request.POST['filename']
        Desc = request.POST['desc']

        req = Requests()
        req.Filename = Filename
        req.Desc = Desc
        req.save()
        return redirect('/home/req')
    else:
        return (render(request,'abcd/req.html'))

def noti(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        Content = request.POST['Content']

        notif = Notification()
        notif.Title = Title
        notif.Content = Content
        notif.save()
        return redirect('/home/noti')
    else:
        return (render(request,'abcd/noti.html'))


