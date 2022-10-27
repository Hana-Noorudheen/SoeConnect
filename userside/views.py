
from django.shortcuts import render
from adminside.models import Students
# Create your views here.

def index(request):
    return (render(request,'Admin/index.html'))


def register(request):
    if request.method == 'POST':
            Name = request.POST['Name']
            Gender = request.POST['Gender']
            Address = request.POST['Address']
            Mob = request.POST['Mob']


            Email = request.POST['Email']