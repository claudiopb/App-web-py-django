from django.http import HttpResponse

def saludo(request):  #primera Vista

    return HttpResponse("Hola 5 C Primera Pagina en Django")