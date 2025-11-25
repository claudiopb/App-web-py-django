from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,'myfirst.html')

def alumnos(request):
    return render(request,'lista_alumnos.html')

def nosotros(request):
    return render(request,'nosotros.html')

def crear(request):
    return render(request,'crear.html')

def editar(request):
    return render(request,'editar.html')
