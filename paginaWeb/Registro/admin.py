from django.contrib import admin
from .models import Formulario, Cliente

# Acá registramos los modelos.
admin.site.register(Formulario)
admin.site.register(Cliente)
