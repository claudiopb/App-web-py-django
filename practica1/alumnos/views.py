from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>hola alumnos de 5C De programacion</h1>")
dir