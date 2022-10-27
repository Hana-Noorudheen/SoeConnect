from django.shortcuts import render

# Create your views here.

def index(request):
    return (render(request,'Admin/index.html'))

def req(request):
    return (render(request,'Admin/req.html'))

def noti(request):
    return (render(request,'Admin/noti.html'))