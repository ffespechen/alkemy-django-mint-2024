from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Frase


# Create your views here.
class FrasesListView(generic.ListView):
    queryset = Frase.objects.all()
    template_name = 'frases/frases_list.html'
    context_object_name = 'lista_de_frases'


class FrasesCreateView(CreateView):
    model = Frase
    # fields = '__all__'
    fields = ['autor', 'contenido', 'fecha']
    template_name = 'frases/frases_edit.html'
    success_url = 'http://localhost:8000/frases/'

class FrasesUpdateView(UpdateView):
    model = Frase
    fields = '__all__'
    template_name = 'frases/frases_edit.html'
    success_url = 'http://localhost:8000/frases/'   