from django.http import HttpResponse
import datetime

documento = "<HTML><BODY><H1>Hola Alumnos 5 C Primera Pagina con Django</H1></BODY></HTML>"
def saludo(request):
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego 5 C")

def fecha():
    fecha_actual = datetime.datetime.now()

    documento= """<HTML>
    <BODY>
    <H1>Fecha y hora actual %s</H1>
    </BODY>
    </HTML>""" %fecha_actual

    return HttpResponse(documento)
