from django.urls import path
from .views import (
    autores_list, 
    autor_por_id, 
    AutorCreateView, 
    AutorUpdateView, 
    autor_cambiar_estado,
    autor_frases,
    autores_buscar )


app_name = 'autores'

urlpatterns = [
    path('', autores_list, name='autores_list'),
    path('<int:id>/', autor_por_id, name='autor_por_id'),
    path('crear/', AutorCreateView.as_view(), name='autores_crear'),
    # path('crear_funcion/', autor_crear),
    path('modificar/<int:pk>/', AutorUpdateView.as_view(), name='autores_modificar'),
    path('cambiar_estado/<int:id>/', autor_cambiar_estado, name='autor_cambiar_estado'),
    path('frases/<int:id>/', autor_frases, name='autor_frases'),
    path('buscar/', autores_buscar, name='buscar')
]
