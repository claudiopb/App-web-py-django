from django.shortcuts import render
from django.http import HttpResponse
import datetime

documento = "<HTML><BODY><H1>Hola Alumnos 5 C Primera Pagina con Django</H1></BODY></HTML>"
def saludo(request):
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego 5 C")

def lafecha(request):
    fecha_actual = datetime.datetime.now()

    documento= """<HTML>
    <BODY>
    <H1>Fecha y hora actual %s</H1>
    </BODY>
    </HTML>""" %fecha_actual

    return HttpResponse(documento)

def calculaedad(request,anio):
    edadActual = 48
    periodo = anio - 2025
    edadFutura = edadActual + periodo
    doc = f"<HTML><BODY><H2>En el año {anio} tendras {edadFutura} años </H2></BODY></HTML>"
    return HttpResponse(doc)

def calculaedad2(request,edad,anio):
    
    periodo = anio - 2025
    edadFutura = edad + periodo
    doc = f"<HTML><BODY><H2>En el año {anio} tendras {edadFutura} años </H2></BODY></HTML>"
    return HttpResponse(doc)
