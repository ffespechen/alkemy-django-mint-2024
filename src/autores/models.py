from django.db import models
from django.urls import reverse


# Create your models here.
class Autor(models.Model):
    """ Clase que representa a los autores de las frases """
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.nombre.upper()}"
    
    def get_absolute_url(self):
        return reverse("autores:autor_por_id", kwargs={"id": self.id})
    