from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Autor 

# Create your views here.
def autores_list(request):
    autores = Autor.objects.all()
    return render(request, 'autores/autores_list.html', {'autores': autores})


def autor_por_id(request, id):
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'autores/autores_id.html', {'autor': autor})


# def autor_crear(request):
#     if request.method == 'GET':
#         return HttpResponse(content="Debo mostrar el formulario para cargar datos")

#     if request.method == 'POST':
#         return HttpResponse(content="ALTA DEL NUEVO AUTOR")

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento']
    template_name = 'autores/autores_edit.html'
    success_url = 'http://localhost:8000/autores/'