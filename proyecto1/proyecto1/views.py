from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Alumnos 5 C Primera Pagina con Django")
