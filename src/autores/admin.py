from django.contrib import admin
from .models import Autor

# Register your models here.
# admin.site.register(Autor)

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'modificado']
    fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'modificado']
    list_filter = ['nombre', 'fecha_nacimiento']
    ordering = ['fecha_nacimiento']

admin.site.register(Autor, AutorAdmin)