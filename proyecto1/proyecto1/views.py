from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Alumnos 5 C Primera Pagina con Django")

def despedida(request):
    return HttpResponse("Hasta Luego 5 C")
