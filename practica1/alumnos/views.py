from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,'myfirst.html')

def nosotros(request):
    return render(request,'nosotros.html')
