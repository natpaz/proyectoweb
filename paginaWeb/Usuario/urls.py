from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList

urlpatterns = [
    
    # Acá añadimos las funcionalidades de la app Usuario.
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    
    path('listar', UserList.as_view(), name="listar_usuario"),
    
    
]
