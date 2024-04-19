from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
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
#         return HttpResponse("Llegué con método GET")

#     if request.method == 'POST':
#         return HttpResponse("Llegué con método POST")

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'foto']
    template_name = 'autores/autores_edit.html'
    success_url = 'http://localhost:8000/autores/'


class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'foto']
    template_name = 'autores/autores_edit.html'
    success_url = 'http://localhost:8000/autores/'


def autor_cambiar_estado(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = not(autor.activo)
    autor.save()
    return redirect("autores:autores_list")


def autor_frases(request, id):
    autor = get_object_or_404(Autor, id=id)
    frases = autor.frase_set.all()
    return render(request, 'frases/frases_list.html', {'lista_de_frases': frases})