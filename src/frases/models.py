from django.db import models
from autores.models import Autor

# Create your models here.
class Frase(models.Model):
    """
    Representa una frase dicha por uno de los autores
    """
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=200)
    fecha = models.DateField(blank=True, null=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.contenido}"