from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def primera_vista(request):
    return HttpResponse(content="Hola desde Django!!!!")

def segunda_vista(request):
    return HttpResponse(content="<h1>ESTA ES LA SEGUNDA VISTA</h1>")

def vista_html(request, dinamico, numero):
    return render(request, 'prueba/prueba_mensajes.html', 
            { 'valor': dinamico, 
              'anios': numero })