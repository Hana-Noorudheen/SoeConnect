from django.shortcuts import render

# Create your views here.

def index(request):
    return (render(request,'abcd/index.html'))

def req(request):
    return (render(request,'abcd/req.html'))

def noti(request):
    return (render(request,'abcd/noti.html'))

