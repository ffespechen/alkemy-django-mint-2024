from django.urls import path
from .views import autores_list, autor_por_id, AutorCreateView

app_name = 'autores'

urlpatterns = [
    path('', autores_list, name='autores_list'),
    path('<int:id>/', autor_por_id, name='autor_por_id'),
    # path('crear/', autor_crear, name='autor_crear'),
    path('crear/', AutorCreateView.as_view(), name='autores_crear'),
]
